"""Integration contracts for the Topic 06 benchmark suite."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE_DIR = ROOT / "tests" / "topic06" / "cases"
RUNNER_PATH = ROOT / "scripts" / "run_topic06_benchmarks.py"


def _load_runner():
    spec = importlib.util.spec_from_file_location("topic06_runner", RUNNER_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_topic06_case_manifest_is_complete():
    dsl_files = sorted(CASE_DIR.rglob("*.dsl"))
    meta_files = sorted(CASE_DIR.rglob("*.meta.json"))

    assert len(dsl_files) == 23
    assert len(meta_files) == 23
    assert {path.with_suffix("") for path in dsl_files} == {
        path.with_suffix("").with_suffix("") for path in meta_files
    }


def test_compiler_emits_register_map_for_topic06_case(tmp_path):
    from scratchv.compiler import CompilerConfig, CompilerDriver

    driver = CompilerDriver(CompilerConfig(
        backend="riscv",
        optimize_level="all",
        reg_alloc="greedy",
    ))
    source = CASE_DIR / "activation" / "relu_add.dsl"
    result = driver.compile(str(source), str(tmp_path / "relu_add.s"))

    assert result.success
    assert result.stats["register_map"]["input"] == "t0"
    assert result.stats["register_map"]["bias"] == "t1"


def test_runner_loads_compiler_register_map(tmp_path):
    runner = _load_runner()
    register_map_file = tmp_path / "registers.json"
    register_map_file.write_text(
        json.dumps({
            "schema_version": 1,
            "register_map": {"input": "t0", "bias": "t1"},
        }),
        encoding="utf-8",
    )

    initial = runner.load_initial_registers(
        register_map_file,
        {"input": -3, "bias": 7, "tensor": [1, 2]},
    )

    assert initial == {"t0": -3, "t1": 7}


def test_topic06_report_paths_are_portable():
    runner = _load_runner()
    case = runner.TEST_DIR / "activation" / "relu_only.dsl"

    assert runner._report_path(case) == "tests/topic06/cases/activation/relu_only.dsl"


def test_runner_uses_project_layout():
    runner = _load_runner()

    assert runner.PROJECT_ROOT == ROOT
    assert runner.TEST_DIR == ROOT / "tests" / "topic06" / "cases"
    assert runner.BUILD_DIR == ROOT / "build" / "topic06"
    assert runner.REPORT_DIR == ROOT / "benchmark_reports" / "topic06"
    assert runner.BASELINE_FILE == ROOT / "benchmarks" / "topic06" / "baseline.json"


def test_interpreter_verifies_scalar_and_tensor_cases():
    runner = _load_runner()

    for relative_path in (
        Path("activation/relu_add.dsl"),
        Path("tensor/matmul_2x2.dsl"),
    ):
        dsl_file = CASE_DIR / relative_path
        metadata = runner.load_metadata(dsl_file)
        result = runner.run_interpreter(dsl_file, metadata["inputs"])

        assert result["success"]
        assert runner.values_equal(
            result["return_value"],
            metadata["expected_return"],
        )


def test_interpreter_marks_control_flow_as_unsupported():
    runner = _load_runner()

    for relative_path in (
        Path("loop/loop_add_4.dsl"),
        Path("branch/if_else.dsl"),
    ):
        dsl_file = CASE_DIR / relative_path
        metadata = runner.load_metadata(dsl_file)
        result = runner.run_interpreter(dsl_file, metadata["inputs"])

        assert result["status"] == "UNSUPPORTED"
        assert not result["success"]


def test_runner_writes_independent_backend_case_report(tmp_path, monkeypatch):
    runner = _load_runner()
    report_dir = tmp_path / "reports"
    monkeypatch.setattr(runner, "BUILD_DIR", tmp_path / "build")
    monkeypatch.setattr(runner, "REPORT_DIR", report_dir)
    monkeypatch.setattr(runner, "REPORT_FILE", report_dir / "report.md")
    monkeypatch.setattr(runner, "JSON_REPORT_FILE", report_dir / "report.json")
    monkeypatch.setattr(runner, "HTML_REPORT_FILE", report_dir / "report.html")
    monkeypatch.setattr(runner, "CHART_FILE", report_dir / "chart.png")
    monkeypatch.setattr(runner, "FAILURE_DIR", report_dir / "failures")
    monkeypatch.setattr(runner, "CASE_REPORT_DIR", report_dir / "cases")

    exit_code = runner.main([
        "--filter", "relu_only",
        "--verification-backend", "both",
        "--fail-on-test-failure",
    ])

    assert exit_code == 0
    payload = json.loads((report_dir / "report.json").read_text(encoding="utf-8"))
    result = payload["results"][0]
    assert payload["schema_version"] == 2
    assert result["interpreter_status"] == "PASS"
    assert result["tinyfive_status"] == "PASS"
    assert result["backend_outputs_match"] is True
    assert result["static_asm_instruction_count"] > 0
    assert (report_dir / "cases/activation-relu_only.md").exists()
    assert (report_dir / "cases/activation-relu_only.json").exists()


def test_tinyfive_input_abi_marks_tensor_inputs_unsupported():
    runner = _load_runner()

    supported, reason = runner.tinyfive_input_abi_supported({"A": [[1, 2], [3, 4]]})

    assert not supported
    assert "A" in reason


def test_cost_model_baseline_uses_versioned_schema(tmp_path, monkeypatch):
    runner = _load_runner()
    baseline_file = tmp_path / "baseline.json"
    monkeypatch.setattr(runner, "BASELINE_FILE", baseline_file)

    runner.save_baseline([{
        "name": "relu_only",
        "category": "activation",
        "avg_instr_count": 5.0,
        "benchmark_runs": 3,
        "tinyfive_status": "PASS",
        "cost_model": {
            "static_asm_instructions": 3,
            "machine_instructions": 6,
            "code_size_bytes": 24,
            "dynamic_instructions": 5.0,
        },
    }])

    payload = json.loads(baseline_file.read_text(encoding="utf-8"))
    assert payload["schema_version"] == 2
    assert payload["primary_metric"] == "dynamic_instructions"
    assert payload["cases"]["relu_only"]["cost_model"]["code_size_bytes"] == 24
    assert runner.load_baseline() == payload["cases"]


def test_interpreter_only_mode_cannot_replace_cost_model_baseline(tmp_path, monkeypatch):
    runner = _load_runner()
    baseline_file = tmp_path / "baseline.json"
    monkeypatch.setattr(runner, "BASELINE_FILE", baseline_file)

    exit_code = runner.main([
        "--benchmark", "1",
        "--update-baseline",
        "--verification-backend", "interpreter",
    ])

    assert exit_code == 2
    assert not baseline_file.exists()

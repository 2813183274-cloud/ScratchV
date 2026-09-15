# vector_add 测试详情

## 基本信息

- 类别: elementwise
- DSL: `tests/topic06/cases/elementwise/vector_add.dsl`
- 描述: Single add over two symbolic vector inputs.
- 总体状态: PASS
- 验证模式: both

## 后端能力矩阵

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败类型 | 错误 |
|---|---|---|---|---|---|
| DSLInterpreter | PASS | 5 | True | null | null |
| TinyFive | PASS | 5 | True | null | null |

- 期望输出: 5
- 两后端输出一致: True
- TinyFive 输入 ABI 可用: True
- TinyFive 输入 ABI 说明: null

## 性能指标

- 静态汇编指令数: 3
- 编码后机器指令数: 3
- 代码大小(bytes): 12
- TinyFive 动态执行指令数: 3
- TinyFive 分类计数: {'total': 3, 'load': 0, 'store': 0, 'mul': 0, 'add': 2, 'madd': 0, 'branch': 0}
- 编译耗时(s): 0.085438
- 解释器耗时(s): 0.129065
- TinyFive 模拟耗时(s): 0.147592
- 总耗时(s): 0.818664
- 基线动态指令数: 3.0
- 动态指令变化率(%): 0.0
- 是否退化: False

- Cost model 指标: {'static_asm_instructions': 3, 'machine_instructions': 3, 'code_size_bytes': 12, 'dynamic_instructions': 3.0, 'dynamic_load': 0.0, 'dynamic_store': 0.0, 'dynamic_mul': 0.0, 'dynamic_add': 2.0, 'dynamic_madd': 0.0, 'dynamic_branch': 0.0}
- Cost model 对比: {'static_asm_instructions': {'current': 3, 'baseline': 3, 'delta': 0, 'delta_pct': 0.0, 'regressed': False}, 'machine_instructions': {'current': 3, 'baseline': 3, 'delta': 0, 'delta_pct': 0.0, 'regressed': False}, 'code_size_bytes': {'current': 12, 'baseline': 12, 'delta': 0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_instructions': {'current': 3.0, 'baseline': 3.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_load': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_store': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_mul': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_add': {'current': 2.0, 'baseline': 2.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_madd': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_branch': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}}
- Cost model 是否退化: False

## 编译信息

- 命令: `'D:\anaconda3\python.exe' -m scratchv.main 'D:\PycharmProjects\ScratchV\ScratchV\tests\topic06\cases\elementwise\vector_add.dsl' -o 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\vector_add.s' --optimize all --emit-register-map 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\vector_add.registers.json'`
- 返回码: 0
- 编译错误: null
- 失败日志: null
- 寄存器映射: `build/topic06/vector_add.registers.json`
- 汇编文件: `build/topic06/vector_add.s`

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
.entry:
    add t2, t0, t1
    mv a0, t2  # return value
    jalr zero, ra  # ret
```

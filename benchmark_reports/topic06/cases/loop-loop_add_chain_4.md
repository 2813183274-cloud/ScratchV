# loop_add_chain_4 测试详情

## 基本信息

- 类别: loop
- DSL: `tests/topic06/cases/loop/loop_add_chain_4.dsl`
- 描述: Run a four-iteration loop whose body computes two chained adds; final returned value is the last loop-body result.
- 总体状态: PASS
- 验证模式: both

## 后端能力矩阵

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败类型 | 错误 |
|---|---|---|---|---|---|
| DSLInterpreter | UNSUPPORTED | None | False | interpreter_control_flow_unsupported | unsupported control flow: for |
| TinyFive | PASS | 9 | True | null | null |

- 期望输出: 9
- 两后端输出一致: null
- TinyFive 输入 ABI 可用: True
- TinyFive 输入 ABI 说明: null

## 性能指标

- 静态汇编指令数: 8
- 编码后机器指令数: 9
- 代码大小(bytes): 36
- TinyFive 动态执行指令数: 26
- TinyFive 分类计数: {'total': 26, 'load': 0, 'store': 0, 'mul': 0, 'add': 16, 'madd': 0, 'branch': 5}
- 编译耗时(s): 0.086606
- 解释器耗时(s): 0.000088
- TinyFive 模拟耗时(s): 0.157277
- 总耗时(s): 0.703120
- 基线动态指令数: 26.0
- 动态指令变化率(%): 0.0
- 是否退化: False

- Cost model 指标: {'static_asm_instructions': 8, 'machine_instructions': 9, 'code_size_bytes': 36, 'dynamic_instructions': 26.0, 'dynamic_load': 0.0, 'dynamic_store': 0.0, 'dynamic_mul': 0.0, 'dynamic_add': 16.0, 'dynamic_madd': 0.0, 'dynamic_branch': 5.0}
- Cost model 对比: {'static_asm_instructions': {'current': 8, 'baseline': 8, 'delta': 0, 'delta_pct': 0.0, 'regressed': False}, 'machine_instructions': {'current': 9, 'baseline': 9, 'delta': 0, 'delta_pct': 0.0, 'regressed': False}, 'code_size_bytes': {'current': 36, 'baseline': 36, 'delta': 0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_instructions': {'current': 26.0, 'baseline': 26.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_load': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_store': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_mul': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_add': {'current': 16.0, 'baseline': 16.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_madd': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_branch': {'current': 5.0, 'baseline': 5.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}}
- Cost model 是否退化: False

## 编译信息

- 命令: `'D:\anaconda3\python.exe' -m scratchv.main 'D:\PycharmProjects\ScratchV\ScratchV\tests\topic06\cases\loop\loop_add_chain_4.dsl' -o 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\loop_add_chain_4.s' --optimize all --emit-register-map 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\loop_add_chain_4.registers.json'`
- 返回码: 0
- 编译错误: null
- 失败日志: null
- 寄存器映射: `build/topic06/loop_add_chain_4.registers.json`
- 汇编文件: `build/topic06/loop_add_chain_4.s`

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
.entry:
    add t2, t0, t1
    li t3, 0  # loop init
.Lloop_header_1:
    bge t3, 4, .Lloop_exit_3
.Lloop_body_2:
    add t5, t2, t4
    addi t3, t3, 1  # loop inc
    j .Lloop_header_1
.Lloop_exit_3:
    mv a0, t5  # return value
    jalr zero, ra  # ret
```

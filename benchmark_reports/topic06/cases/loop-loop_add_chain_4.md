# loop_add_chain_4 测试详情

## 基本信息

- 类别: loop
- DSL: `tests/topic06/cases/loop/loop_add_chain_4.dsl`
- 描述: Run a four-iteration loop whose body computes two chained adds; final returned value is the last loop-body result.
- 总体状态: FAIL
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

- 静态汇编指令数: 20
- 编码后机器指令数: 21
- 代码大小(bytes): 84
- TinyFive 动态执行指令数: 61
- TinyFive 分类计数: {'total': 61, 'load': 18, 'store': 16, 'mul': 0, 'add': 17, 'madd': 0, 'branch': 5}
- 编译耗时(s): 0.095539
- 解释器耗时(s): 0.000102
- TinyFive 模拟耗时(s): 0.165189
- 总耗时(s): 0.736818
- 基线动态指令数: 26.0
- 动态指令变化率(%): 134.6154
- 是否退化: True

- Cost model 指标: {'static_asm_instructions': 20, 'machine_instructions': 21, 'code_size_bytes': 84, 'dynamic_instructions': 61.0, 'dynamic_load': 18.0, 'dynamic_store': 16.0, 'dynamic_mul': 0.0, 'dynamic_add': 17.0, 'dynamic_madd': 0.0, 'dynamic_branch': 5.0}
- Cost model 对比: {'static_asm_instructions': {'current': 20, 'baseline': 8, 'delta': 12, 'delta_pct': 150.0, 'regressed': True}, 'machine_instructions': {'current': 21, 'baseline': 9, 'delta': 12, 'delta_pct': 133.3333, 'regressed': True}, 'code_size_bytes': {'current': 84, 'baseline': 36, 'delta': 48, 'delta_pct': 133.3333, 'regressed': True}, 'dynamic_instructions': {'current': 61.0, 'baseline': 26.0, 'delta': 35.0, 'delta_pct': 134.6154, 'regressed': True}, 'dynamic_load': {'current': 18.0, 'baseline': 0.0, 'delta': 18.0, 'delta_pct': None, 'regressed': True}, 'dynamic_store': {'current': 16.0, 'baseline': 0.0, 'delta': 16.0, 'delta_pct': None, 'regressed': True}, 'dynamic_mul': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_add': {'current': 17.0, 'baseline': 16.0, 'delta': 1.0, 'delta_pct': 6.25, 'regressed': True}, 'dynamic_madd': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_branch': {'current': 5.0, 'baseline': 5.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}}
- Cost model 是否退化: True

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
  addi sp, sp, -16  # create stack frame
.entry:
    add t3, t0, t1
    li t0, 0  # loop init
    sw t0, 12(sp)  # spill v_1 [regalloc:spill]
    sw t2, 8(sp)  # spill c [regalloc:spill]
    sw t3, 4(sp)  # spill v_2 [regalloc:spill]
.Lloop_header_1:
    lw t0, 12(sp)  # reload v_1 [regalloc:reload]
    sw t0, 12(sp)  # spill v_1 [regalloc:spill]
    bge t0, 4, .Lloop_exit_3
.Lloop_body_2:
    lw t0, 4(sp)  # reload v_2 [regalloc:reload]
    lw t1, 8(sp)  # reload c [regalloc:reload]
    add t2, t0, t1
    lw t0, 12(sp)  # reload v_1 [regalloc:reload]
    addi t0, t0, 1  # loop inc
    sw t0, 12(sp)  # spill v_1 [regalloc:spill]
    sw t2, 0(sp)  # spill v_3 [regalloc:spill]
    j .Lloop_header_1
.Lloop_exit_3:
    lw t0, 0(sp)  # reload v_3 [regalloc:reload]
    mv a0, t0  # return value
    jalr zero, ra  # ret
```

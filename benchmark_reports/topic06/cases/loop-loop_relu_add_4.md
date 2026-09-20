# loop_relu_add_4 测试详情

## 基本信息

- 类别: loop
- DSL: `tests/topic06/cases/loop/loop_relu_add_4.dsl`
- 描述: Run a four-iteration loop whose body computes add followed by ReLU; final returned value is the last loop-body result.
- 总体状态: FAIL
- 验证模式: both

## 后端能力矩阵

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败类型 | 错误 |
|---|---|---|---|---|---|
| DSLInterpreter | UNSUPPORTED | None | False | interpreter_control_flow_unsupported | unsupported control flow: for |
| TinyFive | PASS | 2 | True | null | null |

- 期望输出: 2
- 两后端输出一致: null
- TinyFive 输入 ABI 可用: True
- TinyFive 输入 ABI 说明: null

## 性能指标

- 静态汇编指令数: 18
- 编码后机器指令数: 22
- 代码大小(bytes): 88
- TinyFive 动态执行指令数: 60
- TinyFive 分类计数: {'total': 60, 'load': 14, 'store': 15, 'mul': 0, 'add': 17, 'madd': 0, 'branch': 9}
- 编译耗时(s): 0.104160
- 解释器耗时(s): 0.000071
- TinyFive 模拟耗时(s): 0.165995
- 总耗时(s): 0.755380
- 基线动态指令数: 30.0
- 动态指令变化率(%): 100.0
- 是否退化: True

- Cost model 指标: {'static_asm_instructions': 18, 'machine_instructions': 22, 'code_size_bytes': 88, 'dynamic_instructions': 60.0, 'dynamic_load': 14.0, 'dynamic_store': 15.0, 'dynamic_mul': 0.0, 'dynamic_add': 17.0, 'dynamic_madd': 0.0, 'dynamic_branch': 9.0}
- Cost model 对比: {'static_asm_instructions': {'current': 18, 'baseline': 8, 'delta': 10, 'delta_pct': 125.0, 'regressed': True}, 'machine_instructions': {'current': 22, 'baseline': 12, 'delta': 10, 'delta_pct': 83.3333, 'regressed': True}, 'code_size_bytes': {'current': 88, 'baseline': 48, 'delta': 40, 'delta_pct': 83.3333, 'regressed': True}, 'dynamic_instructions': {'current': 60.0, 'baseline': 30.0, 'delta': 30.0, 'delta_pct': 100.0, 'regressed': True}, 'dynamic_load': {'current': 14.0, 'baseline': 0.0, 'delta': 14.0, 'delta_pct': None, 'regressed': True}, 'dynamic_store': {'current': 15.0, 'baseline': 0.0, 'delta': 15.0, 'delta_pct': None, 'regressed': True}, 'dynamic_mul': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_add': {'current': 17.0, 'baseline': 16.0, 'delta': 1.0, 'delta_pct': 6.25, 'regressed': True}, 'dynamic_madd': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_branch': {'current': 9.0, 'baseline': 9.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}}
- Cost model 是否退化: True

## 编译信息

- 命令: `'D:\anaconda3\python.exe' -m scratchv.main 'D:\PycharmProjects\ScratchV\ScratchV\tests\topic06\cases\loop\loop_relu_add_4.dsl' -o 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\loop_relu_add_4.s' --optimize all --emit-register-map 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\loop_relu_add_4.registers.json'`
- 返回码: 0
- 编译错误: null
- 失败日志: null
- 寄存器映射: `build/topic06/loop_relu_add_4.registers.json`
- 汇编文件: `build/topic06/loop_relu_add_4.s`

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
  addi sp, sp, -16  # create stack frame
.entry:
    add t2, t0, t1
    li t0, 0  # loop init
    sw t0, 12(sp)  # spill v_1 [regalloc:spill]
    sw t2, 8(sp)  # spill v_2 [regalloc:spill]
.Lloop_header_1:
    lw t0, 12(sp)  # reload v_1 [regalloc:reload]
    sw t0, 12(sp)  # spill v_1 [regalloc:spill]
    bge t0, 4, .Lloop_exit_3
.Lloop_body_2:
    lw t0, 8(sp)  # reload v_2 [regalloc:reload]
    max t1, t0, 0
    lw t0, 12(sp)  # reload v_1 [regalloc:reload]
    addi t0, t0, 1  # loop inc
    sw t0, 12(sp)  # spill v_1 [regalloc:spill]
    sw t1, 4(sp)  # spill v_3 [regalloc:spill]
    j .Lloop_header_1
.Lloop_exit_3:
    lw t0, 4(sp)  # reload v_3 [regalloc:reload]
    mv a0, t0  # return value
    jalr zero, ra  # ret
```

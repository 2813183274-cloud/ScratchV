# loop_add_4 测试详情

## 基本信息

- 类别: loop
- DSL: `tests/topic06/cases/loop/loop_add_4.dsl`
- 描述: Run a four-iteration loop whose body computes one add; final returned value is the last loop-body result.
- 总体状态: FAIL
- 验证模式: both

## 后端能力矩阵

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败类型 | 错误 |
|---|---|---|---|---|---|
| DSLInterpreter | UNSUPPORTED | None | False | interpreter_control_flow_unsupported | unsupported control flow: for |
| TinyFive | PASS | 5 | True | null | null |

- 期望输出: 5
- 两后端输出一致: null
- TinyFive 输入 ABI 可用: True
- TinyFive 输入 ABI 说明: null

## 性能指标

- 静态汇编指令数: 15
- 编码后机器指令数: 16
- 代码大小(bytes): 64
- TinyFive 动态执行指令数: 44
- TinyFive 分类计数: {'total': 44, 'load': 10, 'store': 11, 'mul': 0, 'add': 13, 'madd': 0, 'branch': 5}
- 编译耗时(s): 0.092592
- 解释器耗时(s): 0.000089
- TinyFive 模拟耗时(s): 0.161210
- 总耗时(s): 0.729026
- 基线动态指令数: 22.0
- 动态指令变化率(%): 100.0
- 是否退化: True

- Cost model 指标: {'static_asm_instructions': 15, 'machine_instructions': 16, 'code_size_bytes': 64, 'dynamic_instructions': 44.0, 'dynamic_load': 10.0, 'dynamic_store': 11.0, 'dynamic_mul': 0.0, 'dynamic_add': 13.0, 'dynamic_madd': 0.0, 'dynamic_branch': 5.0}
- Cost model 对比: {'static_asm_instructions': {'current': 15, 'baseline': 7, 'delta': 8, 'delta_pct': 114.2857, 'regressed': True}, 'machine_instructions': {'current': 16, 'baseline': 8, 'delta': 8, 'delta_pct': 100.0, 'regressed': True}, 'code_size_bytes': {'current': 64, 'baseline': 32, 'delta': 32, 'delta_pct': 100.0, 'regressed': True}, 'dynamic_instructions': {'current': 44.0, 'baseline': 22.0, 'delta': 22.0, 'delta_pct': 100.0, 'regressed': True}, 'dynamic_load': {'current': 10.0, 'baseline': 0.0, 'delta': 10.0, 'delta_pct': None, 'regressed': True}, 'dynamic_store': {'current': 11.0, 'baseline': 0.0, 'delta': 11.0, 'delta_pct': None, 'regressed': True}, 'dynamic_mul': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_add': {'current': 13.0, 'baseline': 12.0, 'delta': 1.0, 'delta_pct': 8.3333, 'regressed': True}, 'dynamic_madd': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_branch': {'current': 5.0, 'baseline': 5.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}}
- Cost model 是否退化: True

## 编译信息

- 命令: `'D:\anaconda3\python.exe' -m scratchv.main 'D:\PycharmProjects\ScratchV\ScratchV\tests\topic06\cases\loop\loop_add_4.dsl' -o 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\loop_add_4.s' --optimize all --emit-register-map 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\loop_add_4.registers.json'`
- 返回码: 0
- 编译错误: null
- 失败日志: null
- 寄存器映射: `build/topic06/loop_add_4.registers.json`
- 汇编文件: `build/topic06/loop_add_4.s`

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
    lw t0, 12(sp)  # reload v_1 [regalloc:reload]
    addi t0, t0, 1  # loop inc
    sw t0, 12(sp)  # spill v_1 [regalloc:spill]
    j .Lloop_header_1
.Lloop_exit_3:
    lw t0, 8(sp)  # reload v_2 [regalloc:reload]
    mv a0, t0  # return value
    jalr zero, ra  # ret
```

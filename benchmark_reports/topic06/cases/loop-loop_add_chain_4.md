# loop_add_chain_4 测试详情

## 基本信息

- 类别: loop
- DSL: `tests/topic06/cases/loop/loop_add_chain_4.dsl`
- 描述: Run a four-iteration loop whose body computes two chained adds; final returned value is the last loop-body result.
- 总体状态: PASS

## 后端结果

- 预期输出: 9

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败原因 |
|---|---|---|---|---|
| DSLInterpreter | UNSUPPORTED | null | null | unsupported control flow: for |
| TinyFive | PASS | 9 | True | null |

## 性能指标

| 指标 | 当前值 | 基线 | 变化率(%) | 是否退化 |
|---|---:|---:|---:|---|
| 静态汇编指令数 | 20 | 20 | 0.0 | False |
| 编码后机器指令数 | 21 | 21 | 0.0 | False |
| 代码大小(bytes) | 84 | 84 | 0.0 | False |
| TinyFive 动态指令数 | 61 | 61 | 0.0 | False |
| 动态 load | 18 | 18 | 0.0 | False |
| 动态 store | 16 | 16 | 0.0 | False |
| 动态 mul | 0 | 0 | 0.0 | False |
| 动态 add | 17 | 17 | 0.0 | False |
| 动态 madd | 0 | 0 | 0.0 | False |
| 动态 branch | 5 | 5 | 0.0 | False |

## 耗时诊断

- 编译耗时(s): 0.096816
- 解释器耗时(s): 0.000060
- TinyFive 模拟耗时(s): 0.163816

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

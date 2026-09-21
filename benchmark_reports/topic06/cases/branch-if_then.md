# if_then 测试详情

## 基本信息

- 类别: branch
- DSL: `tests/topic06/cases/branch/if_then.dsl`
- 描述: if/else branch returns add result when flag is non-zero.
- 总体状态: PASS

## 后端结果

- 预期输出: 13

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败原因 |
|---|---|---|---|---|
| DSLInterpreter | UNSUPPORTED | null | null | unsupported control flow: if |
| TinyFive | PASS | 13 | True | null |

## 性能指标

| 指标 | 当前值 | 基线 | 变化率(%) | 是否退化 |
|---|---:|---:|---:|---|
| 静态汇编指令数 | 29 | 29 | 0.0 | False |
| 编码后机器指令数 | 29 | 29 | 0.0 | False |
| 代码大小(bytes) | 116 | 116 | 0.0 | False |
| TinyFive 动态指令数 | 20 | 20 | 0.0 | False |
| 动态 load | 4 | 4 | 0.0 | False |
| 动态 store | 9 | 9 | 0.0 | False |
| 动态 mul | 0 | 0 | 0.0 | False |
| 动态 add | 5 | 5 | 0.0 | False |
| 动态 madd | 0 | 0 | 0.0 | False |
| 动态 branch | 1 | 1 | 0.0 | False |

## 耗时诊断

- 编译耗时(s): 0.102595
- 解释器耗时(s): 0.000060
- TinyFive 模拟耗时(s): 0.162116

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
  addi sp, sp, -32  # create stack frame
.entry:
    addi t3, sp, -4  # alloca 4
    li t4, 0  # const 0
    sw t0, 28(sp)  # spill flag [regalloc:spill]
    sw t1, 24(sp)  # spill a [regalloc:spill]
    sw t2, 20(sp)  # spill b [regalloc:spill]
    sw t3, 16(sp)  # spill v_1 [regalloc:spill]
    sw t4, 12(sp)  # spill v_2 [regalloc:spill]
    bne t0, t4, .if_then1
    j .if_else2
.if_then1:
    lw t0, 24(sp)  # reload a [regalloc:reload]
    lw t1, 20(sp)  # reload b [regalloc:reload]
    add t2, t0, t1
    lw t3, 16(sp)  # reload v_1 [regalloc:reload]
    sw t2, 0(t3)
    lw t2, 0(t3)
    mv a0, t2  # return value
    sw t0, 24(sp)  # spill a [regalloc:spill]
    sw t1, 20(sp)  # spill b [regalloc:spill]
    sw t3, 16(sp)  # spill v_1 [regalloc:spill]
    jalr zero, ra  # ret
.if_else2:
    lw t0, 24(sp)  # reload a [regalloc:reload]
    lw t1, 20(sp)  # reload b [regalloc:reload]
    sub t2, t0, t1
    lw t0, 16(sp)  # reload v_1 [regalloc:reload]
    sw t2, 0(t0)
    lw t1, 0(t0)
    mv a0, t1  # return value
    jalr zero, ra  # ret
```

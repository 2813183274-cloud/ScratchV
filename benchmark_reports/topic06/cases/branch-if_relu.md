# if_relu 测试详情

## 基本信息

- 类别: branch
- DSL: `tests/topic06/cases/branch/if_relu.dsl`
- 描述: if/else branch combined with add and relu.
- 总体状态: PASS

## 后端结果

- 预期输出: 0

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败原因 |
|---|---|---|---|---|
| DSLInterpreter | UNSUPPORTED | null | null | unsupported control flow: if |
| TinyFive | PASS | 0 | True | null |

## 性能指标

| 指标 | 当前值 | 基线 | 变化率(%) | 是否退化 |
|---|---:|---:|---:|---|
| 静态汇编指令数 | 25 | 25 | 0.0 | False |
| 编码后机器指令数 | 28 | 28 | 0.0 | False |
| 代码大小(bytes) | 112 | 112 | 0.0 | False |
| TinyFive 动态指令数 | 22 | 22 | 0.0 | False |
| 动态 load | 4 | 4 | 0.0 | False |
| 动态 store | 7 | 7 | 0.0 | False |
| 动态 mul | 0 | 0 | 0.0 | False |
| 动态 add | 7 | 7 | 0.0 | False |
| 动态 madd | 0 | 0 | 0.0 | False |
| 动态 branch | 2 | 2 | 0.0 | False |

## 耗时诊断

- 编译耗时(s): 0.105136
- 解释器耗时(s): 0.000062
- TinyFive 模拟耗时(s): 0.161975

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
  addi sp, sp, -16  # create stack frame
.entry:
    addi t3, sp, -4  # alloca 4
    addi t4, sp, -8  # alloca 4
    add t5, t0, t1
    sw t5, 0(t4)
    li t0, 0  # const 0
    sw t0, 12(sp)  # spill v_4 [regalloc:spill]
    sw t2, 8(sp)  # spill use_relu [regalloc:spill]
    sw t3, 4(sp)  # spill v_1 [regalloc:spill]
    sw t4, 0(sp)  # spill v_2 [regalloc:spill]
    bne t2, t0, .if_then1
    j .if_else2
.if_then1:
    lw t0, 0(sp)  # reload v_2 [regalloc:reload]
    lw t1, 0(t0)
    max t2, t1, 0
    lw t1, 4(sp)  # reload v_1 [regalloc:reload]
    sw t2, 0(t1)
    lw t2, 0(t1)
    mv a0, t2  # return value
    sw t0, 0(sp)  # spill v_2 [regalloc:spill]
    jalr zero, ra  # ret
.if_else2:
    lw t0, 0(sp)  # reload v_2 [regalloc:reload]
    lw t1, 0(t0)
    mv a0, t1  # return value
    jalr zero, ra  # ret
```

# matmul_2x2 测试详情

## 基本信息

- 类别: tensor
- DSL: `tests/topic06/cases/tensor/matmul_2x2.dsl`
- 描述: Compute a symbolic 2x2 by 2x2 matrix multiplication.
- 总体状态: FAIL

## 后端结果

- 预期输出: [[19, 22], [43, 50]]

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败原因 |
|---|---|---|---|---|
| DSLInterpreter | PASS | [[19, 22], [43, 50]] | True | null |
| TinyFive | UNSUPPORTED | null | null | non-scalar TinyFive input ABI is unavailable: A, B |

## 性能指标

TinyFive 未有效执行，不生成性能指标。

- 原因: non-scalar TinyFive input ABI is unavailable: A, B
- 编译耗时(s): 0.092766
- 解释器耗时(s): 0.137420

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
.entry:
    mul t2, t0, t1  # matmul: a * b
    mv a0, t2  # return value
    jalr zero, ra  # ret
```

# matmul_4x4 测试详情

## 基本信息

- 类别: tensor
- DSL: `tests/topic06/cases/tensor/matmul_4x4.dsl`
- 描述: Compute a symbolic 4x4 by 4x4 matrix multiplication.
- 总体状态: FAIL

## 后端结果

- 预期输出: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败原因 |
|---|---|---|---|---|
| DSLInterpreter | PASS | [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]] | True | null |
| TinyFive | UNSUPPORTED | null | null | non-scalar TinyFive input ABI is unavailable: A, B |

## 性能指标

TinyFive 未有效执行，不生成性能指标。

- 原因: non-scalar TinyFive input ABI is unavailable: A, B
- 编译耗时(s): 0.095735
- 解释器耗时(s): 0.133596

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

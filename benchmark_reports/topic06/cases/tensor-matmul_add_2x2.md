# matmul_add_2x2 测试详情

## 基本信息

- 类别: tensor
- DSL: `tests/topic06/cases/tensor/matmul_add_2x2.dsl`
- 描述: Compute a 2x2 matmul and then add a symbolic bias term.
- 总体状态: FAIL

## 后端结果

- 预期输出: [[20, 23], [44, 51]]

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败原因 |
|---|---|---|---|---|
| DSLInterpreter | PASS | [[20, 23], [44, 51]] | True | null |
| TinyFive | UNSUPPORTED | null | null | non-scalar TinyFive input ABI is unavailable: A, B, bias |

## 性能指标

TinyFive 未有效执行，不生成性能指标。

- 原因: non-scalar TinyFive input ABI is unavailable: A, B, bias
- 编译耗时(s): 0.095464
- 解释器耗时(s): 0.136079

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
.entry:
    mul t3, t0, t1  # matmul: a * b
    add t0, t3, t2
    mv a0, t0  # return value
    jalr zero, ra  # ret
```

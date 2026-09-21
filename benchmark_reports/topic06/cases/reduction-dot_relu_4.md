# dot_relu_4 测试详情

## 基本信息

- 类别: reduction
- DSL: `tests/topic06/cases/reduction/dot_relu_4.dsl`
- 描述: Compute a length-4 dot product and pass it through ReLU.
- 总体状态: FAIL

## 后端结果

- 预期输出: 0

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败原因 |
|---|---|---|---|---|
| DSLInterpreter | PASS | 0.0 | True | null |
| TinyFive | UNSUPPORTED | null | null | non-scalar TinyFive input ABI is unavailable: a, b |

## 性能指标

TinyFive 未有效执行，不生成性能指标。

- 原因: non-scalar TinyFive input ABI is unavailable: a, b
- 编译耗时(s): 0.097558
- 解释器耗时(s): 0.135579

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
.entry:
    mul t2, t0, t1  # dot: a * b
    max t0, t2, 0
    mv a0, t0  # return value
    jalr zero, ra  # ret
```

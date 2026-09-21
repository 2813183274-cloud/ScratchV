# dot_4 测试详情

## 基本信息

- 类别: reduction
- DSL: `tests/topic06/cases/reduction/dot_4.dsl`
- 描述: Compute the dot product of two symbolic vectors of length 4.
- 总体状态: FAIL

## 后端结果

- 预期输出: 70

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败原因 |
|---|---|---|---|---|
| DSLInterpreter | PASS | 70 | True | null |
| TinyFive | UNSUPPORTED | null | null | non-scalar TinyFive input ABI is unavailable: a, b |

## 性能指标

TinyFive 未有效执行，不生成性能指标。

- 原因: non-scalar TinyFive input ABI is unavailable: a, b
- 编译耗时(s): 0.104655
- 解释器耗时(s): 0.137755

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
.entry:
    mul t2, t0, t1  # dot: a * b
    mv a0, t2  # return value
    jalr zero, ra  # ret
```

# relu_only 测试详情

## 基本信息

- 类别: activation
- DSL: `tests/topic06/cases/activation/relu_only.dsl`
- 描述: Apply ReLU directly to a single input value.
- 总体状态: PASS

## 后端结果

- 预期输出: 0

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败原因 |
|---|---|---|---|---|
| DSLInterpreter | PASS | 0.0 | True | null |
| TinyFive | PASS | 0 | True | null |

## 性能指标

| 指标 | 当前值 | 基线 | 变化率(%) | 是否退化 |
|---|---:|---:|---:|---|
| 静态汇编指令数 | 3 | 3 | 0.0 | False |
| 编码后机器指令数 | 6 | 6 | 0.0 | False |
| 代码大小(bytes) | 24 | 24 | 0.0 | False |
| TinyFive 动态指令数 | 5 | 5 | 0.0 | False |
| 动态 load | 0 | 0 | 0.0 | False |
| 动态 store | 0 | 0 | 0.0 | False |
| 动态 mul | 0 | 0 | 0.0 | False |
| 动态 add | 2 | 2 | 0.0 | False |
| 动态 madd | 0 | 0 | 0.0 | False |
| 动态 branch | 1 | 1 | 0.0 | False |

## 耗时诊断

- 编译耗时(s): 0.096901
- 解释器耗时(s): 0.128973
- TinyFive 模拟耗时(s): 0.159899

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
.entry:
    max t1, t0, 0
    mv a0, t1  # return value
    jalr zero, ra  # ret
```

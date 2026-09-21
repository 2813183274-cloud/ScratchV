# add_chain_3 测试详情

## 基本信息

- 类别: elementwise
- DSL: `tests/topic06/cases/elementwise/add_chain_3.dsl`
- 描述: Chain three add operations across four symbolic inputs.
- 总体状态: PASS

## 后端结果

- 预期输出: 14

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败原因 |
|---|---|---|---|---|
| DSLInterpreter | PASS | 14 | True | null |
| TinyFive | PASS | 14 | True | null |

## 性能指标

| 指标 | 当前值 | 基线 | 变化率(%) | 是否退化 |
|---|---:|---:|---:|---|
| 静态汇编指令数 | 5 | 5 | 0.0 | False |
| 编码后机器指令数 | 5 | 5 | 0.0 | False |
| 代码大小(bytes) | 20 | 20 | 0.0 | False |
| TinyFive 动态指令数 | 5 | 5 | 0.0 | False |
| 动态 load | 0 | 0 | 0.0 | False |
| 动态 store | 0 | 0 | 0.0 | False |
| 动态 mul | 0 | 0 | 0.0 | False |
| 动态 add | 4 | 4 | 0.0 | False |
| 动态 madd | 0 | 0 | 0.0 | False |
| 动态 branch | 0 | 0 | 0.0 | False |

## 耗时诊断

- 编译耗时(s): 0.097598
- 解释器耗时(s): 0.124739
- TinyFive 模拟耗时(s): 0.164359

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
.entry:
    add t4, t0, t1
    add t0, t4, t2
    add t1, t0, t3
    mv a0, t1  # return value
    jalr zero, ra  # ret
```

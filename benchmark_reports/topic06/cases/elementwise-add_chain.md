# add_chain 测试详情

## 基本信息

- 类别: elementwise
- DSL: `tests/topic06/cases/elementwise/add_chain.dsl`
- 描述: Add a and b, then add c to the intermediate result.
- 总体状态: PASS

## 后端结果

- 预期输出: 9

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败原因 |
|---|---|---|---|---|
| DSLInterpreter | PASS | 9 | True | null |
| TinyFive | PASS | 9 | True | null |

## 性能指标

| 指标 | 当前值 | 基线 | 变化率(%) | 是否退化 |
|---|---:|---:|---:|---|
| 静态汇编指令数 | 4 | 4 | 0.0 | False |
| 编码后机器指令数 | 4 | 4 | 0.0 | False |
| 代码大小(bytes) | 16 | 16 | 0.0 | False |
| TinyFive 动态指令数 | 4 | 4 | 0.0 | False |
| 动态 load | 0 | 0 | 0.0 | False |
| 动态 store | 0 | 0 | 0.0 | False |
| 动态 mul | 0 | 0 | 0.0 | False |
| 动态 add | 3 | 3 | 0.0 | False |
| 动态 madd | 0 | 0 | 0.0 | False |
| 动态 branch | 0 | 0 | 0.0 | False |

## 耗时诊断

- 编译耗时(s): 0.092210
- 解释器耗时(s): 0.131257
- TinyFive 模拟耗时(s): 0.157711

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
.entry:
    add t3, t0, t1
    add t0, t3, t2
    mv a0, t0  # return value
    jalr zero, ra  # ret
```

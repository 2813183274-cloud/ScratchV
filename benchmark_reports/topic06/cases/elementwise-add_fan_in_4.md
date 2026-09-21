# add_fan_in_4 测试详情

## 基本信息

- 类别: elementwise
- DSL: `tests/topic06/cases/elementwise/add_fan_in_4.dsl`
- 描述: Compute two independent adds and then merge them with a final add.
- 总体状态: PASS

## 后端结果

- 预期输出: 10

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败原因 |
|---|---|---|---|---|
| DSLInterpreter | PASS | 10 | True | null |
| TinyFive | PASS | 10 | True | null |

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

- 编译耗时(s): 0.101332
- 解释器耗时(s): 0.138245
- TinyFive 模拟耗时(s): 0.164181

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
.entry:
    add t4, t0, t1
    add t0, t2, t3
    add t1, t4, t0
    mv a0, t1  # return value
    jalr zero, ra  # ret
```

# add_reuse 测试详情

## 基本信息

- 类别: elementwise
- DSL: `tests/topic06/cases/elementwise/add_reuse.dsl`
- 描述: Reuse the same intermediate add result on both operands of a second add.
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

- 编译耗时(s): 0.103832
- 解释器耗时(s): 0.132426
- TinyFive 模拟耗时(s): 0.163270

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
.entry:
    add t2, t0, t1
    add t0, t2, t2
    mv a0, t0  # return value
    jalr zero, ra  # ret
```

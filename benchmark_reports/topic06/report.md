# ScratchV DSL 编译器性能测试报告

## 测试概览

- 用例类别筛选: null
- 用例名称筛选: null
- 生成时间: 2026-09-21 16:51:49
- 用例总数: 23
- 通过数量: 15
- 失败数量: 8
- 通过率: 65.2%
- 测试目录: `tests/topic06/cases`
- 汇编输出目录: `build/topic06`
- 性能基线文件: `benchmarks/topic06/baseline.json`
- 性能退化阈值: 5.00%
- 单次编译超时: 30s
- 单次模拟超时: 5s

## 测试结果

| 用例 | 类别 | 解释器状态 | TinyFive 状态 | 失败类型 | TinyFive 动态指令数 | 基线 | 变化率(%) | 是否退化 | 预期输出 | 解释器输出 | TinyFive 输出 |
|---|---|---|---|---|---:|---:|---:|---|---|---|---|
| add_relu_relu | activation | PASS | PASS | null | 7 | 7.00 | 0.00 | False | 7 | 7.0 | 7 |
| relu_add | activation | PASS | PASS | null | 5 | 5.00 | 0.00 | False | 3 | 3.0 | 3 |
| relu_only | activation | PASS | PASS | null | 5 | 5.00 | 0.00 | False | 0 | 0.0 | 0 |
| relu_twice | activation | PASS | PASS | null | 6 | 6.00 | 0.00 | False | 4 | 4.0 | 4 |
| if_else | branch | UNSUPPORTED | PASS | null | 18 | 18.00 | 0.00 | False | 5 | null | 5 |
| if_relu | branch | UNSUPPORTED | PASS | null | 22 | 22.00 | 0.00 | False | 0 | null | 0 |
| if_then | branch | UNSUPPORTED | PASS | null | 20 | 20.00 | 0.00 | False | 13 | null | 13 |
| add_chain | elementwise | PASS | PASS | null | 4 | 4.00 | 0.00 | False | 9 | 9 | 9 |
| add_chain_3 | elementwise | PASS | PASS | null | 5 | 5.00 | 0.00 | False | 14 | 14 | 14 |
| add_fan_in_4 | elementwise | PASS | PASS | null | 5 | 5.00 | 0.00 | False | 10 | 10 | 10 |
| add_reuse | elementwise | PASS | PASS | null | 4 | 4.00 | 0.00 | False | 10 | 10 | 10 |
| vector_add | elementwise | PASS | PASS | null | 3 | 3.00 | 0.00 | False | 5 | 5 | 5 |
| loop_add_4 | loop | UNSUPPORTED | PASS | null | 44 | 44.00 | 0.00 | False | 5 | null | 5 |
| loop_add_chain_4 | loop | UNSUPPORTED | PASS | null | 61 | 61.00 | 0.00 | False | 9 | null | 9 |
| loop_relu_add_4 | loop | UNSUPPORTED | PASS | null | 60 | 60.00 | 0.00 | False | 2 | null | 2 |
| dot_4 | reduction | PASS | UNSUPPORTED | input_abi_unsupported | null | null | null | null | 70 | 70 | null |
| dot_8 | reduction | PASS | UNSUPPORTED | input_abi_unsupported | null | null | null | null | 36 | 36 | null |
| dot_relu_4 | reduction | PASS | UNSUPPORTED | input_abi_unsupported | null | null | null | null | 0 | 0.0 | null |
| dot_relu_8 | reduction | PASS | UNSUPPORTED | input_abi_unsupported | null | null | null | null | 8 | 8.0 | null |
| matmul_2x2 | tensor | PASS | UNSUPPORTED | input_abi_unsupported | null | null | null | null | [[19, 22], [43, 50]] | [[19, 22], [43, 50]] | null |
| matmul_4x4 | tensor | PASS | UNSUPPORTED | input_abi_unsupported | null | null | null | null | [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]] | [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]] | null |
| matmul_add_2x2 | tensor | PASS | UNSUPPORTED | input_abi_unsupported | null | null | null | null | [[20, 23], [44, 51]] | [[20, 23], [44, 51]] | null |
| matmul_relu_2x2 | tensor | PASS | UNSUPPORTED | input_abi_unsupported | null | null | null | null | [[0, 2], [0, 4]] | [[0.0, 2.0], [0.0, 4.0]] | null |

## 性能图表

![课程版指令数图表](course_report_instructions.png)


## 单用例报告

每个用例的后端结果、性能指标、耗时诊断和生成汇编见 [`cases/`](cases/) 目录。

# matmul_add_2x2 测试详情

## 基本信息

- 类别: tensor
- DSL: `tests/topic06/cases/tensor/matmul_add_2x2.dsl`
- 描述: Compute a 2x2 matmul and then add a symbolic bias term.
- 总体状态: FAIL
- 验证模式: both

## 后端能力矩阵

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败类型 | 错误 |
|---|---|---|---|---|---|
| DSLInterpreter | PASS | [[20, 23], [44, 51]] | True | null | null |
| TinyFive | UNSUPPORTED | 0 | False | input_abi_unsupported | null |

- 期望输出: [[20, 23], [44, 51]]
- 两后端输出一致: null
- TinyFive 输入 ABI 可用: False
- TinyFive 输入 ABI 说明: non-scalar TinyFive input ABI is unavailable: A, B, bias

## 性能指标

- 静态汇编指令数: 4
- 编码后机器指令数: 4
- 代码大小(bytes): 16
- TinyFive 动态执行指令数: 4
- TinyFive 分类计数: {'total': 4, 'load': 0, 'store': 0, 'mul': 1, 'add': 2, 'madd': 0, 'branch': 0}
- 编译耗时(s): 0.084293
- 解释器耗时(s): 0.121554
- TinyFive 模拟耗时(s): 0.157928
- 总耗时(s): 0.364772
- 基线动态指令数: null
- 动态指令变化率(%): null
- 是否退化: null

- Cost model 指标: {'static_asm_instructions': 4, 'machine_instructions': 4, 'code_size_bytes': 16, 'dynamic_instructions': 4, 'dynamic_load': 0, 'dynamic_store': 0, 'dynamic_mul': 1, 'dynamic_add': 2, 'dynamic_madd': 0, 'dynamic_branch': 0}
- Cost model 对比: {}
- Cost model 是否退化: null

## 编译信息

- 命令: `'D:\anaconda3\python.exe' -m scratchv.main 'D:\PycharmProjects\ScratchV\ScratchV\tests\topic06\cases\tensor\matmul_add_2x2.dsl' -o 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\matmul_add_2x2.s' --optimize all --emit-register-map 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\matmul_add_2x2.registers.json'`
- 返回码: 0
- 编译错误: null
- 失败日志: null
- 寄存器映射: `build/topic06/matmul_add_2x2.registers.json`
- 汇编文件: `build/topic06/matmul_add_2x2.s`

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
.entry:
    mul t2, t0, t1  # matmul: a * b
    add t4, t2, t3
    mv a0, t4  # return value
    jalr zero, ra  # ret
```

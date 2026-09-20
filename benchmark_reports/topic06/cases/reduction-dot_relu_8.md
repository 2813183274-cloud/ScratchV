# dot_relu_8 测试详情

## 基本信息

- 类别: reduction
- DSL: `tests/topic06/cases/reduction/dot_relu_8.dsl`
- 描述: Compute a length-8 dot product and pass it through ReLU.
- 总体状态: FAIL
- 验证模式: both

## 后端能力矩阵

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败类型 | 错误 |
|---|---|---|---|---|---|
| DSLInterpreter | PASS | 8.0 | True | null | null |
| TinyFive | UNSUPPORTED | 0 | False | input_abi_unsupported | null |

- 期望输出: 8
- 两后端输出一致: null
- TinyFive 输入 ABI 可用: False
- TinyFive 输入 ABI 说明: non-scalar TinyFive input ABI is unavailable: a, b

## 性能指标

- 静态汇编指令数: 4
- 编码后机器指令数: 7
- 代码大小(bytes): 28
- TinyFive 动态执行指令数: 5
- TinyFive 分类计数: {'total': 5, 'load': 0, 'store': 0, 'mul': 1, 'add': 2, 'madd': 0, 'branch': 1}
- 编译耗时(s): 0.092350
- 解释器耗时(s): 0.131473
- TinyFive 模拟耗时(s): 0.158085
- 总耗时(s): 0.383007
- 基线动态指令数: null
- 动态指令变化率(%): null
- 是否退化: null

- Cost model 指标: {'static_asm_instructions': 4, 'machine_instructions': 7, 'code_size_bytes': 28, 'dynamic_instructions': 5, 'dynamic_load': 0, 'dynamic_store': 0, 'dynamic_mul': 1, 'dynamic_add': 2, 'dynamic_madd': 0, 'dynamic_branch': 1}
- Cost model 对比: {}
- Cost model 是否退化: null

## 编译信息

- 命令: `'D:\anaconda3\python.exe' -m scratchv.main 'D:\PycharmProjects\ScratchV\ScratchV\tests\topic06\cases\reduction\dot_relu_8.dsl' -o 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\dot_relu_8.s' --optimize all --emit-register-map 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\dot_relu_8.registers.json'`
- 返回码: 0
- 编译错误: null
- 失败日志: null
- 寄存器映射: `build/topic06/dot_relu_8.registers.json`
- 汇编文件: `build/topic06/dot_relu_8.s`

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

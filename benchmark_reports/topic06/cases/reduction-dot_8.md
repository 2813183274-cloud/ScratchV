# dot_8 测试详情

## 基本信息

- 类别: reduction
- DSL: `tests/topic06/cases/reduction/dot_8.dsl`
- 描述: Compute the dot product of two symbolic vectors of length 8.
- 总体状态: FAIL
- 验证模式: both

## 后端能力矩阵

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败类型 | 错误 |
|---|---|---|---|---|---|
| DSLInterpreter | PASS | 36 | True | null | null |
| TinyFive | UNSUPPORTED | 0 | False | input_abi_unsupported | null |

- 期望输出: 36
- 两后端输出一致: null
- TinyFive 输入 ABI 可用: False
- TinyFive 输入 ABI 说明: non-scalar TinyFive input ABI is unavailable: a, b

## 性能指标

- 静态汇编指令数: 3
- 编码后机器指令数: 3
- 代码大小(bytes): 12
- TinyFive 动态执行指令数: 3
- TinyFive 分类计数: {'total': 3, 'load': 0, 'store': 0, 'mul': 1, 'add': 1, 'madd': 0, 'branch': 0}
- 编译耗时(s): 0.083567
- 解释器耗时(s): 0.123846
- TinyFive 模拟耗时(s): 0.150275
- 总耗时(s): 0.358555
- 基线动态指令数: null
- 动态指令变化率(%): null
- 是否退化: null

- Cost model 指标: {'static_asm_instructions': 3, 'machine_instructions': 3, 'code_size_bytes': 12, 'dynamic_instructions': 3, 'dynamic_load': 0, 'dynamic_store': 0, 'dynamic_mul': 1, 'dynamic_add': 1, 'dynamic_madd': 0, 'dynamic_branch': 0}
- Cost model 对比: {}
- Cost model 是否退化: null

## 编译信息

- 命令: `'D:\anaconda3\python.exe' -m scratchv.main 'D:\PycharmProjects\ScratchV\ScratchV\tests\topic06\cases\reduction\dot_8.dsl' -o 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\dot_8.s' --optimize all --emit-register-map 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\dot_8.registers.json'`
- 返回码: 0
- 编译错误: null
- 失败日志: null
- 寄存器映射: `build/topic06/dot_8.registers.json`
- 汇编文件: `build/topic06/dot_8.s`

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

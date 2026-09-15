# if_then 测试详情

## 基本信息

- 类别: branch
- DSL: `tests/topic06/cases/branch/if_then.dsl`
- 描述: if/else branch returns add result when flag is non-zero.
- 总体状态: FAIL
- 验证模式: both

## 后端能力矩阵

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败类型 | 错误 |
|---|---|---|---|---|---|
| DSLInterpreter | UNSUPPORTED | None | False | interpreter_control_flow_unsupported | unsupported control flow: if |
| TinyFive | TIMEOUT | None | False | simulation_timeout | simulation timeout after 5s |

- 期望输出: 13
- 两后端输出一致: null
- TinyFive 输入 ABI 可用: True
- TinyFive 输入 ABI 说明: null

## 性能指标

- 静态汇编指令数: 12
- 编码后机器指令数: null
- 代码大小(bytes): null
- TinyFive 动态执行指令数: 0
- TinyFive 分类计数: {}
- 编译耗时(s): 0.089163
- 解释器耗时(s): 0.000071
- TinyFive 模拟耗时(s): 5.015826
- 总耗时(s): 5.106110
- 基线动态指令数: null
- 动态指令变化率(%): null
- 是否退化: null

- Cost model 指标: {'static_asm_instructions': 12, 'machine_instructions': None, 'code_size_bytes': None, 'dynamic_instructions': None, 'dynamic_load': None, 'dynamic_store': None, 'dynamic_mul': None, 'dynamic_add': None, 'dynamic_madd': None, 'dynamic_branch': None}
- Cost model 对比: {}
- Cost model 是否退化: null

## 编译信息

- 命令: `'D:\anaconda3\python.exe' -m scratchv.main 'D:\PycharmProjects\ScratchV\ScratchV\tests\topic06\cases\branch\if_then.dsl' -o 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\if_then.s' --optimize all --emit-register-map 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\if_then.registers.json'`
- 返回码: 0
- 编译错误: null
- 失败日志: null
- 寄存器映射: `build/topic06/if_then.registers.json`
- 汇编文件: `build/topic06/if_then.s`

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
.entry:
    li t0, 0  # const 0
    bnez t1, if_then1
    j if_else2
.if_then1:
    add t4, t2, t3
    mv a0, t4  # return value
    jalr zero, ra  # ret
    j if_end3
.if_else2:
    sub t5, t2, t3
    mv a0, t5  # return value
    jalr zero, ra  # ret
    j if_end3
.if_end3:
    jalr zero, ra  # ret
```

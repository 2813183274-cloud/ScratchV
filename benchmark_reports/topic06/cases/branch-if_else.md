# if_else 测试详情

## 基本信息

- 类别: branch
- DSL: `tests/topic06/cases/branch/if_else.dsl`
- 描述: if/else branch returns subtraction result when flag is zero.
- 总体状态: FAIL
- 验证模式: both

## 后端能力矩阵

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败类型 | 错误 |
|---|---|---|---|---|---|
| DSLInterpreter | UNSUPPORTED | None | False | interpreter_control_flow_unsupported | unsupported control flow: if |
| TinyFive | ERROR | None | False | simulation_error | undefined branch target: if_then1 |

- 期望输出: 5
- 两后端输出一致: null
- TinyFive 输入 ABI 可用: True
- TinyFive 输入 ABI 说明: null

## 性能指标

- 静态汇编指令数: 22
- 编码后机器指令数: null
- 代码大小(bytes): null
- TinyFive 动态执行指令数: 0
- TinyFive 分类计数: {'total': 0, 'load': 0, 'store': 0, 'mul': 0, 'add': 0, 'madd': 0, 'branch': 0}
- 编译耗时(s): 0.099637
- 解释器耗时(s): 0.000065
- TinyFive 模拟耗时(s): 0.171959
- 总耗时(s): 0.282802
- 基线动态指令数: null
- 动态指令变化率(%): null
- 是否退化: null

- Cost model 指标: {'static_asm_instructions': 22, 'machine_instructions': None, 'code_size_bytes': None, 'dynamic_instructions': None, 'dynamic_load': 0, 'dynamic_store': 0, 'dynamic_mul': 0, 'dynamic_add': 0, 'dynamic_madd': 0, 'dynamic_branch': 0}
- Cost model 对比: {}
- Cost model 是否退化: null

## 编译信息

- 命令: `'D:\anaconda3\python.exe' -m scratchv.main 'D:\PycharmProjects\ScratchV\ScratchV\tests\topic06\cases\branch\if_else.dsl' -o 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\if_else.s' --optimize all --emit-register-map 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\if_else.registers.json'`
- 返回码: 0
- 编译错误: null
- 失败日志: null
- 寄存器映射: `build/topic06/if_else.registers.json`
- 汇编文件: `build/topic06/if_else.s`

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
  addi sp, sp, -16  # create stack frame
.entry:
    li t3, 0  # const 0
    sw t0, 12(sp)  # spill flag [regalloc:spill]
    sw t1, 8(sp)  # spill a [regalloc:spill]
    sw t2, 4(sp)  # spill b [regalloc:spill]
    bnez t0, if_then1
    j if_else2
.if_then1:
    lw t0, 8(sp)  # reload a [regalloc:reload]
    lw t1, 4(sp)  # reload b [regalloc:reload]
    add t2, t0, t1
    mv a0, t2  # return value
    sw t0, 8(sp)  # spill a [regalloc:spill]
    sw t1, 4(sp)  # spill b [regalloc:spill]
    jalr zero, ra  # ret
    j if_end3
.if_else2:
    lw t0, 8(sp)  # reload a [regalloc:reload]
    lw t1, 4(sp)  # reload b [regalloc:reload]
    sub t2, t0, t1
    mv a0, t2  # return value
    jalr zero, ra  # ret
    j if_end3
.if_end3:
    jalr zero, ra  # ret
```

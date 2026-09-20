# if_relu 测试详情

## 基本信息

- 类别: branch
- DSL: `tests/topic06/cases/branch/if_relu.dsl`
- 描述: if/else branch combined with add and relu.
- 总体状态: FAIL
- 验证模式: both

## 后端能力矩阵

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败类型 | 错误 |
|---|---|---|---|---|---|
| DSLInterpreter | UNSUPPORTED | None | False | interpreter_control_flow_unsupported | unsupported control flow: if |
| TinyFive | ERROR | None | False | simulation_error | undefined branch target: if_then1 |

- 期望输出: 0
- 两后端输出一致: null
- TinyFive 输入 ABI 可用: True
- TinyFive 输入 ABI 说明: null

## 性能指标

- 静态汇编指令数: 17
- 编码后机器指令数: null
- 代码大小(bytes): null
- TinyFive 动态执行指令数: 0
- TinyFive 分类计数: {'total': 0, 'load': 0, 'store': 0, 'mul': 0, 'add': 0, 'madd': 0, 'branch': 0}
- 编译耗时(s): 0.090661
- 解释器耗时(s): 0.000061
- TinyFive 模拟耗时(s): 0.159972
- 总耗时(s): 0.254441
- 基线动态指令数: null
- 动态指令变化率(%): null
- 是否退化: null

- Cost model 指标: {'static_asm_instructions': 17, 'machine_instructions': None, 'code_size_bytes': None, 'dynamic_instructions': None, 'dynamic_load': 0, 'dynamic_store': 0, 'dynamic_mul': 0, 'dynamic_add': 0, 'dynamic_madd': 0, 'dynamic_branch': 0}
- Cost model 对比: {}
- Cost model 是否退化: null

## 编译信息

- 命令: `'D:\anaconda3\python.exe' -m scratchv.main 'D:\PycharmProjects\ScratchV\ScratchV\tests\topic06\cases\branch\if_relu.dsl' -o 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\if_relu.s' --optimize all --emit-register-map 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\if_relu.registers.json'`
- 返回码: 0
- 编译错误: null
- 失败日志: null
- 寄存器映射: `build/topic06/if_relu.registers.json`
- 汇编文件: `build/topic06/if_relu.s`

## 生成汇编

```asm
.text
.align 2
  .globl main
  .type main, @function
main:
  addi sp, sp, -16  # create stack frame
.entry:
    li t2, 0  # const 0
    sw t0, 12(sp)  # spill use_relu [regalloc:spill]
    sw t1, 8(sp)  # spill v_1 [regalloc:spill]
    bnez t0, if_then1
    j if_else2
.if_then1:
    lw t0, 8(sp)  # reload v_1 [regalloc:reload]
    max t1, t0, 0
    mv a0, t1  # return value
    sw t0, 8(sp)  # spill v_1 [regalloc:spill]
    jalr zero, ra  # ret
    j if_end3
.if_else2:
    lw t0, 8(sp)  # reload v_1 [regalloc:reload]
    mv a0, t0  # return value
    jalr zero, ra  # ret
    j if_end3
.if_end3:
    jalr zero, ra  # ret
```

# add_fan_in_4 测试详情

## 基本信息

- 类别: elementwise
- DSL: `tests/topic06/cases/elementwise/add_fan_in_4.dsl`
- 描述: Compute two independent adds and then merge them with a final add.
- 总体状态: PASS
- 验证模式: both

## 后端能力矩阵

| 后端 | 状态 | 实际输出 | 与期望匹配 | 失败类型 | 错误 |
|---|---|---|---|---|---|
| DSLInterpreter | PASS | 10 | True | null | null |
| TinyFive | PASS | 10 | True | null | null |

- 期望输出: 10
- 两后端输出一致: True
- TinyFive 输入 ABI 可用: True
- TinyFive 输入 ABI 说明: null

## 性能指标

- 静态汇编指令数: 5
- 编码后机器指令数: 5
- 代码大小(bytes): 20
- TinyFive 动态执行指令数: 5
- TinyFive 分类计数: {'total': 5, 'load': 0, 'store': 0, 'mul': 0, 'add': 4, 'madd': 0, 'branch': 0}
- 编译耗时(s): 0.092745
- 解释器耗时(s): 0.129068
- TinyFive 模拟耗时(s): 0.157450
- 总耗时(s): 0.845947
- 基线动态指令数: 5.0
- 动态指令变化率(%): 0.0
- 是否退化: False

- Cost model 指标: {'static_asm_instructions': 5, 'machine_instructions': 5, 'code_size_bytes': 20, 'dynamic_instructions': 5.0, 'dynamic_load': 0.0, 'dynamic_store': 0.0, 'dynamic_mul': 0.0, 'dynamic_add': 4.0, 'dynamic_madd': 0.0, 'dynamic_branch': 0.0}
- Cost model 对比: {'static_asm_instructions': {'current': 5, 'baseline': 5, 'delta': 0, 'delta_pct': 0.0, 'regressed': False}, 'machine_instructions': {'current': 5, 'baseline': 5, 'delta': 0, 'delta_pct': 0.0, 'regressed': False}, 'code_size_bytes': {'current': 20, 'baseline': 20, 'delta': 0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_instructions': {'current': 5.0, 'baseline': 5.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_load': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_store': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_mul': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_add': {'current': 4.0, 'baseline': 4.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_madd': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}, 'dynamic_branch': {'current': 0.0, 'baseline': 0.0, 'delta': 0.0, 'delta_pct': 0.0, 'regressed': False}}
- Cost model 是否退化: False

## 编译信息

- 命令: `'D:\anaconda3\python.exe' -m scratchv.main 'D:\PycharmProjects\ScratchV\ScratchV\tests\topic06\cases\elementwise\add_fan_in_4.dsl' -o 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\add_fan_in_4.s' --optimize all --emit-register-map 'D:\PycharmProjects\ScratchV\ScratchV\build\topic06\add_fan_in_4.registers.json'`
- 返回码: 0
- 编译错误: null
- 失败日志: null
- 寄存器映射: `build/topic06/add_fan_in_4.registers.json`
- 汇编文件: `build/topic06/add_fan_in_4.s`

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

---
课程: Python学习
类型: 工具教程
难度: 必修
tags: [Python, VSCode, 调试, Jupyter]
---

# VS Code运行、调试与Notebook

## 运行 `.py`

- 打开脚本，点击右上角“运行Python文件”。
- 或在终端执行 `python 路径/脚本.py`。
- 结果不同步时，先保存文件并检查终端命令中的路径。

## 调试必须会的五个动作

1. 单击行号左侧设置红色断点。
2. 按 `F5`启动调试。
3. `F10`执行当前行但不进入函数。
4. `F11`进入函数。
5. 在“变量”和“监视”面板查看值、类型和形状。

第一次练习：打开[[python学习/13-VSCode代码/02-函数文件与调试/07_debug_logging.py|调试示例]]，在均值计算行暂停，观察 `values`与`result`。

## 条件断点

右键断点可设置条件，例如：

```python
value < 0
```

处理上万行数据时，条件断点比反复打印更有效。

## 在VS Code使用Notebook

打开 `13-VSCode代码/Notebook/EDA交互练习.ipynb`，右上角选择与`.py`相同的`.venv`内核。Notebook适合逐步探索；最终结论仍要整理成可从头运行的脚本。

## 项目内置配置

- `.vscode/settings.json`：优先选择项目内解释器。
- `.vscode/launch.json`：提供“当前Python文件”和“模拟C题”调试入口。
- `requirements.txt`：记录基础依赖。
- `13-VSCode代码/00-环境检查.py`：检查解释器、库和CUDA。

## 验收

- [ ] 能从终端和右上角按钮各运行一次脚本。
- [ ] 能设置断点、单步进入函数、观察变量。
- [ ] 能选择Notebook内核并执行全部单元格。
- [ ] 能解释“VS Code、Python解释器、虚拟环境、包”四者关系。

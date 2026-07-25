---
课程: Python学习
类型: 环境配置
难度: 必修
tags: [Python, VSCode, venv]
---

# VS Code与venv环境搭建

## 目标

在 `python学习` 项目中使用独立 `.venv`。VS Code负责文件、终端、运行和调试；`.venv`负责隔离Python解释器与第三方库。

## 第一次配置

1. 在VS Code选择“文件 → 打开文件夹”，打开整个 `python学习`。
2. 安装Microsoft发布的 **Python** 和 **Jupyter** 扩展。
3. 打开VS Code终端，确认当前目录末尾是 `python学习`。
4. 依次尝试以下命令之一：

```powershell
py -3.12 -m venv .venv
```

如果 `py`不可用，但Anaconda已安装：

```powershell
C:\ProgramData\anaconda3\python.exe -m venv .venv
```

5. 激活环境：

```powershell
.\.venv\Scripts\Activate.ps1
```

若PowerShell执行策略阻止激活，不必改全局策略，直接使用：

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
```

6. 安装本课程依赖：

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

PyTorch的CUDA版本与驱动有关。先安装基础依赖并完成必修；再阅读[[python学习/00-总导航与学习计划/PyTorch与RTX4060配置说明|PyTorch与RTX 4060配置说明]]。不要在比赛当天升级所有库。

## 在VS Code选择解释器

按 `Ctrl+Shift+P`，运行 `Python: Select Interpreter`，选择：

```text
python学习\.venv\Scripts\python.exe
```

右下角应显示 `.venv`。新建终端后运行：

```powershell
python 13-VSCode代码/00-环境检查.py
```

## 环境验收

- [ ] VS Code打开的是整个 `python学习`文件夹，而非单个文件。
- [ ] 右下角解释器指向项目内 `.venv`。
- [ ] `python --version`能输出版本。
- [ ] 环境检查脚本能列出各库版本。
- [ ] 可以运行一个 `.py`和一个 `.ipynb`。
- [ ] 重启VS Code后仍能选择同一解释器。

## 常见问题

### 终端提示找不到python

不要猜路径。使用 `Ctrl+Shift+P → Python: Select Interpreter`选择解释器，再新建终端。也可以直接执行 `.venv\Scripts\python.exe`。

### pip安装到了错误环境

始终写：

```powershell
python -m pip install 包名
```

并核对：

```powershell
python -c "import sys; print(sys.executable)"
```

### ModuleNotFoundError

先确认报错脚本使用的解释器与安装包时相同。不要因为缺一个包就删除整个环境。

下一步：[[python学习/00-总导航与学习计划/VSCode运行、调试与Notebook|VS Code运行、调试与Notebook]]。

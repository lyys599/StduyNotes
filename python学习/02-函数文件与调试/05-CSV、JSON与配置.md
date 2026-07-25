---
课程: Python学习
类型: 主题笔记
难度: 必修
预计学习时间: 80分钟
掌握状态: 未开始
tags:
  - Python
  - 数学建模
  - 函数文件与调试
---

# CSV、JSON与配置

> [!abstract] 学完本篇，你要能够
- 使用标准库处理小型CSV和JSON
- 把参数从代码中分离
- 理解表格数据与配置数据的区别

## 核心概念

- CSV适合二维表
- JSON适合嵌套配置
- `with`确保文件关闭

## 手敲示例

先预测输出，再逐行输入；运行成功后至少修改三个值。

```python
import json
from pathlib import Path

config = {
    "random_seed": 42,
    "test_size": 0.2,
    "target": "产量",
}
path = Path("config.json")
path.write_text(
    json.dumps(config, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
loaded = json.loads(path.read_text(encoding="utf-8"))
print(loaded["target"], loaded["test_size"])
```

> [!example] 可运行代码
> [[python学习/13-VSCode代码/02-函数文件与调试/05_json_config.py|打开对应 `.py` 文件]]。

## 代码拆解

1. `ensure_ascii=False`保留中文。
2. `indent=2`让配置可读。
3. 加载后按键访问参数。

## 数学建模中的用途

把随机种子、目标列、图像分辨率等放进配置，方便团队统一修改。

## 常见报错与易错点

- 用JSON保存NumPy对象会失败，需转成Python类型。
- 把密码或隐私数据写入仓库。
- CSV编码和分隔符判断错误。

## 独立练习

建立包含数据路径、目标列、缺失阈值和随机种子的配置文件，并编写读取函数。

完成后去本模块的练习题笔记做“基础模仿题”；不要提前打开参考答案。

## 验收清单

- [ ] 不看示例，从空白文件写出同类程序。
- [ ] 能解释示例中每个变量的类型、形状或业务含义。
- [ ] 主动制造一次错误，并能根据报错定位问题。
- [ ] 修改输入数据后，能判断输出是否合理。
- [ ] 能用两三句话向队友解释这段代码解决了什么问题。

## 理论关联

- 本主题暂无前置理论链接。

## 下一步

返回 [[python学习/00-总导航与学习计划/Python数学建模学习总导航|Python数学建模学习总导航]]，按推荐顺序继续。

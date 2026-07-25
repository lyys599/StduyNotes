from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from textwrap import dedent
import json

import numpy as np
import pandas as pd


VAULT = Path(r"E:\LXZ\Documents\obsidian笔记！\StudyNote")
ROOT = VAULT / "python学习"


@dataclass(frozen=True)
class Topic:
    folder: str
    filename: str
    title: str
    level: str
    minutes: int
    goals: tuple[str, ...]
    concepts: tuple[str, ...]
    example: str
    explanation: tuple[str, ...]
    application: str
    pitfalls: tuple[str, ...]
    exercise: str
    theory_links: tuple[str, ...] = ()
    c_compare: str = ""
    code_file: str = ""


def write(relative: str, content: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def bullets(items: tuple[str, ...] | list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def render_topic(topic: Topic) -> str:
    links = "\n".join(f"- {link}" for link in topic.theory_links) or "- 本主题暂无前置理论链接。"
    code_link = (
        f"\n> [!example] 可运行代码\n> [[python学习/13-VSCode代码/{topic.code_file}|打开对应 `.py` 文件]]。"
        if topic.code_file
        else ""
    )
    c_section = (
        f"\n## 与 C 语言对照\n\n{topic.c_compare}\n"
        if topic.c_compare
        else ""
    )
    explain = "\n".join(f"{i + 1}. {item}" for i, item in enumerate(topic.explanation))
    return f"""---
课程: Python学习
类型: 主题笔记
难度: {topic.level}
预计学习时间: {topic.minutes}分钟
掌握状态: 未开始
tags:
  - Python
  - 数学建模
  - {topic.folder.split('-', 1)[-1]}
---

# {topic.title}

> [!abstract] 学完本篇，你要能够
{bullets(topic.goals)}

## 核心概念

{bullets(topic.concepts)}
{c_section}
## 手敲示例

先预测输出，再逐行输入；运行成功后至少修改三个值。

```python
{dedent(topic.example).strip()}
```
{code_link}

## 代码拆解

{explain}

## 数学建模中的用途

{topic.application}

## 常见报错与易错点

{bullets(topic.pitfalls)}

## 独立练习

{topic.exercise}

完成后去本模块的练习题笔记做“基础模仿题”；不要提前打开参考答案。

## 验收清单

- [ ] 不看示例，从空白文件写出同类程序。
- [ ] 能解释示例中每个变量的类型、形状或业务含义。
- [ ] 主动制造一次错误，并能根据报错定位问题。
- [ ] 修改输入数据后，能判断输出是否合理。
- [ ] 能用两三句话向队友解释这段代码解决了什么问题。

## 理论关联

{links}

## 下一步

返回 [[python学习/00-总导航与学习计划/Python数学建模学习总导航|Python数学建模学习总导航]]，按推荐顺序继续。
"""


TOPICS: list[Topic] = [
    Topic(
        "01-Python基础", "01-程序运行、输出与注释.md", "程序运行、输出与注释", "必修", 55,
        ("在 VS Code 中运行 `.py` 文件", "使用 `print()`输出文本和计算结果", "用注释记录目的而非复述代码"),
        ("程序按从上到下的顺序执行", "`print()`可以接收多个对象", "`#`后的内容不会执行"),
        """
        # 第一个数学建模程序
        team = "建模一队"
        days = 3
        print("队伍：", team)
        print(f"比赛时长：{days * 24} 小时")
        """,
        ("字符串要放在引号中。", "f-string用花括号把变量或表达式嵌入文本。", "先保存文件，再确认终端没有旧程序残留。"),
        "比赛代码必须能清楚输出阶段名称、样本量、指标和保存位置，方便队友核对。",
        ("使用中文弯引号会触发 `SyntaxError`。", "只在交互窗口试代码而没有保存脚本，比赛时难以复现。"),
        "新建 `hello_modeling.py`，输出队名、比赛日期、你负责的角色以及每天学习时长。",
        c_compare="C 的 `printf`需要格式占位符；Python 的 `print`和 f-string 更直接，但变量类型仍要保持合理。",
        code_file="01-Python基础/01_hello_modeling.py",
    ),
    Topic(
        "01-Python基础", "02-变量、数据类型与运算.md", "变量、数据类型与运算", "必修", 75,
        ("区分整数、浮点数、字符串和布尔值", "正确进行算术、比较和逻辑运算", "使用 `type()`检查变量类型"),
        ("Python变量是对象的名字，不需要提前声明类型", "`/`总得到浮点数，`//`是整除，`**`是乘方", "`and/or/not`组合条件"),
        """
        sample_count = 120
        missing_count = 7
        missing_rate = missing_count / sample_count
        qualified = missing_rate < 0.1
        print(type(sample_count), type(missing_rate))
        print(f"缺失率：{missing_rate:.2%}")
        print("是否达到数据质量要求：", qualified)
        """,
        ("整数相除会得到浮点数，适合计算比例。", "`:.2%`把小数按百分比显示并保留两位。", "比较表达式得到布尔值，可直接用于条件判断。"),
        "样本量、比例、误差和阈值判断贯穿数据审计与模型评价。",
        ("把数值写成字符串后不能直接做加法。", "浮点数不宜用 `==`判断理论上的精确相等。"),
        "输入总样本数与异常样本数，输出异常率，并判断是否超过5%的警戒线。",
        c_compare="C 常显式写 `int`、`double`；Python运行时决定类型。Python仍不是“没有类型”，而是动态类型。",
        code_file="01-Python基础/02_data_quality.py",
    ),
    Topic(
        "01-Python基础", "03-字符串与格式化输出.md", "字符串与格式化输出", "必修", 65,
        ("使用索引、切片和常用字符串方法", "拆分与拼接字段", "生成规范的结果描述"),
        ("字符串不可原地修改", "索引从0开始，负索引从末尾开始", "`split`拆分，`join`连接，`strip`去两端空白"),
        """
        raw = "  A区,2026-07-26,PM2.5=43.7  "
        clean = raw.strip()
        region, day, value_text = clean.split(",")
        value = float(value_text.split("=")[1])
        report = f"{day} {region} 的PM2.5为 {value:.1f}"
        print(report)
        """,
        ("先 `strip`去掉多余空格。", "第一次 `split`按逗号得到三个字段。", "第二次 `split`取等号右侧，再转成浮点数。"),
        "真实附件中经常出现带单位、空格、编码或复合字段的文本，需要先清洗再转数值。",
        ("切片右端不包含。", "`str.replace`返回新字符串，必须接收结果。", "`float('43.7mg')`会失败。"),
        "解析字符串 `B站点|温度:28.6|正常`，提取站点、温度和状态并生成一句报告。",
        c_compare="C字符串通常是字符数组；Python字符串有丰富方法且会自动管理内存，但仍要注意索引越界。",
        code_file="01-Python基础/03_text_parser.py",
    ),
    Topic(
        "01-Python基础", "04-列表与元组.md", "列表与元组", "必修", 80,
        ("创建、索引、切片和修改列表", "使用排序、追加和聚合函数", "理解元组适合固定记录"),
        ("列表可变，元组不可变", "`append`添加一个元素，`extend`展开多个元素", "`sorted`返回新列表，`list.sort`原地排序"),
        """
        values = [18.2, 20.1, 19.7, 50.0, 21.3]
        normal = [x for x in values if x < 40]
        normal.append(22.0)
        print("前三项：", normal[:3])
        print("均值：", sum(normal) / len(normal))
        station = ("A01", 31.2, 121.5)
        print("站点编号：", station[0])
        """,
        ("列表推导式同时表达遍历和筛选。", "切片产生新列表。", "元组可用于存放不会随意改变的坐标记录。"),
        "小规模中间结果可以先放列表；进入批量数值运算后应转为NumPy数组。",
        ("空列表求均值会除以0。", "`append([1,2])`与`extend([1,2])`结果不同。", "误以为 `sort()`返回排序后的列表。"),
        "给定一组成绩，去掉低于0或高于100的非法值，输出排序结果、中位位置的值和前3名。",
        c_compare="C数组长度通常固定；Python列表可动态扩容并容纳不同类型，但建模数据最好保持类型一致。",
        code_file="01-Python基础/04_score_list.py",
    ),
    Topic(
        "01-Python基础", "05-字典与集合.md", "字典与集合", "必修", 75,
        ("用字典保存键值关系", "安全查询、遍历和更新字典", "用集合去重和做集合运算"),
        ("字典通过键访问值", "`dict.get`可提供默认值", "集合元素唯一且无固定顺序"),
        """
        records = ["A", "B", "A", "C", "B", "A"]
        counts = {}
        for name in records:
            counts[name] = counts.get(name, 0) + 1
        print("频数：", counts)
        print("站点集合：", sorted(set(records)))
        required = {"A", "B", "C", "D"}
        print("缺失站点：", required - set(records))
        """,
        ("`get(name, 0)`避免首次出现时键不存在。", "`set`立即去重。", "集合差找出应有但未出现的类别。"),
        "频数统计、编码映射、参数表和字段检查都经常使用字典与集合。",
        ("直接访问不存在的键会 `KeyError`。", "集合无下标。", "字典键必须可哈希，列表不能作为键。"),
        "统计一组地区名称的频数，并检查目标地区集合中哪些地区没有数据。",
        c_compare="C通常要用结构体、数组或手写映射；Python字典直接提供哈希映射。",
        code_file="01-Python基础/05_frequency.py",
    ),
    Topic(
        "01-Python基础", "06-条件判断.md", "条件判断", "必修", 65,
        ("编写多分支规则", "正确使用比较与逻辑运算", "避免边界条件遗漏"),
        ("`if/elif/else`从上到下匹配，第一个真分支执行", "缩进定义代码块", "链式比较可写成 `0 <= x <= 100`"),
        """
        score = 78
        if not 0 <= score <= 100:
            label = "非法"
        elif score >= 85:
            label = "优秀"
        elif score >= 60:
            label = "合格"
        else:
            label = "不合格"
        print(label)
        """,
        ("先处理非法值，避免它被业务规则接收。", "分支应从严格条件到宽松条件排列。", "`else`承接所有未匹配情况。"),
        "质量分级、异常标记、决策规则和指标正向化都依赖清晰的条件判断。",
        ("用多个互相独立的 `if`导致同一对象被重复分类。", "混淆 `=`和`==`。", "遗漏等号造成边界样本错分。"),
        "根据AQI把数据分成优、良、轻度污染、中度污染、重度污染，并为非法负值单独标记。",
        c_compare="语义与C的 `if/else`相近，但Python不用花括号，缩进必须统一。",
        code_file="01-Python基础/06_aqi_rule.py",
    ),
    Topic(
        "01-Python基础", "07-循环、range与遍历.md", "循环、range与遍历", "必修", 85,
        ("使用 `for`与`while`", "掌握 `range/enumerate/zip`", "使用 `break/continue`控制流程"),
        ("优先直接遍历对象", "`enumerate`同时给序号和值", "`zip`按位置配对多个序列"),
        """
        cities = ["甲市", "乙市", "丙市"]
        values = [72.1, 68.4, 91.0]
        for index, (city, value) in enumerate(zip(cities, values), start=1):
            if value < 0:
                continue
            print(index, city, value)

        total = 0
        for value in values:
            total += value
        print("平均值：", total / len(values))
        """,
        ("`zip`把城市与指标值配对。", "`enumerate(..., start=1)`生成适合报告的序号。", "累计变量要在循环前初始化。"),
        "循环适合批量处理文件、参数组合和情景；大型数值计算优先用向量化。",
        ("修改正在遍历的列表。", "`range(n)`不包含n。", "循环内重复读取大文件造成性能浪费。"),
        "同时遍历产品名、成本和收益，输出利润并找到利润最高的产品。",
        c_compare="Python `for`更像遍历容器，不需要手写 `i++`；需要下标时使用 `enumerate`。",
        code_file="01-Python基础/07_loop_report.py",
    ),
    Topic(
        "01-Python基础", "08-推导式与基础排序.md", "推导式与基础排序", "进阶", 70,
        ("读写列表和字典推导式", "按自定义键排序", "判断何时应改用普通循环"),
        ("推导式适合简单映射与筛选", "`key`指定排序依据", "复杂逻辑不要压成一行"),
        """
        scores = {"甲": 82, "乙": 91, "丙": 76}
        passed = {name: score for name, score in scores.items() if score >= 80}
        ranking = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        print(passed)
        print(ranking)
        """,
        ("字典推导式同时遍历键和值。", "`lambda item: item[1]`表示按分数排序。", "`reverse=True`表示降序。"),
        "适合快速生成特征列表、过滤参数和排序候选方案。",
        ("过度嵌套导致不可读。", "把匿名函数写得过于复杂。", "忘记 `items()`会只遍历键。"),
        "把一组城市及指标值标准化为0—1后组成新字典，并按指标值从高到低输出。",
        code_file="01-Python基础/08_ranking.py",
    ),
    Topic(
        "02-函数文件与调试", "01-函数、参数与返回值.md", "函数、参数与返回值", "必修", 90,
        ("把重复步骤封装成函数", "区分参数、返回值和打印", "使用默认参数与关键字参数"),
        ("函数应完成一个明确任务", "`return`把结果交给调用者", "类型注解帮助阅读但不强制类型"),
        """
        def missing_rate(values: list[object], missing_mark=None) -> float:
            missing = sum(value is missing_mark for value in values)
            return missing / len(values) if values else 0.0

        data = [12.0, None, 18.5, None, 20.0]
        rate = missing_rate(data)
        print(f"缺失率：{rate:.1%}")
        """,
        ("函数名描述动作或结果。", "空列表时返回0，避免除零。", "打印用于展示，返回值用于后续计算。"),
        "比赛代码应把读取、清洗、绘图、建模和保存拆成函数，主流程才容易检查。",
        ("函数只打印不返回，后续得到 `None`。", "使用可变对象作为默认参数。", "一个函数承担太多职责。"),
        "编写 `describe(values)`，返回样本量、均值、最小值和最大值组成的字典，并处理空列表。",
        c_compare="与C函数相似，但Python可返回任意对象，也可通过类型注解表达预期输入输出。",
        code_file="02-函数文件与调试/01_functions.py",
    ),
    Topic(
        "02-函数文件与调试", "02-作用域与可变对象.md", "作用域与可变对象", "进阶", 60,
        ("理解局部变量与全局变量", "识别可变对象带来的副作用", "用返回值替代隐式修改"),
        ("函数内部赋值默认创建局部名字", "列表和字典可被原地修改", "复制分浅拷贝与深拷贝"),
        """
        def add_total(record: dict[str, float]) -> dict[str, float]:
            result = record.copy()
            result["总分"] = result["数学"] + result["英语"]
            return result

        original = {"数学": 90, "英语": 82}
        updated = add_total(original)
        print(original)
        print(updated)
        """,
        ("先复制字典，避免函数悄悄改变原数据。", "新字段只存在于返回结果。", "比赛数据处理要明确是原地修改还是产生新表。"),
        "复杂流水线中，隐式修改会让结果难以复现；尽量让函数输入输出清晰。",
        ("滥用 `global`。", "以为 `b = a`复制了列表。", "在多个函数间共享可变全局状态。"),
        "编写标准化函数：接收列表，返回新列表，保证原列表保持不变。",
        code_file="02-函数文件与调试/02_scope_copy.py",
    ),
    Topic(
        "02-函数文件与调试", "03-模块、包与main入口.md", "模块、包与main入口", "必修", 75,
        ("拆分多个 `.py` 文件", "理解导入与 `__name__`", "设计清晰的主程序入口"),
        ("模块就是可导入的Python文件", "导入时模块顶层代码会执行", "`if __name__ == '__main__'`保护入口"),
        """
        from statistics import mean

        def main() -> None:
            values = [10, 12, 15, 18]
            print("均值：", mean(values))

        if __name__ == "__main__":
            main()
        """,
        ("把流程放进 `main`，减少全局变量。", "作为脚本运行时调用 `main`。", "作为模块导入时不会自动执行主流程。"),
        "模拟C题通常由 `run_all.py`协调各分问脚本，函数放在 `src`目录中。",
        ("文件名与第三方库重名，如 `pandas.py`。", "循环导入。", "依赖当前工作目录的脆弱相对路径。"),
        "建立 `utils.py`与 `main.py`，把均值函数放在前者，在后者导入并运行。",
        c_compare="C用头文件声明、源文件实现；Python模块直接通过 `import`组织。",
        code_file="02-函数文件与调试/03_main_entry.py",
    ),
    Topic(
        "02-函数文件与调试", "04-Pathlib与文本文件.md", "Pathlib与文本文件", "必修", 80,
        ("用 `pathlib`构造跨平台路径", "安全读取与写入UTF-8文本", "基于脚本位置定位项目目录"),
        ("`Path`对象可用 `/`拼接", "`__file__`表示当前脚本", "读写文本时显式指定编码"),
        """
        from pathlib import Path

        project_root = Path(__file__).resolve().parents[2]
        output = project_root / "tmp" / "学习记录.txt"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text("今天完成了文件读写。\\n", encoding="utf-8")
        print(output.read_text(encoding="utf-8"))
        """,
        ("由脚本路径推导项目根目录，不依赖终端位置。", "`mkdir`确保输出目录存在。", "显式UTF-8避免中文乱码。"),
        "国赛附件和结果目录很多，可靠路径管理能避免“在我电脑上能跑”的问题。",
        ("把Windows反斜杠直接写入字符串导致转义。", "假定当前工作目录固定。", "覆盖重要原始数据。"),
        "建立 `outputs`目录，写入带当前阶段说明的文本文件，再读取并核对。",
        code_file="02-函数文件与调试/04_pathlib_text.py",
    ),
    Topic(
        "02-函数文件与调试", "05-CSV、JSON与配置.md", "CSV、JSON与配置", "必修", 80,
        ("使用标准库处理小型CSV和JSON", "把参数从代码中分离", "理解表格数据与配置数据的区别"),
        ("CSV适合二维表", "JSON适合嵌套配置", "`with`确保文件关闭"),
        """
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
        """,
        ("`ensure_ascii=False`保留中文。", "`indent=2`让配置可读。", "加载后按键访问参数。"),
        "把随机种子、目标列、图像分辨率等放进配置，方便团队统一修改。",
        ("用JSON保存NumPy对象会失败，需转成Python类型。", "把密码或隐私数据写入仓库。", "CSV编码和分隔符判断错误。"),
        "建立包含数据路径、目标列、缺失阈值和随机种子的配置文件，并编写读取函数。",
        code_file="02-函数文件与调试/05_json_config.py",
    ),
    Topic(
        "02-函数文件与调试", "06-异常处理与断言.md", "异常处理与断言", "必修", 85,
        ("读懂Traceback", "只捕获能够处理的异常", "用断言检查模型前提"),
        ("异常类型说明失败类别", "`try/except/else/finally`分工不同", "`assert`用于程序内部不变量"),
        """
        def safe_ratio(numerator: float, denominator: float) -> float:
            if denominator == 0:
                raise ValueError("分母不能为0")
            return numerator / denominator

        try:
            print(safe_ratio(7, 0))
        except ValueError as error:
            print("输入检查失败：", error)
        """,
        ("主动抛出含业务含义的异常。", "只捕获 `ValueError`，不隐藏其他程序错误。", "错误信息告诉使用者如何修正。"),
        "数据列缺失、样本为空、求解器失败时应立即停止并给出明确提示。",
        ("使用裸 `except`吞掉所有错误。", "捕获后继续使用无效结果。", "把断言当作用户输入校验。"),
        "写一个均值函数：遇到空序列抛出 `ValueError`，调用处捕获并输出友好信息。",
        c_compare="C常用返回码表示失败；Python通过异常把正常结果和错误路径分开。",
        code_file="02-函数文件与调试/06_exceptions.py",
    ),
    Topic(
        "02-函数文件与调试", "07-VSCode断点调试与日志.md", "VS Code断点调试与日志", "必修", 90,
        ("使用断点、单步执行和变量面板", "区分日志与临时打印", "为长流程保留可追踪记录"),
        ("断点暂停在指定行", "Step Over与Step Into用途不同", "`logging`支持级别和时间戳"),
        """
        import logging

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
        )
        values = [2, 4, 8]
        logging.info("开始处理，样本量=%d", len(values))
        result = sum(values) / len(values)
        logging.info("处理完成，均值=%.3f", result)
        """,
        ("日志模板把计算过程结构化。", "参数化日志避免手工拼接。", "在VS Code中给 `result`行设置断点并观察变量。"),
        "比赛中一键运行可能持续数分钟，日志能说明程序卡在哪一步、使用了哪些参数。",
        ("提交代码前到处残留无意义 `print`。", "日志中不记录输入版本和随机种子。", "只看最后一行报错，不看Traceback起点。"),
        "用VS Code调试本例：设置条件断点，查看调用堆栈，并把日志写入 `outputs/run.log`。",
        code_file="02-函数文件与调试/07_debug_logging.py",
    ),
    Topic(
        "02-函数文件与调试", "08-代码规范与可复现性.md", "代码规范与可复现性", "必修", 70,
        ("写出可由队友阅读的代码", "固定随机种子并记录参数", "区分原始数据、中间数据与结果"),
        ("变量名表达含义和单位", "函数避免隐式依赖", "同一输入应得到同一输出"),
        """
        from dataclasses import dataclass
        import random
        import numpy as np

        @dataclass(frozen=True)
        class Settings:
            random_seed: int = 42
            threshold: float = 0.10

        settings = Settings()
        random.seed(settings.random_seed)
        rng = np.random.default_rng(settings.random_seed)
        print(rng.normal(size=3))
        """,
        ("配置集中保存，避免魔法数字散落。", "同时固定标准库和NumPy随机性。", "`frozen=True`防止运行中误改配置。"),
        "可复现性是竞赛可信度的一部分；论文中的表图必须能由代码重新生成。",
        ("使用 `x1/a/tmp`等无含义名字。", "手工修改中间文件却不记录。", "随机算法不固定种子。"),
        "整理一个旧脚本：拆函数、改变量名、集中参数，并添加 `main()`入口。",
        code_file="02-函数文件与调试/08_reproducibility.py",
    ),
    Topic(
        "03-NumPy数值计算", "01-ndarray、形状与数据类型.md", "ndarray、形状与数据类型", "必修", 90,
        ("创建一维与二维数组", "检查 `shape/ndim/dtype`", "理解数组与列表的差别"),
        ("NumPy数组通常只保存一种数据类型", "`shape`描述各维长度", "二维特征矩阵常记为X，形状是样本数×特征数"),
        """
        import numpy as np

        x = np.array([12, 15, 18, 21], dtype=float)
        X = np.array([[1.2, 3.4], [2.0, 4.1], [3.2, 5.0]])
        print(x.shape, x.ndim, x.dtype)
        print(X.shape)
        print("每列均值：", X.mean(axis=0))
        """,
        ("显式浮点类型便于后续统计。", "`axis=0`沿行压缩，得到每列统计。", "打印形状是建模调试的第一习惯。"),
        "机器学习输入、距离矩阵、评价矩阵和优化变量都以数组为基础。",
        ("把 `(n,)`与 `(n,1)`混为一谈。", "混入字符串导致整个数组变成文本类型。", "不检查形状就矩阵相乘。"),
        "创建4个城市×3个指标的矩阵，输出每个指标的均值和每个城市的总和。",
        theory_links=("[[数学建模国赛/02-探索性分析/描述统计与分布诊断|描述统计与分布诊断]]",),
        code_file="03-NumPy数值计算/01_array_shape.py",
    ),
    Topic(
        "03-NumPy数值计算", "02-索引、切片与布尔筛选.md", "索引、切片与布尔筛选", "必修", 85,
        ("选择数组的行、列和子矩阵", "按条件筛选", "理解视图与副本"),
        ("二维索引写成 `[行, 列]`", "布尔数组可作为筛选条件", "基础切片常返回共享内存的视图"),
        """
        import numpy as np

        X = np.array([[10, 2], [15, 8], [20, 4], [25, 9]])
        print("第一列：", X[:, 0])
        mask = (X[:, 0] >= 15) & (X[:, 1] < 9)
        selected = X[mask]
        print(selected)
        """,
        ("冒号表示该维全部位置。", "多个数组条件要用 `&`或 `|`并各自加括号。", "布尔筛选保留条件为真的行。"),
        "异常值筛选、条件抽样和满足约束的方案提取都需要布尔索引。",
        ("对数组使用Python的 `and/or`。", "忘记条件两侧括号。", "切片视图被修改后原数组也变化。"),
        "筛选出第三个指标为正且第一个指标位于10到30之间的所有行。",
        code_file="03-NumPy数值计算/02_index_filter.py",
    ),
    Topic(
        "03-NumPy数值计算", "03-向量化与广播.md", "向量化与广播", "必修", 100,
        ("用数组表达式替代数值循环", "判断广播是否合理", "完成按列标准化"),
        ("向量化把运算交给底层实现", "广播从末尾维度比较", "长度为列数的一维数组可按列作用于二维矩阵"),
        """
        import numpy as np

        X = np.array([[10, 100], [20, 120], [30, 160]], dtype=float)
        minimum = X.min(axis=0)
        span = X.max(axis=0) - minimum
        X_scaled = (X - minimum) / span
        print(X_scaled)
        """,
        ("最小值和极差都是长度为2的数组。", "二维矩阵减一维数组时按列广播。", "整套标准化没有显式循环。"),
        "归一化、距离计算、指标正向化和模型损失函数都应优先向量化。",
        ("极差为0导致除零。", "广播虽然不报错但作用在错误维度。", "过早追求一行代码而失去可读性。"),
        "实现Z-score标准化，并对标准差为0的列给出安全处理。",
        theory_links=("[[数学建模国赛/01-数据处理/Min-Max归一化|Min-Max归一化]]", "[[数学建模国赛/01-数据处理/Z-score标准化|Z-score标准化]]"),
        code_file="03-NumPy数值计算/03_vectorize_broadcast.py",
    ),
    Topic(
        "03-NumPy数值计算", "04-聚合、随机数与模拟.md", "聚合、随机数与模拟", "必修", 90,
        ("沿指定轴计算统计量", "使用现代随机数生成器", "编写可复现蒙特卡洛模拟"),
        ("常用聚合有 `sum/mean/std/min/max/quantile`", "`default_rng(seed)`创建独立生成器", "重复随机实验用比例估计概率"),
        """
        import numpy as np

        rng = np.random.default_rng(42)
        points = rng.uniform(-1, 1, size=(100_000, 2))
        inside = (points[:, 0] ** 2 + points[:, 1] ** 2) <= 1
        pi_estimate = 4 * inside.mean()
        print(f"圆周率估计：{pi_estimate:.5f}")
        """,
        ("一次生成十万个二维点。", "布尔均值就是落入圆内的比例。", "固定种子后结果可复现。"),
        "蒙特卡洛可估计复杂概率、传播参数不确定性和比较随机策略。",
        ("在循环中反复新建随机生成器。", "把随机种子当作调参手段。", "模拟次数太少却报告很多小数。"),
        "模拟两个骰子之和大于等于10的概率，并用不同模拟次数比较误差。",
        theory_links=("[[数学建模国赛/04-优化决策/蒙特卡洛模拟|蒙特卡洛模拟]]",),
        code_file="03-NumPy数值计算/04_monte_carlo.py",
    ),
    Topic(
        "03-NumPy数值计算", "05-线性代数与矩阵运算.md", "线性代数与矩阵运算", "必修", 95,
        ("区分逐元素乘法与矩阵乘法", "解线性方程组", "计算特征值并判断矩阵形状"),
        ("`*`逐元素，`@`矩阵乘法", "优先 `solve(A,b)`而不是显式求逆", "病态矩阵会放大数值误差"),
        """
        import numpy as np

        A = np.array([[2.0, 1.0], [1.0, 3.0]])
        b = np.array([8.0, 13.0])
        x = np.linalg.solve(A, b)
        print("方程解：", x)
        print("验证：", A @ x)
        eigenvalues = np.linalg.eigvalsh(A)
        print("特征值：", eigenvalues)
        """,
        ("`solve`直接求方程组。", "`A @ x`代回验证。", "对称矩阵使用 `eigvalsh`更稳定。"),
        "最小二乘、PCA、马尔可夫过程和多元统计都依赖线性代数。",
        ("用 `A * x`代替矩阵乘法。", "不检查矩阵奇异或条件数。", "无必要地计算逆矩阵。"),
        "求解三元线性方程组，打印残差范数 `norm(A @ x - b)`并解释是否足够小。",
        theory_links=("[[数学建模国赛/02-探索性分析/PCA主成分分析|PCA主成分分析]]", "[[数学建模国赛/03-统计与预测/线性回归|线性回归]]"),
        code_file="03-NumPy数值计算/05_linear_algebra.py",
    ),
    Topic(
        "04-pandas数据处理", "01-Series、DataFrame与读取数据.md", "Series、DataFrame与读取数据", "必修", 100,
        ("理解行索引、列名和数据类型", "读取CSV与Excel", "用 `head/info/describe`快速审计"),
        ("Series是一维带标签数据", "DataFrame是二维异质表", "读取后先检查形状、列名、类型和样例"),
        """
        from pathlib import Path
        import pandas as pd

        root = Path(__file__).resolve().parents[2]
        path = root / "12-示例数据" / "环境监测数据.csv"
        df = pd.read_csv(path)
        print(df.head())
        print(df.shape)
        print(df.dtypes)
        print(df.describe(include="all"))
        """,
        ("基于项目根目录定位数据。", "`shape`给行列数。", "`include='all'`同时摘要数值与类别列。"),
        "C题第一步通常是附件读取和数据质量审计，不能读完立即建模。",
        ("Excel工作表读错。", "中文编码不一致。", "把编号误读为数值或日期误读为文本。"),
        "分别读取同一份CSV和Excel，比较形状、列名和数据类型是否一致。",
        theory_links=("[[数学建模国赛/01-数据处理/pandas数据读取与质量审计|pandas数据读取与质量审计]]",),
        code_file="04-pandas数据处理/01_read_audit.py",
    ),
    Topic(
        "04-pandas数据处理", "02-选择、筛选、排序与赋值.md", "选择、筛选、排序与赋值", "必修", 100,
        ("使用 `loc/iloc`选择数据", "组合多个筛选条件", "安全创建新列"),
        ("单列用 `df['列']`，多列用列表", "`loc`按标签，`iloc`按位置", "链式赋值可能不生效"),
        """
        import pandas as pd

        df = pd.DataFrame({
            "地区": ["甲", "乙", "丙", "丁"],
            "产量": [80, 120, 95, 140],
            "成本": [50, 90, 70, 100],
        })
        df["利润"] = df["产量"] - df["成本"]
        selected = df.loc[(df["产量"] >= 100) & (df["利润"] > 25)]
        print(selected.sort_values("利润", ascending=False))
        """,
        ("向量化创建利润列。", "每个条件加括号并用 `&`。", "排序默认返回新表。"),
        "筛选有效样本、构造派生指标和排列候选方案是高频操作。",
        ("写 `df[condition]['列'] = ...`触发链式赋值问题。", "对Series使用 `and/or`。", "排序后忘记保存结果。"),
        "筛选温度在合理范围且状态为有效的记录，新增温差列，并按日期和站点排序。",
        code_file="04-pandas数据处理/02_select_assign.py",
    ),
    Topic(
        "04-pandas数据处理", "03-缺失、重复与异常值.md", "缺失、重复与异常值", "必修", 120,
        ("统计缺失率与重复记录", "按业务规则处理非法值", "使用IQR标记异常而非盲目删除"),
        ("缺失处理取决于机制和模型目的", "重复要基于业务主键判断", "异常点可能是真实极端事件"),
        """
        import pandas as pd

        df = pd.DataFrame({"值": [10, 11, None, 12, 80, 12]})
        q1, q3 = df["值"].quantile([0.25, 0.75])
        iqr = q3 - q1
        lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        df["异常"] = ~df["值"].between(lower, upper) & df["值"].notna()
        df["值_填补"] = df["值"].fillna(df["值"].median())
        print(df)
        """,
        ("分位数忽略缺失值。", "`between`判断正常区间，取反后得到异常。", "缺失填补与异常标记保留在新列，便于追溯。"),
        "数据清洗必须保留规则、处理前后样本量和敏感性比较。",
        ("先看全数据再划分训练集会泄漏。", "遇到异常全部删除。", "用0填所有缺失值而不说明。"),
        "对环境监测数据生成每列缺失率、重复数、IQR异常数和清洗日志。",
        theory_links=("[[数学建模国赛/01-数据处理/缺失机制MCAR-MAR-MNAR|缺失机制]]", "[[数学建模国赛/01-数据处理/IQR箱线图异常检测|IQR异常检测]]", "[[数学建模国赛/01-数据处理/简单插补与插值|简单插补与插值]]"),
        code_file="04-pandas数据处理/03_cleaning.py",
    ),
    Topic(
        "04-pandas数据处理", "04-分组聚合与透视表.md", "分组聚合与透视表", "必修", 100,
        ("使用 `groupby`按类别统计", "一次计算多个聚合指标", "构造透视表比较二维分组"),
        ("分组遵循拆分—应用—合并", "`agg`可给多列多函数", "`pivot_table`处理重复组合"),
        """
        import pandas as pd

        df = pd.DataFrame({
            "地区": ["甲", "甲", "乙", "乙"],
            "季度": [1, 2, 1, 2],
            "销量": [30, 45, 28, 50],
        })
        summary = df.groupby("地区", as_index=False).agg(
            平均销量=("销量", "mean"),
            总销量=("销量", "sum"),
            样本量=("销量", "size"),
        )
        table = df.pivot_table(index="地区", columns="季度", values="销量")
        print(summary)
        print(table)
        """,
        ("命名聚合让结果列名可直接用于论文。", "`as_index=False`保留普通列。", "透视表将季度展开成列。"),
        "地区比较、年度汇总、群体差异与数据附件重构都需要分组。",
        ("分组后索引结构没看懂。", "用平均值掩盖样本量差异。", "透视时重复键导致普通 `pivot`报错。"),
        "按地区和月份统计均值、标准差、样本量，并生成地区×月份透视表。",
        code_file="04-pandas数据处理/04_groupby_pivot.py",
    ),
    Topic(
        "04-pandas数据处理", "05-合并、拼接与主键验证.md", "合并、拼接与主键验证", "必修", 110,
        ("选择正确的连接类型", "使用 `validate`检查键关系", "识别合并后行数膨胀"),
        ("`merge`按键横向连接", "`concat`按轴拼接", "一对一、一对多和多对多必须事先明确"),
        """
        import pandas as pd

        city = pd.DataFrame({"城市ID": [1, 2], "城市": ["甲", "乙"]})
        yearly = pd.DataFrame({
            "城市ID": [1, 1, 2, 2],
            "年份": [2025, 2026, 2025, 2026],
            "指标": [10, 12, 8, 11],
        })
        merged = yearly.merge(
            city, on="城市ID", how="left", validate="many_to_one",
            indicator=True,
        )
        print(merged)
        print(merged["_merge"].value_counts())
        """,
        ("年度表对城市表是多对一。", "`validate`在键关系错误时立即报错。", "`indicator`检查是否有未匹配行。"),
        "C题经常有多张附件表，错误连接会悄悄复制样本并扭曲统计结果。",
        ("不检查主键唯一性。", "连接键类型不同。", "默认内连接意外丢掉未匹配样本。"),
        "合并站点信息表与日监测表，验证多对一关系，并列出未匹配站点。",
        theory_links=("[[数学建模国赛/01-数据处理/多表合并与主键验证|多表合并与主键验证]]",),
        code_file="04-pandas数据处理/05_merge_validate.py",
    ),
    Topic(
        "04-pandas数据处理", "06-日期时间与时间序列整理.md", "日期时间与时间序列整理", "必修", 100,
        ("把文本转成日期时间", "提取年月日和周期特征", "重采样并检查时间间隔"),
        ("`to_datetime`解析日期", "时间索引支持 `resample`", "排序和重复时间检查必须先做"),
        """
        import pandas as pd

        df = pd.DataFrame({
            "日期": ["2026-01-01", "2026-01-03", "2026-01-02"],
            "值": [10, 14, 12],
        })
        df["日期"] = pd.to_datetime(df["日期"])
        df = df.sort_values("日期").set_index("日期")
        daily = df.resample("D").mean().interpolate()
        daily["星期"] = daily.index.dayofweek
        print(daily)
        """,
        ("解析后排序并设为时间索引。", "按日重采样暴露缺失日期。", "插值仅适合有序连续量，必须说明假设。"),
        "时间序列预测、季节性分析和逐日环境数据都依赖正确时间索引。",
        ("日期仍是字符串却按字面排序。", "把未来信息用于填补过去。", "忽略时区或不规则采样。"),
        "读取环境数据，检查每天是否连续，生成月份、星期和是否周末三个特征。",
        theory_links=("[[数学建模国赛/03-统计与预测/ARIMA时间序列模型|ARIMA时间序列模型]]",),
        code_file="04-pandas数据处理/06_datetime.py",
    ),
    Topic(
        "04-pandas数据处理", "07-Excel多工作表与结果导出.md", "Excel多工作表与结果导出", "必修", 105,
        ("读取指定或全部工作表", "用上下文管理器写多表Excel", "控制索引、列顺序和浮点格式"),
        ("`sheet_name=None`返回工作表字典", "`ExcelWriter`一次写多个表", "导出前先建立结果数据字典"),
        """
        from pathlib import Path
        import pandas as pd

        output = Path("建模结果.xlsx")
        summary = pd.DataFrame({"模型": ["基准"], "MAE": [2.314]})
        predictions = pd.DataFrame({"真实值": [10, 12], "预测值": [10.5, 11.8]})
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            summary.to_excel(writer, sheet_name="模型汇总", index=False)
            predictions.to_excel(writer, sheet_name="预测明细", index=False)
        print(output.resolve())
        """,
        ("一个Writer管理整个工作簿。", "每张结果表命名清楚。", "不导出无意义的DataFrame索引。"),
        "论文手通常直接使用Excel结果；规范导出能减少复制错误。",
        ("覆盖原始附件。", "工作表名超过31字符。", "数值被保存为字符串。"),
        "把清洗数据、描述统计、异常记录分别写入同一个Excel的三张工作表。",
        code_file="04-pandas数据处理/07_excel_io.py",
    ),
    Topic(
        "05-数据可视化", "01-Matplotlib的Figure与Axes.md", "Matplotlib的Figure与Axes", "必修", 90,
        ("使用面向对象接口绘图", "理解Figure、Axes与Artist", "保存而不是只显示图像"),
        ("Figure是整张画布", "Axes是一个坐标区域", "`fig.savefig`输出可复现图片"),
        """
        from pathlib import Path
        import matplotlib.pyplot as plt

        x = [1, 2, 3, 4]
        y = [2.1, 3.4, 3.0, 4.8]
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, y, marker="o", label="观测值")
        ax.set(xlabel="时间", ylabel="指标", title="指标变化趋势")
        ax.legend()
        fig.tight_layout()
        fig.savefig(Path("trend.png"), dpi=300, bbox_inches="tight")
        plt.close(fig)
        """,
        ("面向对象接口便于多图和精细控制。", "`tight_layout`减少遮挡。", "保存后关闭图，批量绘图时避免内存堆积。"),
        "论文中的每一张图都应由脚本生成并保留数据来源和参数。",
        ("用 `plt.show()`阻塞批处理。", "保存图后忘记关闭。", "坐标轴没有单位。"),
        "画一张带标题、单位、图例和数据点标记的折线图，保存为300 DPI PNG。",
        theory_links=("[[数学建模国赛/02-探索性分析/建模可视化选择指南|建模可视化选择指南]]", "[[数学建模国赛/08-竞赛实战/图表规范与结果叙事|图表规范与结果叙事]]"),
        code_file="05-数据可视化/01_figure_axes.py",
    ),
    Topic(
        "05-数据可视化", "02-折线、散点、柱状与分布图.md", "折线、散点、柱状与分布图", "必修", 110,
        ("根据分析问题选择图形", "画折线、散点、柱状、直方和箱线图", "避免误导性坐标与过度装饰"),
        ("折线表达有序变化", "散点表达两个连续变量关系", "直方和箱线图表达分布"),
        """
        import numpy as np
        import matplotlib.pyplot as plt

        rng = np.random.default_rng(42)
        x = rng.normal(size=100)
        y = 2 * x + rng.normal(scale=0.8, size=100)
        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        axes[0].scatter(x, y, alpha=0.7)
        axes[0].set(xlabel="特征X", ylabel="目标Y", title="关系")
        axes[1].hist(y, bins=12, edgecolor="white")
        axes[1].set(title="目标变量分布")
        fig.tight_layout()
        fig.savefig("distribution.png", dpi=300)
        plt.close(fig)
        """,
        ("两个子图分别回答关系与分布问题。", "透明度减轻点重叠。", "箱数会影响直方图观感，应做合理比较。"),
        "EDA阶段至少查看目标分布、特征关系、类别差异和时间趋势。",
        ("对无序类别使用折线。", "柱状图截断纵轴夸大差异。", "用饼图表达过多类别。"),
        "为环境数据选择三种图形，各写一句“这张图回答什么问题”。",
        code_file="05-数据可视化/02_common_charts.py",
    ),
    Topic(
        "05-数据可视化", "03-子图、中文、样式与标注.md", "子图、中文、样式与标注", "必修", 100,
        ("配置中文字体与负号", "统一论文图样式", "添加参考线、重点标注和子图编号"),
        ("样式服务于可读性", "字体设置应有候选回退", "标注只强调关键结论"),
        """
        import matplotlib.pyplot as plt

        plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
        plt.rcParams["axes.unicode_minus"] = False
        years = [2022, 2023, 2024, 2025]
        values = [62, 68, 74, 71]
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(years, values, color="#4C78A8")
        ax.axhline(70, color="#E45756", linestyle="--", label="目标线")
        ax.annotate("最高", xy=(2024, 74), xytext=(2023.4, 80),
                    arrowprops={"arrowstyle": "->"})
        ax.set_ylabel("综合得分")
        ax.legend()
        fig.tight_layout()
        fig.savefig("styled_chart.png", dpi=300)
        plt.close(fig)
        """,
        ("设置常见中文字体候选。", "参考线展示业务阈值。", "箭头只标注最关键位置。"),
        "规范配色、单位和图注能让结果直接进入论文，减少论文手返工。",
        ("依赖本机唯一字体导致换电脑乱码。", "颜色太多且无含义。", "标注遮挡数据。"),
        "把一张默认图改成论文图：加中文、单位、图例、参考线、子图编号并导出。",
        theory_links=("[[数学建模国赛/08-竞赛实战/图表规范与结果叙事|图表规范与结果叙事]]",),
        code_file="05-数据可视化/03_style_chinese.py",
    ),
    Topic(
        "05-数据可视化", "04-Seaborn与相关性热力图.md", "Seaborn与相关性热力图", "进阶", 85,
        ("使用Seaborn快速展示统计关系", "绘制相关性热力图", "避免把相关性图当因果证据"),
        ("Seaborn建立在Matplotlib之上", "`corr`默认计算数值列相关", "热力图适合变量数量适中时总览"),
        """
        import pandas as pd
        import seaborn as sns
        import matplotlib.pyplot as plt

        df = pd.DataFrame({
            "温度": [20, 22, 25, 27, 30],
            "能耗": [50, 53, 58, 65, 76],
            "湿度": [70, 68, 65, 61, 58],
        })
        corr = df.corr(numeric_only=True)
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.heatmap(corr, annot=True, cmap="RdBu_r", center=0, ax=ax)
        fig.tight_layout()
        fig.savefig("correlation.png", dpi=300)
        plt.close(fig)
        """,
        ("先明确参与相关计算的列。", "中心设为0，颜色区分正负。", "相关矩阵对称，变量太多时应筛选。"),
        "热力图可用于初步发现共线性、变量组和后续特征选择方向。",
        ("类别编码后直接解释Pearson相关。", "只看相关系数不看散点。", "把共同趋势造成的相关解释成因果。"),
        "读取环境数据，画数值列相关热力图，再选择绝对相关最高的一对画散点图。",
        theory_links=("[[数学建模国赛/02-探索性分析/Pearson相关系数|Pearson相关系数]]", "[[数学建模国赛/02-探索性分析/Spearman秩相关系数|Spearman秩相关系数]]"),
        code_file="05-数据可视化/04_seaborn_heatmap.py",
    ),
    Topic(
        "05-数据可视化", "05-自动化EDA报告.md", "自动化EDA报告", "必修", 120,
        ("把数据审计和绘图封装为函数", "批量生成数值列分布图", "输出可交付的摘要表与图片目录"),
        ("自动化减少重复劳动", "仍需人工判断变量语义", "文件名必须安全且可追踪"),
        """
        from pathlib import Path
        import pandas as pd

        def audit_table(df: pd.DataFrame) -> pd.DataFrame:
            return pd.DataFrame({
                "类型": df.dtypes.astype(str),
                "缺失数": df.isna().sum(),
                "缺失率": df.isna().mean(),
                "唯一值数": df.nunique(dropna=False),
            })

        data = pd.DataFrame({"A": [1, 2, None], "B": ["x", "x", "y"]})
        report = audit_table(data)
        Path("outputs").mkdir(exist_ok=True)
        report.to_csv("outputs/数据审计.csv", encoding="utf-8-sig")
        print(report)
        """,
        ("审计表以原列名为索引。", "缺失率是布尔均值。", "UTF-8带BOM方便Excel直接打开中文。"),
        "拿到附件后的前1小时可运行EDA模板，快速向建模手反馈数据结构和明显问题。",
        ("自动图很多却没有问题意识。", "对ID列画分布。", "输出文件覆盖且不记录版本。"),
        "扩展审计函数：加入均值、标准差、最小最大值和IQR异常数，并生成至少三类图。",
        theory_links=("[[数学建模国赛/02-探索性分析/EDA完整工作流|EDA完整工作流]]",),
        code_file="05-数据可视化/05_eda_report.py",
    ),
    Topic(
        "06-SciPy与优化", "01-插值、求根与数值积分.md", "插值、求根与数值积分", "进阶", 105,
        ("使用SciPy完成一维插值", "求非线性方程数值根", "计算定积分并理解误差估计"),
        ("数值方法得到近似解", "插值只在观测范围内通常更可靠", "求解前必须检查函数和区间"),
        """
        import numpy as np
        from scipy.interpolate import interp1d
        from scipy.optimize import root_scalar
        from scipy.integrate import quad

        x = np.array([0, 1, 2, 3], dtype=float)
        y = np.array([0, 1, 4, 9], dtype=float)
        f = interp1d(x, y, kind="linear")
        print("插值：", float(f(1.5)))
        root = root_scalar(lambda z: z**2 - 2, bracket=[1, 2])
        area, error = quad(lambda z: np.exp(-z**2), 0, 1)
        print(root.root, area, error)
        """,
        ("插值函数只描述给定点之间的规则。", "`bracket`区间两端应跨过根。", "积分同时返回估计值和误差。"),
        "缺测补齐、反求阈值时间和累积效应计算中常见，但要说明数值假设。",
        ("高阶插值过拟合。", "在数据范围外盲目外推。", "求根失败却继续使用结果。"),
        "对一组稀疏时间观测比较线性与三次插值，并画图说明差异。",
        theory_links=("[[数学建模国赛/01-数据处理/简单插补与插值|简单插补与插值]]",),
        code_file="06-SciPy与优化/01_numerical_methods.py",
    ),
    Topic(
        "06-SciPy与优化", "02-线性规划.md", "SciPy线性规划实现", "必修", 120,
        ("把最大化问题转换给 `linprog`", "正确填写目标、约束和边界", "检查求解状态与约束松弛"),
        ("SciPy默认最小化", "不等式标准为 `A_ub @ x <= b_ub`", "连续解不适用于不可分决策"),
        """
        import numpy as np
        from scipy.optimize import linprog

        c = np.array([-3.0, -5.0])
        A_ub = np.array([[2, 1], [1, 3]], dtype=float)
        b_ub = np.array([100, 90], dtype=float)
        result = linprog(c, A_ub=A_ub, b_ub=b_ub,
                         bounds=[(0, None), (0, None)], method="highs")
        if not result.success:
            raise RuntimeError(result.message)
        print("方案：", result.x)
        print("最大利润：", -result.fun)
        print("剩余资源：", result.ineqlin.residual)
        """,
        ("最大化利润通过最小化负利润实现。", "成功状态必须检查。", "剩余资源帮助判断紧约束。"),
        "资源分配、配比和连续生产计划可直接使用线性规划。",
        ("目标符号写反。", "约束方向转换错误。", "得到小数人数却直接使用。"),
        "建立三种产品、两种资源的生产计划，输出最优产量、利润和资源利用率。",
        theory_links=("[[数学建模国赛/04-优化决策/线性规划|线性规划]]",),
        code_file="06-SciPy与优化/02_linear_programming.py",
    ),
    Topic(
        "06-SciPy与优化", "03-非线性优化与约束.md", "非线性优化与约束", "必修", 120,
        ("使用 `minimize`求解有界问题", "表达等式与不等式约束", "用多初值检查局部最优"),
        ("非凸问题可能有多个局部解", "初值会影响结果", "缩放差异会影响数值稳定性"),
        """
        import numpy as np
        from scipy.optimize import minimize

        def objective(x):
            return (x[0] - 2) ** 2 + (x[1] - 1) ** 2

        constraints = [{"type": "ineq", "fun": lambda x: x[0] + x[1] - 2}]
        result = minimize(
            objective, x0=np.array([0.5, 1.5]),
            bounds=[(0, 4), (0, 4)],
            constraints=constraints, method="SLSQP",
        )
        if not result.success:
            raise RuntimeError(result.message)
        print(result.x, result.fun)
        """,
        ("目标函数只返回一个标量。", "不等式约束按 `fun(x) >= 0`解释。", "边界单独传入更清楚。"),
        "参数估计、非线性成本、设施选址近似和多目标加权可转为非线性优化。",
        ("只用一个初值。", "变量量纲差数个数量级。", "只报告目标值不检查约束。"),
        "从5组随机初值求解同一非凸目标，比较结果并报告最优可行解。",
        theory_links=("[[数学建模国赛/04-优化决策/梯度下降法|梯度下降法]]",),
        code_file="06-SciPy与优化/03_nonlinear_opt.py",
    ),
    Topic(
        "06-SciPy与优化", "04-曲线拟合与参数估计.md", "曲线拟合与参数估计", "必修", 105,
        ("用 `curve_fit`拟合非线性函数", "读取参数协方差与标准误", "画观测和拟合曲线"),
        ("模型形式来自机制或合理经验", "初值和边界可提高稳定性", "高拟合度不等于能外推"),
        """
        import numpy as np
        from scipy.optimize import curve_fit

        def growth(t, capacity, rate):
            return capacity * (1 - np.exp(-rate * t))

        t = np.arange(1, 9, dtype=float)
        y = np.array([18, 31, 43, 53, 61, 67, 72, 76], dtype=float)
        params, covariance = curve_fit(
            growth, t, y, p0=[90, 0.25], bounds=(0, np.inf)
        )
        standard_errors = np.sqrt(np.diag(covariance))
        print(params, standard_errors)
        """,
        ("拟合函数第一个参数是自变量。", "`p0`提供合理起点。", "协方差对角线开方给参数标准误近似。"),
        "增长曲线、衰减规律和经验关系拟合比高阶多项式更容易解释。",
        ("参数无边界导致无意义负值。", "样本太少拟合参数太多。", "只画平滑曲线不画原始点。"),
        "拟合指数衰减模型，计算残差、RMSE并画拟合图。",
        theory_links=("[[数学建模国赛/03-统计与预测/极大似然估计|极大似然估计]]",),
        code_file="06-SciPy与优化/04_curve_fit.py",
    ),
    Topic(
        "06-SciPy与优化", "05-蒙特卡洛与不确定性传播.md", "蒙特卡洛与不确定性传播", "进阶", 100,
        ("为不确定参数指定分布", "批量传播到模型输出", "报告分位数区间和超限概率"),
        ("输入分布要有依据", "输出区间反映输入不确定性而非所有误差", "模拟应固定种子并检查收敛"),
        """
        import numpy as np

        rng = np.random.default_rng(42)
        demand = rng.normal(1000, 80, size=50_000)
        unit_cost = rng.triangular(8, 10, 13, size=50_000)
        total_cost = np.maximum(demand, 0) * unit_cost
        q = np.quantile(total_cost, [0.025, 0.5, 0.975])
        print("成本2.5%、50%、97.5%分位数：", q)
        print("超过13000概率：", (total_cost > 13000).mean())
        """,
        ("需求截断为非负。", "三角分布表达最小、最可能和最大成本。", "用分位数而非正态假设给区间。"),
        "成本风险、预测区间和方案稳健性可用随机情景评估。",
        ("分布凭空设定。", "忽略变量相关性。", "把蒙特卡洛区间称为严格置信区间。"),
        "给线性规划中的利润和资源上限加入随机扰动，统计原方案的可行概率。",
        theory_links=("[[数学建模国赛/04-优化决策/蒙特卡洛模拟|蒙特卡洛模拟]]", "[[数学建模国赛/07-模型检验/不确定性分析|不确定性分析]]"),
        code_file="06-SciPy与优化/05_uncertainty.py",
    ),
    Topic(
        "07-统计与机器学习", "01-statsmodels线性回归与结果解释.md", "statsmodels线性回归与结果解释", "必修", 130,
        ("拟合含截距的OLS", "读取系数、区间和拟合指标", "区分解释模型与预测模型"),
        ("系数是控制其他变量后的条件关联", "p值依赖模型假设", "稳健标准误不修复遗漏变量和非线性"),
        """
        import numpy as np
        import pandas as pd
        import statsmodels.api as sm

        rng = np.random.default_rng(42)
        x1 = rng.uniform(0, 10, 120)
        x2 = rng.normal(5, 2, 120)
        y = 3 + 2 * x1 - 0.8 * x2 + rng.normal(0, 2, 120)
        X = sm.add_constant(pd.DataFrame({"投入": x1, "规模": x2}))
        model = sm.OLS(y, X).fit(cov_type="HC3")
        print(model.params)
        print(model.conf_int())
        print(model.rsquared_adj)
        """,
        ("显式添加截距列。", "HC3提供异方差稳健标准误。", "调整R方考虑变量数量但不是预测性能。"),
        "解释因素影响时用statsmodels；做泛化预测时还需留出集和交叉验证。",
        ("把相关解释成因果。", "只挑显著变量而不控制选择偏差。", "不检查残差和共线性。"),
        "在环境数据上拟合一个解释型回归，写出一个系数的单位化解释并检查残差图。",
        theory_links=("[[数学建模国赛/03-统计与预测/线性回归|线性回归]]", "[[数学建模国赛/07-模型检验/残差诊断与统计假设|残差诊断]]", "[[数学建模国赛/02-探索性分析/VIF多重共线性检测|VIF]]"),
        code_file="07-统计与机器学习/01_ols.py",
    ),
    Topic(
        "07-统计与机器学习", "02-假设检验的Python实现.md", "假设检验的Python实现", "进阶", 115,
        ("根据问题选择常见检验", "计算统计量、p值和效应量", "避免把不显著当作完全相同"),
        ("先写原假设与备择假设", "p值不是原假设为真的概率", "效应量与区间比单独p值更有信息"),
        """
        import numpy as np
        from scipy import stats

        a = np.array([72, 75, 71, 78, 74, 77], dtype=float)
        b = np.array([68, 70, 72, 69, 71, 70], dtype=float)
        result = stats.ttest_ind(a, b, equal_var=False)
        pooled = np.sqrt((a.var(ddof=1) + b.var(ddof=1)) / 2)
        effect = (a.mean() - b.mean()) / pooled
        print("t与p：", result.statistic, result.pvalue)
        print("标准化效应量：", effect)
        """,
        ("Welch检验不要求两组方差相等。", "效应量衡量差异相对波动大小。", "仍需检查独立性与数据生成过程。"),
        "组间比较、政策前后对比和类别关联分析中常见检验必须与设计匹配。",
        ("先看p值再决定假设。", "对重复测量使用独立样本检验。", "多次检验不校正。"),
        "对两组数据画分布、检查异常值，做合适检验并同时报告均值差与效应量。",
        theory_links=("[[数学建模国赛/03-统计与预测/假设检验选择框架|假设检验选择框架]]", "[[数学建模国赛/03-统计与预测/t检验|t检验]]", "[[数学建模国赛/03-统计与预测/非参数检验|非参数检验]]"),
        code_file="07-统计与机器学习/02_hypothesis_tests.py",
    ),
    Topic(
        "07-统计与机器学习", "03-scikit-learn统一建模流程.md", "scikit-learn统一建模流程", "必修", 130,
        ("完成 `fit/predict/score`流程", "划分训练集与测试集", "固定随机种子并保留基准模型"),
        ("特征X通常二维，目标y通常一维", "训练集用于学习，测试集只做最终评估", "估计器接口在多数模型中一致"),
        """
        from sklearn.datasets import load_diabetes
        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import mean_absolute_error, r2_score
        from sklearn.model_selection import train_test_split

        X, y = load_diabetes(return_X_y=True)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model = LinearRegression()
        model.fit(X_train, y_train)
        prediction = model.predict(X_test)
        print("MAE：", mean_absolute_error(y_test, prediction))
        print("R2：", r2_score(y_test, prediction))
        """,
        ("划分发生在训练前。", "`fit`只看训练数据。", "测试指标衡量未参与训练的数据表现。"),
        "统一接口让你能快速比较线性模型、树模型和支持向量机。",
        ("测试集参与调参。", "随机划分时间序列。", "没有简单基准就直接上复杂模型。"),
        "使用内置数据比较线性回归与决策树，记录训练和测试指标并解释过拟合。",
        theory_links=("[[数学建模国赛/05-机器学习/机器学习建模总流程|机器学习建模总流程]]", "[[数学建模国赛/01-数据处理/数据集划分与交叉验证|数据集划分与交叉验证]]"),
        code_file="07-统计与机器学习/03_sklearn_workflow.py",
    ),
    Topic(
        "07-统计与机器学习", "04-预处理与Pipeline防泄漏.md", "预处理与Pipeline防泄漏", "必修", 140,
        ("组合缺失填补、标准化和模型", "在交叉验证内部拟合预处理", "处理数值与类别特征"),
        ("Pipeline按顺序变换", "ColumnTransformer按列类型处理", "任何从数据估计的步骤都应只在训练折拟合"),
        """
        import pandas as pd
        from sklearn.compose import ColumnTransformer
        from sklearn.impute import SimpleImputer
        from sklearn.linear_model import Ridge
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import OneHotEncoder, StandardScaler

        numeric = ["温度", "湿度"]
        categorical = ["地区"]
        preprocess = ColumnTransformer([
            ("num", make_pipeline(SimpleImputer(strategy="median"),
                                  StandardScaler()), numeric),
            ("cat", make_pipeline(SimpleImputer(strategy="most_frequent"),
                                  OneHotEncoder(handle_unknown="ignore")), categorical),
        ])
        model = make_pipeline(preprocess, Ridge(alpha=1.0))
        print(model)
        """,
        ("数值列填补后标准化。", "类别列填补后独热编码。", "未知类别不会让预测直接失败。"),
        "比赛数据常同时含数值、类别和缺失；Pipeline是稳定复现的核心。",
        ("先用全数据标准化。", "手工分别处理训练测试导致列不一致。", "把目标列放进特征。"),
        "在示例分类数据上建立数值+类别Pipeline，完成划分、训练、预测和评价。",
        theory_links=("[[数学建模国赛/01-数据处理/防止数据泄漏与Pipeline|防止数据泄漏与Pipeline]]", "[[数学建模国赛/01-数据处理/类别编码与特征工程|类别编码与特征工程]]"),
        code_file="07-统计与机器学习/04_pipeline.py",
    ),
    Topic(
        "07-统计与机器学习", "05-回归模型与评价指标.md", "回归模型与评价指标", "必修", 135,
        ("比较线性、岭回归和随机森林", "计算MAE、RMSE与R²", "画预测—真实值和残差图"),
        ("MAE与目标同单位", "RMSE更惩罚大误差", "R²可为负且不代表因果"),
        """
        import numpy as np
        from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

        y_true = np.array([10, 12, 15, 20], dtype=float)
        y_pred = np.array([11, 11, 14, 24], dtype=float)
        mae = mean_absolute_error(y_true, y_pred)
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        r2 = r2_score(y_true, y_pred)
        print(f"MAE={mae:.3f}, RMSE={rmse:.3f}, R2={r2:.3f}")
        """,
        ("同时报告至少两个互补指标。", "大误差使RMSE明显增大。", "指标必须结合目标尺度解释。"),
        "连续值预测需报告泛化误差、基线对比和残差结构。",
        ("用训练集指标当最终性能。", "不同数据集直接比较RMSE。", "只追求R²忽视业务误差。"),
        "比较均值基线、岭回归和随机森林，建立结果表并解释哪个模型更合适。",
        theory_links=("[[数学建模国赛/07-模型检验/回归评价指标|回归评价指标]]", "[[数学建模国赛/03-统计与预测/岭回归|岭回归]]", "[[数学建模国赛/05-机器学习/随机森林|随机森林]]"),
        code_file="07-统计与机器学习/05_regression_metrics.py",
    ),
    Topic(
        "07-统计与机器学习", "06-分类模型与评价指标.md", "分类模型与评价指标", "必修", 135,
        ("训练逻辑回归和树模型", "理解混淆矩阵、精确率、召回率、F1与ROC-AUC", "根据任务选择阈值"),
        ("类别不平衡时准确率可能误导", "概率与类别阈值要分开", "测试集评价保持独立"),
        """
        import numpy as np
        from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

        y_true = np.array([0, 0, 0, 1, 1, 1])
        probability = np.array([0.1, 0.4, 0.2, 0.45, 0.7, 0.9])
        prediction = (probability >= 0.5).astype(int)
        print(confusion_matrix(y_true, prediction))
        print(classification_report(y_true, prediction, zero_division=0))
        print("AUC：", roc_auc_score(y_true, probability))
        """,
        ("阈值把概率转成类别。", "混淆矩阵呈现四类结果。", "AUC使用连续概率而不是预测类别。"),
        "风险预警、是否达标和类别识别必须根据漏报与误报代价选择指标。",
        ("用类别标签算AUC。", "只报准确率。", "在测试集调最佳阈值。"),
        "比较阈值0.3、0.5、0.7下的精确率和召回率，说明哪个符合高风险预警。",
        theory_links=("[[数学建模国赛/07-模型检验/分类评价指标|分类评价指标]]", "[[数学建模国赛/03-统计与预测/Logistic回归|Logistic回归]]"),
        code_file="07-统计与机器学习/06_classification.py",
    ),
    Topic(
        "07-统计与机器学习", "07-聚类与PCA.md", "聚类与PCA", "必修", 145,
        ("标准化后进行K-Means", "用轮廓系数比较聚类数", "使用PCA降维并解释方差贡献"),
        ("距离模型对尺度敏感", "聚类标签本身没有大小意义", "PCA是线性组合而非变量筛选"),
        """
        from sklearn.datasets import load_iris
        from sklearn.cluster import KMeans
        from sklearn.decomposition import PCA
        from sklearn.metrics import silhouette_score
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler

        X, _ = load_iris(return_X_y=True)
        cluster_model = make_pipeline(
            StandardScaler(), KMeans(n_clusters=3, n_init=20, random_state=42)
        )
        labels = cluster_model.fit_predict(X)
        X_scaled = StandardScaler().fit_transform(X)
        print("轮廓系数：", silhouette_score(X_scaled, labels))
        pca = PCA(n_components=2).fit(X_scaled)
        print("累计贡献率：", pca.explained_variance_ratio_.sum())
        """,
        ("聚类Pipeline内部完成标准化。", "轮廓系数在同一标准化空间计算。", "PCA贡献率说明二维保留的信息比例。"),
        "城市分型、对象画像、指标降维和综合评价前的数据结构探索常用。",
        ("未标准化就按欧氏距离聚类。", "看二维图主观命名类别。", "用真实标签选择无监督模型后声称纯无监督。"),
        "比较K=2至6的轮廓系数，选择K并用PCA二维图展示，描述而非过度解释簇。",
        theory_links=("[[数学建模国赛/05-机器学习/K-Means聚类|K-Means聚类]]", "[[数学建模国赛/02-探索性分析/PCA主成分分析|PCA主成分分析]]", "[[数学建模国赛/07-模型检验/聚类评价指标|聚类评价指标]]"),
        code_file="07-统计与机器学习/07_cluster_pca.py",
    ),
    Topic(
        "07-统计与机器学习", "08-交叉验证与超参数搜索.md", "交叉验证与超参数搜索", "必修", 130,
        ("使用K折交叉验证", "在Pipeline上搜索参数", "保留独立测试集并控制搜索规模"),
        ("交叉验证估计训练流程波动", "参数名包含Pipeline步骤前缀", "搜索越多越可能对验证过程过拟合"),
        """
        from sklearn.datasets import load_diabetes
        from sklearn.linear_model import Ridge
        from sklearn.model_selection import GridSearchCV, KFold
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler

        X, y = load_diabetes(return_X_y=True)
        pipeline = make_pipeline(StandardScaler(), Ridge())
        search = GridSearchCV(
            pipeline,
            {"ridge__alpha": [0.01, 0.1, 1, 10, 100]},
            scoring="neg_mean_absolute_error",
            cv=KFold(5, shuffle=True, random_state=42),
        )
        search.fit(X, y)
        print(search.best_params_, -search.best_score_)
        """,
        ("搜索对象是完整Pipeline。", "负MAE转回正数解释。", "随机K折固定种子。"),
        "模型选择必须基于验证而非测试集反复试错。",
        ("预处理放在搜索外。", "时间数据使用随机K折。", "网格巨大却不说明计算成本。"),
        "对岭回归和随机森林分别设计小型参数网格，比较验证均值和标准差。",
        theory_links=("[[数学建模国赛/05-机器学习/超参数搜索与模型选择|超参数搜索与模型选择]]", "[[数学建模国赛/01-数据处理/数据集划分与交叉验证|数据集划分与交叉验证]]"),
        code_file="07-统计与机器学习/08_model_selection.py",
    ),
    Topic(
        "07-统计与机器学习", "09-时间序列预测与回测.md", "时间序列预测与回测", "必修", 150,
        ("按时间顺序划分训练与验证", "建立朴素基线和指数平滑模型", "进行滚动来源回测"),
        ("未来不能参与过去的训练", "季节朴素基线是强基准", "一次切分可能不稳定"),
        """
        import numpy as np
        import pandas as pd
        from statsmodels.tsa.holtwinters import ExponentialSmoothing
        from sklearn.metrics import mean_absolute_error

        rng = np.random.default_rng(42)
        index = pd.date_range("2023-01-01", periods=36, freq="MS")
        values = 100 + np.arange(36) * 1.2 + 8 * np.sin(2 * np.pi * np.arange(36) / 12)
        series = pd.Series(values + rng.normal(0, 2, 36), index=index)
        train, test = series.iloc[:-6], series.iloc[-6:]
        model = ExponentialSmoothing(train, trend="add", seasonal="add",
                                     seasonal_periods=12).fit()
        prediction = model.forecast(len(test))
        print("MAE：", mean_absolute_error(test, prediction))
        """,
        ("数据保持时间顺序。", "训练集至少覆盖足够季节周期。", "预测长度与测试集一致。"),
        "销量、污染、需求和资源变化预测常见，但评估必须模拟真正向未来预测。",
        ("随机打乱时间序列。", "用全序列分解后再切分。", "没有与前值或季节前值基线比较。"),
        "建立前值基线、季节朴素和指数平滑三种模型，用最后6期比较MAE。",
        theory_links=("[[数学建模国赛/03-统计与预测/指数平滑ETS|指数平滑ETS]]", "[[数学建模国赛/03-统计与预测/ARIMA时间序列模型|ARIMA]]", "[[数学建模国赛/03-统计与预测/SARIMA季节时间序列模型|SARIMA]]"),
        code_file="07-统计与机器学习/09_time_series.py",
    ),
    Topic(
        "07-统计与机器学习", "10-模型解释、敏感性与稳健性.md", "模型解释、敏感性与稳健性", "必修", 125,
        ("读取置换特征重要性", "改变关键参数做敏感性分析", "比较不同清洗和随机种子下的结论"),
        ("重要性是模型依赖而非因果效应", "敏感性分析要给合理区间", "稳健结论应在替代设定下保持"),
        """
        from sklearn.datasets import load_diabetes
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.inspection import permutation_importance
        from sklearn.model_selection import train_test_split

        X, y = load_diabetes(return_X_y=True)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=42
        )
        model = RandomForestRegressor(n_estimators=150, random_state=42)
        model.fit(X_train, y_train)
        importance = permutation_importance(
            model, X_test, y_test, n_repeats=10, random_state=42
        )
        print(importance.importances_mean)
        """,
        ("重要性在未见测试数据上计算。", "重复置换估计波动。", "重要性高只表示预测依赖该特征。"),
        "论文结论不能只来自单次模型；至少做参数扰动、替代模型或样本重抽样。",
        ("把树模型内置重要性当因果。", "只展示支持结论的敏感性结果。", "不同模型用了不同数据划分。"),
        "改变随机种子、异常处理和模型参数，形成结论稳定性对照表。",
        theory_links=("[[数学建模国赛/05-机器学习/模型解释与特征重要性|模型解释与特征重要性]]", "[[数学建模国赛/07-模型检验/敏感性分析|敏感性分析]]", "[[数学建模国赛/07-模型检验/稳健性检验|稳健性检验]]"),
        code_file="07-统计与机器学习/10_explain_robust.py",
    ),
    Topic(
        "08-数学建模算法实现", "01-熵权法与TOPSIS.md", "熵权法与TOPSIS实现", "必修", 150,
        ("完成指标正向化和归一化", "计算熵权与TOPSIS贴近度", "输出排名并做权重敏感性"),
        ("成本型指标需正向化", "熵权反映样本差异度", "TOPSIS按正负理想解距离排序"),
        """
        import numpy as np

        X = np.array([[80, 20, 7], [70, 15, 9], [90, 30, 6]], dtype=float)
        X[:, 1] = X[:, 1].max() - X[:, 1]  # 成本型正向化
        Z = X / np.sqrt((X**2).sum(axis=0))
        weight = np.array([0.4, 0.3, 0.3])
        V = Z * weight
        d_pos = np.sqrt(((V - V.max(axis=0)) ** 2).sum(axis=1))
        d_neg = np.sqrt(((V - V.min(axis=0)) ** 2).sum(axis=1))
        score = d_neg / (d_pos + d_neg)
        print(score, np.argsort(-score) + 1)
        """,
        ("第二列按成本型正向化。", "向量归一化消除量纲。", "贴近度越大越接近正理想方案。"),
        "城市评价、方案排序和资源配置前的综合评分是C题高频任务。",
        ("忘记指标方向。", "直接混合不同量纲。", "把客观权重称为绝对客观。"),
        "读取城市指标数据，完成熵权TOPSIS排名，并让每个权重±10%检查前三名是否稳定。",
        theory_links=("[[数学建模国赛/06-评价与赋权/熵权法|熵权法]]", "[[数学建模国赛/06-评价与赋权/TOPSIS综合评价|TOPSIS综合评价]]", "[[数学建模国赛/06-评价与赋权/指标正向化与无量纲化|指标正向化]]"),
        code_file="08-数学建模算法实现/01_entropy_topsis.py",
    ),
    Topic(
        "08-数学建模算法实现", "02-AHP与一致性检验.md", "AHP与一致性检验实现", "进阶", 120,
        ("由判断矩阵计算权重", "计算CI与CR一致性指标", "识别主观判断的不一致"),
        ("判断矩阵应正互反", "最大特征向量归一化为权重", "通常CR小于0.1才认为一致性可接受"),
        """
        import numpy as np

        A = np.array([[1, 3, 5], [1/3, 1, 2], [1/5, 1/2, 1]], dtype=float)
        eigenvalues, eigenvectors = np.linalg.eig(A)
        index = np.argmax(eigenvalues.real)
        weight = np.abs(eigenvectors[:, index].real)
        weight /= weight.sum()
        n = len(A)
        ci = (eigenvalues[index].real - n) / (n - 1)
        ri = {3: 0.58}[n]
        cr = ci / ri
        print(weight, cr)
        """,
        ("取最大实特征值对应向量。", "权重归一化和为1。", "一致性不通过要回到判断矩阵调整。"),
        "AHP适合有明确专家判断结构的问题，应与客观权重和敏感性分析结合。",
        ("判断矩阵不互反。", "一致性失败仍继续排名。", "专家意见没有来源说明。"),
        "构造4指标判断矩阵，编写通用函数检查正互反、计算权重和CR。",
        theory_links=("[[数学建模国赛/06-评价与赋权/层次分析法AHP|层次分析法AHP]]",),
        code_file="08-数学建模算法实现/02_ahp.py",
    ),
    Topic(
        "08-数学建模算法实现", "03-灰色预测GM11.md", "灰色预测GM(1,1)实现", "进阶", 140,
        ("实现累加生成和参数估计", "生成拟合与预测值", "计算后验误差并识别适用范围"),
        ("GM(1,1)适合小样本近指数趋势", "原始序列应为正且规律相对稳定", "滚动检验比只看拟合更重要"),
        """
        import numpy as np

        x0 = np.array([12, 15, 19, 24, 30], dtype=float)
        x1 = np.cumsum(x0)
        z1 = -0.5 * (x1[1:] + x1[:-1])
        B = np.column_stack([z1, np.ones(len(z1))])
        a, b = np.linalg.lstsq(B, x0[1:], rcond=None)[0]
        x1_hat = (x0[0] - b / a) * np.exp(-a * np.arange(len(x0) + 2)) + b / a
        x0_hat = np.r_[x1_hat[0], np.diff(x1_hat)]
        print("参数：", a, b)
        print("拟合与未来：", x0_hat)
        """,
        ("累加生成削弱短期波动。", "背景值建立灰微分方程的离散近似。", "累积预测差分还原原序列。"),
        "当样本很少且趋势单调时可作为基线，不能替代充分的时间序列验证。",
        ("数据非正或强周期仍强行使用。", "只报拟合误差。", "长期外推。"),
        "把最后一个观测留出，使用前面数据预测并计算相对误差，再与线性趋势比较。",
        theory_links=("[[数学建模国赛/03-统计与预测/灰色预测GM11|灰色预测GM11]]",),
        code_file="08-数学建模算法实现/03_gm11.py",
    ),
    Topic(
        "08-数学建模算法实现", "04-模拟退火与启发式优化.md", "模拟退火与启发式优化", "进阶", 145,
        ("实现候选解、邻域与接受准则", "记录最优解而非最后解", "多次独立运行比较稳定性"),
        ("高温阶段允许接受较差解", "降温逐步转向局部搜索", "启发式算法不保证全局最优"),
        """
        import math
        import numpy as np

        rng = np.random.default_rng(42)
        current = rng.uniform(-5, 5)
        best = current
        temperature = 10.0
        objective = lambda x: x**2 + 4 * np.sin(3 * x)
        while temperature > 1e-3:
            candidate = current + rng.normal(0, temperature / 5)
            delta = objective(candidate) - objective(current)
            if delta < 0 or rng.random() < math.exp(-delta / temperature):
                current = candidate
            if objective(current) < objective(best):
                best = current
            temperature *= 0.98
        print(best, objective(best))
        """,
        ("较差解按温度相关概率接受。", "最优解单独保存。", "降温率控制搜索广度与速度。"),
        "复杂组合方案无法直接求精确解时可作为候选，但必须与基线和多次运行比较。",
        ("只运行一次。", "参数凭感觉不做敏感性。", "把启发式结果称为全局最优。"),
        "在同一目标上运行20个随机种子，报告最优、均值、标准差和运行时间。",
        theory_links=("[[数学建模国赛/04-优化决策/模拟退火SA|模拟退火SA]]", "[[数学建模国赛/04-优化决策/遗传算法GA|遗传算法GA]]"),
        code_file="08-数学建模算法实现/04_simulated_annealing.py",
    ),
    Topic(
        "08-数学建模算法实现", "05-最短路径与网络问题.md", "最短路径与网络问题实现", "进阶", 115,
        ("用邻接表表示加权图", "实现Dijkstra", "恢复最短路径并处理不可达节点"),
        ("边权必须非负", "优先队列每次扩展当前最短节点", "前驱字典用于恢复路径"),
        """
        import heapq

        graph = {
            "A": [("B", 2), ("C", 5)],
            "B": [("C", 1), ("D", 4)],
            "C": [("D", 1)],
            "D": [],
        }
        distances = {node: float("inf") for node in graph}
        distances["A"] = 0
        queue = [(0, "A")]
        while queue:
            distance, node = heapq.heappop(queue)
            if distance != distances[node]:
                continue
            for neighbor, weight in graph[node]:
                candidate = distance + weight
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate
                    heapq.heappush(queue, (candidate, neighbor))
        print(distances)
        """,
        ("无穷大表示暂时不可达。", "过期队列项直接跳过。", "松弛操作更新更短距离。"),
        "运输路线、应急调度和网络连通问题常可抽象为图。",
        ("存在负权仍用Dijkstra。", "有向边与无向边混淆。", "只输出距离不恢复具体路径。"),
        "扩展代码保存前驱节点，输出A到D的完整路径和总长度。",
        theory_links=("[[数学建模国赛/04-优化决策/Dijkstra最短路径|Dijkstra最短路径]]",),
        code_file="08-数学建模算法实现/05_dijkstra.py",
    ),
    Topic(
        "08-数学建模算法实现", "06-敏感性、Bootstrap与稳健性.md", "敏感性、Bootstrap与稳健性实现", "必修", 135,
        ("进行单因素与情景敏感性分析", "用Bootstrap估计区间", "输出结论稳定性表"),
        ("敏感性看输入变化如何传到输出", "Bootstrap从观测样本有放回抽样", "稳健性需要替代设定而非重复同一模型"),
        """
        import numpy as np

        rng = np.random.default_rng(42)
        sample = np.array([12, 15, 14, 18, 20, 17, 16], dtype=float)
        bootstrap_means = np.empty(5000)
        for i in range(len(bootstrap_means)):
            resample = rng.choice(sample, size=len(sample), replace=True)
            bootstrap_means[i] = resample.mean()
        interval = np.quantile(bootstrap_means, [0.025, 0.975])
        print("均值：", sample.mean())
        print("Bootstrap 95%区间：", interval)
        """,
        ("每次重抽样与原样本同样大小。", "统计量可替换为中位数、模型系数或排名。", "分位数给经验区间。"),
        "竞赛论文至少应说明结论是否对权重、阈值、抽样和模型选择敏感。",
        ("时间序列随意独立重抽样。", "样本偏差被Bootstrap复制。", "只展示一个参数点。"),
        "对TOPSIS输入进行Bootstrap，统计每个城市成为第一名的概率。",
        theory_links=("[[数学建模国赛/03-统计与预测/Bootstrap重抽样与置信区间|Bootstrap]]", "[[数学建模国赛/07-模型检验/敏感性分析|敏感性分析]]", "[[数学建模国赛/07-模型检验/稳健性检验|稳健性检验]]"),
        code_file="08-数学建模算法实现/06_bootstrap_sensitivity.py",
    ),
    Topic(
        "08-数学建模算法实现", "07-PyTorch张量、设备与自动求导.md", "PyTorch张量、设备与自动求导", "赛时查阅", 130,
        ("创建张量并检查形状", "自动选择CUDA或CPU", "使用自动求导理解训练基础"),
        ("张量类似可在GPU运行的NumPy数组", "模型和数据必须位于同一设备", "`backward`计算梯度"),
        """
        import torch

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        x = torch.tensor([1.0, 2.0, 3.0], device=device, requires_grad=True)
        loss = ((x - 2.0) ** 2).mean()
        loss.backward()
        print("设备：", device)
        print("损失：", loss.item())
        print("梯度：", x.grad.cpu().numpy())
        """,
        ("设备自动选择。", "标量损失调用反向传播。", "转回NumPy前移到CPU并脱离梯度环境。"),
        "只有当传统模型明显不足且样本量足够时再考虑神经网络；它不是默认首选。",
        ("CUDA可用就认为训练一定更快。", "数据和模型设备不同。", "把带梯度张量直接转NumPy。"),
        "在CPU和可用CUDA上分别完成矩阵乘法，核对结果并记录设备名称。",
        code_file="08-数学建模算法实现/07_torch_basics.py",
    ),
    Topic(
        "08-数学建模算法实现", "08-PyTorch全连接网络训练.md", "PyTorch全连接网络训练", "赛时查阅", 180,
        ("使用Dataset和DataLoader", "搭建回归全连接网络", "完成训练、验证、早停与保存"),
        ("训练循环包含前向、损失、清梯度、反向和更新", "标准化只在训练集拟合", "验证损失用于早停"),
        """
        import torch
        from torch import nn

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = nn.Sequential(
            nn.Linear(4, 16), nn.ReLU(),
            nn.Linear(16, 8), nn.ReLU(),
            nn.Linear(8, 1),
        ).to(device)
        optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
        loss_function = nn.MSELoss()
        X = torch.randn(32, 4, device=device)
        y = torch.randn(32, 1, device=device)
        optimizer.zero_grad()
        prediction = model(X)
        loss = loss_function(prediction, y)
        loss.backward()
        optimizer.step()
        print(loss.item())
        """,
        ("输出维度与目标一致。", "每批训练前清空旧梯度。", "优化器根据梯度更新参数。"),
        "基础MLP可做表格回归或分类对比模型；必须与线性和树模型公平比较。",
        ("全数据标准化后才划分。", "训练损失下降就认为泛化良好。", "不固定随机种子或不保存最佳验证模型。"),
        "完成一个回归和一个二分类网络，加入验证集、早停、学习曲线和最佳权重保存。",
        theory_links=("[[数学建模国赛/05-机器学习/机器学习建模总流程|机器学习建模总流程]]", "[[数学建模国赛/07-模型检验/模型对比与消融实验|模型对比与消融实验]]"),
        code_file="08-数学建模算法实现/08_torch_mlp.py",
    ),
]


MODULE_EXERCISES = {
    "01-Python基础": {
        "title": "Python基础三级练习",
        "basic": "输入5个观测值，剔除不在0—100范围的值，输出有效值、均值、最大值和最小值。",
        "independent": "编写一个命令行成绩统计器：循环读取姓名和成绩，输入 `q`结束，输出排名、及格率和缺考名单。",
        "modeling": "读取代码中给定的一组站点记录，统计各站点有效观测数、异常数和异常率，按异常率降序输出。",
        "answer": """
        def clean_values(values):
            valid = [value for value in values if 0 <= value <= 100]
            if not valid:
                raise ValueError("没有有效值")
            return {
                "有效值": valid,
                "均值": sum(valid) / len(valid),
                "最大值": max(valid),
                "最小值": min(valid),
            }

        records = [
            ("A", 20.0), ("A", -1.0), ("B", 31.0),
            ("B", 999.0), ("B", 28.0), ("C", 26.0),
        ]
        summary = {}
        for station, value in records:
            item = summary.setdefault(station, {"总数": 0, "异常数": 0})
            item["总数"] += 1
            if not 0 <= value <= 100:
                item["异常数"] += 1
        for station, item in summary.items():
            item["异常率"] = item["异常数"] / item["总数"]
        ranking = sorted(summary.items(), key=lambda pair: pair[1]["异常率"],
                         reverse=True)
        print(ranking)
        """,
    },
    "02-函数文件与调试": {
        "title": "函数、文件与调试三级练习",
        "basic": "把均值、极差、缺失率分别封装为函数，使用统一的 `describe`函数调用它们。",
        "independent": "编写配置驱动的数据审计程序：从JSON读取输入路径、合法范围和输出路径，错误时给出友好提示。",
        "modeling": "建立 `main.py + utils.py`项目，读取CSV，检查主键重复和字段缺失，保存审计日志及JSON摘要。",
        "answer": """
        import json
        from pathlib import Path
        import pandas as pd

        def audit_csv(input_path: Path, key: str) -> dict:
            df = pd.read_csv(input_path)
            if key not in df.columns:
                raise ValueError(f"缺少主键列：{key}")
            return {
                "行数": len(df),
                "列数": df.shape[1],
                "主键重复数": int(df[key].duplicated().sum()),
                "各列缺失数": df.isna().sum().astype(int).to_dict(),
            }

        def main():
            root = Path(__file__).resolve().parents[2]
            result = audit_csv(root / "12-示例数据" / "环境监测数据.csv", "记录ID")
            output = root / "tmp" / "审计摘要.json"
            output.parent.mkdir(exist_ok=True)
            output.write_text(json.dumps(result, ensure_ascii=False, indent=2),
                              encoding="utf-8")
            print(result)

        if __name__ == "__main__":
            main()
        """,
    },
    "03-NumPy数值计算": {
        "title": "NumPy三级练习",
        "basic": "创建5×4评价矩阵，输出每列均值、标准差和每行总分。",
        "independent": "不使用显式循环实现安全的Min-Max和Z-score标准化，常数列保持为0。",
        "modeling": "用蒙特卡洛估计项目利润为正的概率、平均利润和95%区间，并研究模拟次数对结果的影响。",
        "answer": """
        import numpy as np

        def minmax(X):
            X = np.asarray(X, dtype=float)
            minimum = X.min(axis=0)
            span = X.max(axis=0) - minimum
            safe_span = np.where(span == 0, 1, span)
            return (X - minimum) / safe_span

        def simulate_profit(n=100_000, seed=42):
            rng = np.random.default_rng(seed)
            price = rng.normal(20, 1.5, n)
            demand = np.maximum(rng.normal(1000, 120, n), 0)
            unit_cost = rng.triangular(12, 14, 17, n)
            fixed_cost = 4200
            profit = (price - unit_cost) * demand - fixed_cost
            return {
                "盈利概率": float((profit > 0).mean()),
                "平均利润": float(profit.mean()),
                "95%区间": np.quantile(profit, [0.025, 0.975]).tolist(),
            }

        print(simulate_profit())
        """,
    },
    "04-pandas数据处理": {
        "title": "pandas三级练习",
        "basic": "读取环境监测CSV，输出形状、字段类型、缺失率和数值描述统计。",
        "independent": "按记录ID去重，按站点中位数填补温度，对PM2.5做IQR异常标记，导出清洗表。",
        "modeling": "合并站点信息与监测记录，按地区和月份汇总，写入含清洗数据、异常记录、统计汇总三张表的Excel。",
        "answer": """
        from pathlib import Path
        import pandas as pd

        root = Path(__file__).resolve().parents[2]
        df = pd.read_csv(root / "12-示例数据" / "环境监测数据.csv")
        df["日期"] = pd.to_datetime(df["日期"])
        df = df.drop_duplicates("记录ID").copy()
        df["温度"] = df["温度"].fillna(df.groupby("站点")["温度"].transform("median"))
        q1, q3 = df["PM2.5"].quantile([0.25, 0.75])
        lower, upper = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
        df["PM2.5异常"] = ~df["PM2.5"].between(lower, upper) & df["PM2.5"].notna()
        df["月份"] = df["日期"].dt.to_period("M").astype(str)
        summary = df.groupby(["地区", "月份"], as_index=False).agg(
            平均PM25=("PM2.5", "mean"), 样本量=("记录ID", "size")
        )
        output = root / "tmp" / "pandas练习结果.xlsx"
        output.parent.mkdir(exist_ok=True)
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="清洗数据", index=False)
            df.loc[df["PM2.5异常"]].to_excel(writer, sheet_name="异常记录", index=False)
            summary.to_excel(writer, sheet_name="统计汇总", index=False)
        print(output)
        """,
    },
    "05-数据可视化": {
        "title": "数据可视化三级练习",
        "basic": "为给定数据分别绘制折线、散点和直方图，补齐标题、单位和图例。",
        "independent": "制作2×2 EDA面板：趋势、分布、箱线图和相关热力图，保存300 DPI图片。",
        "modeling": "自动遍历数值列生成分布图，并输出一张可直接放进论文的关键结论图和50字图表解读。",
        "answer": """
        from pathlib import Path
        import matplotlib.pyplot as plt
        import pandas as pd
        import seaborn as sns

        root = Path(__file__).resolve().parents[2]
        df = pd.read_csv(root / "12-示例数据" / "环境监测数据.csv",
                         parse_dates=["日期"])
        output = root / "tmp" / "eda_panel.png"
        output.parent.mkdir(exist_ok=True)
        fig, axes = plt.subplots(2, 2, figsize=(11, 8))
        daily = df.groupby("日期", as_index=False)["PM2.5"].mean()
        axes[0, 0].plot(daily["日期"], daily["PM2.5"])
        axes[0, 0].set(title="日均PM2.5趋势", ylabel="μg/m³")
        axes[0, 1].hist(df["PM2.5"].dropna(), bins=15)
        axes[0, 1].set(title="PM2.5分布")
        sns.boxplot(data=df, x="地区", y="PM2.5", ax=axes[1, 0])
        corr = df.select_dtypes("number").corr()
        sns.heatmap(corr, cmap="RdBu_r", center=0, ax=axes[1, 1])
        fig.tight_layout()
        fig.savefig(output, dpi=300, bbox_inches="tight")
        plt.close(fig)
        print(output)
        """,
    },
    "06-SciPy与优化": {
        "title": "SciPy与优化三级练习",
        "basic": "用插值估算缺失时点，用曲线拟合估计增长参数。",
        "independent": "建立三产品两资源线性规划，输出方案、目标值、剩余资源并验证约束。",
        "modeling": "把需求和价格视为不确定参数，比较确定性最优方案在随机情景中的利润和不可行风险。",
        "answer": """
        import numpy as np
        from scipy.optimize import linprog

        profit = np.array([5, 7, 4], dtype=float)
        resources = np.array([[2, 3, 1], [1, 2, 2]], dtype=float)
        limits = np.array([180, 120], dtype=float)
        result = linprog(
            -profit, A_ub=resources, b_ub=limits,
            bounds=[(0, None)] * 3, method="highs"
        )
        if not result.success:
            raise RuntimeError(result.message)
        print("方案：", result.x)
        print("利润：", -result.fun)
        print("资源消耗：", resources @ result.x)
        print("剩余资源：", limits - resources @ result.x)
        """,
    },
    "07-统计与机器学习": {
        "title": "统计与机器学习三级练习",
        "basic": "划分训练测试集，训练线性回归并报告MAE、RMSE和R²。",
        "independent": "建立含缺失填补、标准化和岭回归的Pipeline，用5折交叉验证搜索alpha。",
        "modeling": "比较基准、线性、随机森林和MLP，使用完全相同的数据切分，输出性能、训练时间和解释性对照表。",
        "answer": """
        import numpy as np
        from sklearn.datasets import load_diabetes
        from sklearn.impute import SimpleImputer
        from sklearn.linear_model import Ridge
        from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
        from sklearn.model_selection import GridSearchCV, train_test_split
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler

        X, y = load_diabetes(return_X_y=True)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        pipeline = make_pipeline(SimpleImputer(), StandardScaler(), Ridge())
        search = GridSearchCV(
            pipeline, {"ridge__alpha": [0.01, 0.1, 1, 10, 100]},
            scoring="neg_mean_absolute_error", cv=5
        )
        search.fit(X_train, y_train)
        prediction = search.predict(X_test)
        print(search.best_params_)
        print("MAE", mean_absolute_error(y_test, prediction))
        print("RMSE", np.sqrt(mean_squared_error(y_test, prediction)))
        print("R2", r2_score(y_test, prediction))
        """,
    },
    "08-数学建模算法实现": {
        "title": "数学建模算法实现三级练习",
        "basic": "对4个方案、4个指标完成成本型正向化和TOPSIS排名。",
        "independent": "把TOPSIS封装成函数，验证输入、返回得分和排名，并进行权重±10%敏感性分析。",
        "modeling": "综合评价结果作为优化优先级，在预算约束下选择项目；再用Bootstrap统计各方案进入前三名的概率。",
        "answer": """
        import numpy as np

        def topsis(X, weights, cost_columns=()):
            X = np.asarray(X, dtype=float).copy()
            weights = np.asarray(weights, dtype=float)
            if X.ndim != 2 or len(weights) != X.shape[1]:
                raise ValueError("矩阵和权重形状不匹配")
            if np.any(weights < 0) or weights.sum() <= 0:
                raise ValueError("权重必须非负且总和大于0")
            for column in cost_columns:
                X[:, column] = X[:, column].max() - X[:, column]
            denominator = np.sqrt((X**2).sum(axis=0))
            denominator[denominator == 0] = 1
            V = X / denominator * (weights / weights.sum())
            d_pos = np.linalg.norm(V - V.max(axis=0), axis=1)
            d_neg = np.linalg.norm(V - V.min(axis=0), axis=1)
            score = d_neg / np.where(d_pos + d_neg == 0, 1, d_pos + d_neg)
            return score, np.argsort(-score)

        X = [[80, 20, 7, 50], [70, 15, 9, 60],
             [90, 30, 6, 55], [82, 18, 8, 58]]
        score, order = topsis(X, [0.3, 0.2, 0.25, 0.25], cost_columns=[1])
        print(score, order + 1)
        """,
    },
}


def render_exercise(folder: str, info: dict[str, str]) -> str:
    return f"""---
课程: Python学习
类型: 练习题
模块: {folder}
答案状态: 独立存放
tags: [Python, 练习, 数学建模]
---

# {info["title"]}

> [!warning] 做题规则
> 先关闭参考答案。从空白 `.py` 文件开始，允许查看主题笔记和官方文档；卡住15分钟后再查提示。每题完成后至少修改一组输入。

## A. 基础模仿题

{info["basic"]}

验收：

- [ ] 能运行且对正常输入正确。
- [ ] 至少检查一种非法或边界输入。
- [ ] 能逐句解释自己的代码。

## B. 独立编程题

{info["independent"]}

验收：

- [ ] 至少拆成两个函数。
- [ ] 使用清晰的英文变量名与中文输出。
- [ ] 保存一份可核对的结果。

## C. 数学建模应用题

{info["modeling"]}

验收：

- [ ] 写清输入、方法、参数和输出。
- [ ] 提供一个基准或人工核对结果。
- [ ] 写出至少两个局限或风险。

## 提交前自查

- [ ] 我没有修改原始数据文件。
- [ ] 路径不是写死在某个用户目录。
- [ ] 随机过程固定了种子。
- [ ] 结果能从头重新生成。

完成后再打开 [[python学习/11-参考答案/{folder}-参考答案|参考答案]]。
"""


def render_answer(folder: str, info: dict[str, str]) -> str:
    code_path = f"{folder}/模块综合参考.py"
    return f"""---
课程: Python学习
类型: 参考答案
模块: {folder}
tags: [Python, 参考答案, 数学建模]
---

# {info["title"]}参考答案

> [!important] 正确使用答案
> 先比较思路，不要逐字复制。找出自己代码与参考实现的三个差异；关闭本页后，从空白文件重写一次。

## 思路拆解

1. 先验证输入形状、字段或取值范围。
2. 把核心计算封装成函数，打印只放在调用处。
3. 先用极小数据人工核对，再运行完整数据。
4. 保存可复查结果，不能只依赖屏幕输出。

## 参考实现

```python
{dedent(info["answer"]).strip()}
```

可运行文件：[[python学习/13-VSCode代码/{code_path}|模块综合参考.py]]

## 预期结果

数值会随题目数据而不同，但必须满足：程序无未捕获异常、输出量纲合理、排序或指标能用人工小例子复核。

## 常见错误

- 输入校验放在计算之后。
- 只为当前数据写死列号或绝对路径。
- 函数内部同时读取、计算、画图、保存，导致难以测试。
- 对随机结果报告过多小数，却没有固定随机种子。

## 另一种写法

数据规模扩大后，可把基础列表循环替换成NumPy向量化或pandas分组；但替换前后必须在小样本上得到一致结果。
"""


MODULE_LABELS = {
    "01-Python基础": "Python基础",
    "02-函数文件与调试": "函数、文件与调试",
    "03-NumPy数值计算": "NumPy数值计算",
    "04-pandas数据处理": "pandas数据处理",
    "05-数据可视化": "数据可视化",
    "06-SciPy与优化": "SciPy与优化",
    "07-统计与机器学习": "统计与机器学习",
    "08-数学建模算法实现": "数学建模算法实现",
}


def navigation() -> str:
    grouped: dict[str, list[Topic]] = {}
    for topic in TOPICS:
        grouped.setdefault(topic.folder, []).append(topic)
    sections = []
    for folder, topics in grouped.items():
        rows = "\n".join(
            f"- `{topic.level}` [[python学习/{folder}/{Path(topic.filename).stem}|{topic.title}]]（约{topic.minutes}分钟）"
            for topic in topics
        )
        sections.append(
            f"## {MODULE_LABELS[folder]}\n\n{rows}\n\n"
            f"练习：[[python学习/10-练习题/{folder}-练习题|{MODULE_LABELS[folder]}三级练习]]"
        )
    sections_text = "\n\n".join(sections)
    return f"""---
课程: Python学习
类型: 总导航
学习期限: 2026-07-26至2026-08-15
每日投入: 约4小时
tags: [Python, 数学建模, MOC]
---

# Python数学建模学习总导航

> [!success] 课程目标
> 8月15日前完成比赛编程手所需Python的第一轮学习：能够在VS Code中独立读取与清洗数据、绘图、建模、评价、优化并保存可复现结果。8月16日至9月1日继续通过模拟题把“学会”变成“熟练”。

## 从这里开始

1. [[python学习/00-总导航与学习计划/课程使用说明|课程使用说明]]
2. [[python学习/00-总导航与学习计划/VSCode与venv环境搭建|VS Code与venv环境搭建]]
3. [[python学习/00-总导航与学习计划/VSCode运行、调试与Notebook|VS Code运行、调试与Notebook]]
4. [[python学习/00-总导航与学习计划/2026-07-26至08-15每日学习计划|每日学习计划]]
5. [[python学习/00-总导航与学习计划/学习进度看板|学习进度看板]]
6. [[python学习/00-总导航与学习计划/PyTorch与RTX4060配置说明|PyTorch与RTX 4060配置说明]]（学到神经网络时再看）

## 分级说明

| 标记 | 你的要求 |
|---|---|
| 必修 | 按计划手敲代码并完成练习；8月15日前掌握 |
| 进阶 | 至少读懂和运行；有余力再独立重写 |
| 赛时查阅 | 知道适用场景和模板位置，比赛遇到时能修改 |

{sections_text}

## 综合项目与比赛工具

- [[python学习/09-综合项目/模拟C题-城市韧性评估预测与资源配置|模拟C题题面]]
- [[python学习/09-综合项目/模拟C题-完成指南与验收|完成指南与验收]]
- [[python学习/00-总导航与学习计划/比赛编程手速查总表|比赛编程手速查总表]]
- [[python学习/00-总导航与学习计划/报错排查手册|报错排查手册]]
- [[数学建模国赛/00-导航与准备/数学建模国赛-C题总导航|原数学建模C题知识库]]

## 学会的判定

不要用“看完笔记”判定完成。一个主题必须依次通过：

1. **看懂**：能预测示例输出。
2. **复现**：关闭笔记后，从空白文件写出。
3. **迁移**：换数据、列名或参数仍能完成。
4. **解释**：能告诉队友输入、方法、参数、输出和局限。
5. **复现**：重新打开VS Code，一键从原始数据生成结果。

> [!warning] 现实边界
> 21天约80小时足以完成系统第一轮，但不会自动带来熟练。8月16日后至少完成两次限时综合练习。
"""


def course_usage() -> str:
    return """---
课程: Python学习
类型: 使用说明
tags: [Python, 学习方法]
---

# 课程使用说明

## 每篇短笔记怎么学

1. 阅读“学习目标”，用一句话说出本篇解决的问题。
2. 遮住输出，预测示例运行结果。
3. 在VS Code新建自己的练习文件，**亲手输入**，不要复制。
4. 运行成功后修改三个地方：输入值、业务规则、输出格式。
5. 主动制造一个错误，阅读Traceback，从最后一层自己的代码开始定位。
6. 关闭笔记，从空白文件重写核心部分。
7. 完成模块三级练习；最后才看独立答案。

## 每天4小时模板

| 环节 | 时间 | 做法 |
|---|---:|---|
| 间隔复习 | 20分钟 | 重做第1、3、7天前的关键题 |
| 新知识 | 50分钟 | 读短笔记并预测代码 |
| 手敲代码 | 100分钟 | 输入、运行、修改、调试 |
| 独立练习/项目 | 55分钟 | 从空白文件完成任务 |
| 错题与日志 | 15分钟 | 记录报错、原因、修复和防范 |

## 15分钟卡点规则

卡住后按顺序做：

1. 完整阅读Traceback，找到自己文件的行号。
2. 打印变量的值、`type`、数组或表格的`shape`。
3. 把数据缩小到3—5行，构造最小可复现例子。
4. 查本课程[[python学习/00-总导航与学习计划/报错排查手册|报错排查手册]]或官方文档。
5. 仍未解决再询问AI；提问时附目标、最小代码、完整报错和已尝试方法。

## 使用AI的纪律

- 先自己设计输入、输出和函数，再让AI检查。
- 不提交自己无法逐句解释的代码。
- 得到修复后关闭回答，从空白文件重写。
- 要求AI说明修改原因、适用前提和可能副作用。
- 所有关键数值用人工小例子或第二种方法复核。

## 文件使用

- `01—08`：按主题学习的短笔记。
- `10-练习题`：先做，答案不在同一页。
- `11-参考答案`：完成尝试后再打开。
- `12-示例数据`：原始练习数据，不要原地覆盖。
- `13-VSCode代码`：可运行示例、答案与模板。
- `tmp`：你运行程序产生的临时结果，可随时重新生成。

下一步：[[python学习/00-总导航与学习计划/VSCode与venv环境搭建|VS Code与venv环境搭建]]。
"""


def environment_note() -> str:
    return r"""---
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
"""


def vscode_note() -> str:
    return """---
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
"""


def troubleshooting_note() -> str:
    return """---
课程: Python学习
类型: 速查
tags: [Python, 报错, 调试]
---

# 报错排查手册

## 固定排查顺序

1. 阅读Traceback最末行的异常类型和信息。
2. 向上找到第一个属于自己项目的文件与行号。
3. 打印或在调试器观察值、`type()`、`shape`、列名。
4. 缩成最小输入复现。
5. 修复后增加输入检查，防止同类错误再次出现。

| 报错 | 常见原因 | 第一检查项 |
|---|---|---|
| `SyntaxError` | 括号、引号、冒号或中文符号 | 报错行及其上一行 |
| `IndentationError` | Tab与空格混用、缩进层级错 | VS Code格式化与空白字符 |
| `NameError` | 名字拼错、定义未执行 | 变量首次赋值位置 |
| `TypeError` | 对错误类型做操作 | `type(value)` |
| `ValueError` | 类型可转换但值不合法 | 原始字符串与范围 |
| `IndexError` | 列表/数组位置越界 | `len`与`shape` |
| `KeyError` | 字典键或DataFrame列不存在 | `dict.keys()`或`df.columns` |
| `FileNotFoundError` | 当前目录或路径错误 | `Path.cwd()`与完整解析路径 |
| `ModuleNotFoundError` | 解释器与安装环境不一致 | `sys.executable` |
| `UnicodeDecodeError` | 文件编码判断错误 | 尝试明确编码并确认来源 |
| `SettingWithCopyWarning` | pandas链式赋值 | 改用 `.loc`或 `.copy()` |
| shape/broadcast错误 | 数组维度不兼容 | 所有输入的 `.shape` |
| CUDA out of memory | 批量过大或旧张量未释放 | 减小batch，先用CPU验证 |

## 提问模板

```text
目标：
最小代码：
完整Traceback：
输入数据的前5行、类型和shape：
我已经尝试：
期望输出：
```

> [!danger] 不要这样修
> 不要使用裸 `except`隐藏错误；不要随机删除代码直到不报错；不要在不理解原因时升级或重装所有包。
"""


DAILY = [
    ("07-26", "环境与第一段程序", ["环境搭建", "VS Code运行与调试", "程序运行、输出与注释", "变量、数据类型与运算"], "环境检查脚本通过；从空白写数据质量计算器"),
    ("07-27", "文本与容器", ["字符串与格式化输出", "列表与元组", "字典与集合"], "完成文本解析和频数统计"),
    ("07-28", "流程控制", ["条件判断", "循环、range与遍历", "推导式与基础排序"], "完成Python基础三级练习A、B"),
    ("07-29", "函数化思维", ["函数、参数与返回值", "作用域与可变对象", "模块、包与main入口"], "把旧脚本拆成函数与main"),
    ("07-30", "文件与配置", ["Pathlib与文本文件", "CSV、JSON与配置", "异常处理与断言"], "完成配置驱动小程序"),
    ("07-31", "调试与小项目", ["VS Code断点调试与日志", "代码规范与可复现性"], "完成函数文件三级练习并重做7月26日题"),
    ("08-01", "NumPy数组", ["ndarray、形状与数据类型", "索引、切片与布尔筛选", "向量化与广播"], "实现两种标准化"),
    ("08-02", "NumPy数值能力", ["聚合、随机数与模拟", "线性代数与矩阵运算"], "完成NumPy三级练习和蒙特卡洛项目"),
    ("08-03", "pandas读取与选择", ["Series、DataFrame与读取数据", "选择、筛选、排序与赋值"], "审计环境数据并生成新列"),
    ("08-04", "pandas清洗与汇总", ["缺失、重复与异常值", "分组聚合与透视表"], "输出清洗日志；重做8月1日标准化"),
    ("08-05", "pandas多表与时间", ["合并、拼接与主键验证", "日期时间与时间序列整理", "Excel多工作表与结果导出"], "完成pandas三级练习"),
    ("08-06", "Matplotlib基础", ["Matplotlib的Figure与Axes", "折线、散点、柱状与分布图", "子图、中文、样式与标注"], "输出第一张论文级300DPI图片"),
    ("08-07", "EDA自动化", ["Seaborn与相关性热力图", "自动化EDA报告"], "完成可视化三级练习；重做8月4日清洗"),
    ("08-08", "SciPy数值与线性规划", ["插值、求根与数值积分", "SciPy线性规划实现"], "完成生产计划并人工核对约束"),
    ("08-09", "非线性与不确定性", ["非线性优化与约束", "曲线拟合与参数估计", "蒙特卡洛与不确定性传播"], "完成SciPy三级练习"),
    ("08-10", "统计解释", ["statsmodels线性回归与结果解释", "假设检验的Python实现"], "写出系数、区间、检验和局限"),
    ("08-11", "机器学习流水线", ["scikit-learn统一建模流程", "预处理与Pipeline防泄漏"], "从原始表到测试集指标一键运行"),
    ("08-12", "监督学习评价", ["回归模型与评价指标", "分类模型与评价指标", "交叉验证与超参数搜索"], "完成统计与机器学习练习A、B"),
    ("08-13", "无监督与时间", ["聚类与PCA", "时间序列预测与回测", "模型解释、敏感性与稳健性"], "建立模型对照表；重做8月10日回归"),
    ("08-14", "竞赛算法与PyTorch查阅", ["熵权法与TOPSIS实现", "AHP与一致性检验", "灰色预测GM(1,1)实现", "PyTorch张量、设备与自动求导"], "跑通模板，完成TOPSIS练习；其余达到赛时可查"),
    ("08-15", "模拟C题结业", ["模拟C题题面", "完成指南与验收", "比赛速查总表"], "限时完成数据清洗、评价、预测、优化并复盘"),
]


def daily_plan() -> str:
    start = date(2026, 7, 26)
    lines = []
    for index, (md, theme, topics, deliverable) in enumerate(DAILY):
        current = start + timedelta(days=index)
        review = []
        for lag in (1, 3, 7):
            if index - lag >= 0:
                review.append(DAILY[index - lag][1])
        review_text = "、".join(review) if review else "无，建立错题与报错日志"
        topic_links = []
        for title in topics:
            found = next((t for t in TOPICS if t.title == title), None)
            if found:
                topic_links.append(f"[[python学习/{found.folder}/{Path(found.filename).stem}|{title}]]")
            elif title == "环境搭建":
                topic_links.append("[[python学习/00-总导航与学习计划/VSCode与venv环境搭建|环境搭建]]")
            elif title == "VS Code运行与调试":
                topic_links.append("[[python学习/00-总导航与学习计划/VSCode运行、调试与Notebook|VS Code运行与调试]]")
            elif title == "模拟C题题面":
                topic_links.append("[[python学习/09-综合项目/模拟C题-城市韧性评估预测与资源配置|模拟C题题面]]")
            elif title == "完成指南与验收":
                topic_links.append("[[python学习/09-综合项目/模拟C题-完成指南与验收|完成指南与验收]]")
            elif title == "比赛速查总表":
                topic_links.append("[[python学习/00-总导航与学习计划/比赛编程手速查总表|比赛速查总表]]")
        lines.append(f"""## {current:%m月%d日}｜{theme}

- [ ] 复习20分钟：{review_text}
- [ ] 阅读50分钟：{"；".join(topic_links)}
- [ ] 手敲100分钟：所有示例至少改3处
- [ ] 独立练习55分钟：{deliverable}
- [ ] 日志15分钟：记录今天最有价值的一个报错

**当日验收：** {deliverable}。无法从空白文件完成时，本日不算“掌握”，次日先补20分钟。
""")
    lines_text = "\n".join(lines)
    return f"""---
课程: Python学习
类型: 每日计划
开始日期: 2026-07-26
结束日期: 2026-08-15
每日投入: 4小时
tags: [Python, 学习计划, 间隔复习]
---

# 2026-07-26至08-15每日学习计划

> [!important] 时间说明
> 每天共240分钟：复习20 + 新知识50 + 手敲100 + 项目55 + 日志15。任务很多时优先完成“必修”和当日验收；进阶与赛时查阅只需运行、理解入口和使用条件。

## 间隔复习规则

- D+1：不看示例重写核心代码。
- D+3：换一组输入或列名完成迁移。
- D+7：在综合任务中再次使用。
- 重写失败就把该主题移回“学习中”，不能只勾选阅读完成。

{lines_text}

## 8月16日至9月1日

- 8月16—20日：补齐未通过验收的必修，完成模拟C题参考实现对照。
- 8月21—25日：第一次团队限时模拟，完整生成论文表图。
- 8月26—29日：第二次团队限时模拟，交换电脑复现。
- 8月30—9月1日：冻结环境与模板，只修复问题，不再大规模升级。
"""


def progress_board() -> str:
    rows = "\n".join(
        f"| [[python学习/{topic.folder}/{Path(topic.filename).stem}|{topic.title}]] | {topic.level} | {topic.minutes} | ⬜ | |"
        for topic in TOPICS
    )
    module_lines = "\n".join(
        f"- [ ] [[python学习/10-练习题/{folder}-练习题|{MODULE_LABELS[folder]}三级练习]]"
        for folder in MODULE_LABELS
    )
    return f"""---
课程: Python学习
类型: 进度看板
tags: [Python, 进度]
---

# 学习进度看板

状态建议：⬜未开始、🟨看懂、🟦能复现、🟩能迁移。只有🟩才算掌握。

| 主题 | 分级 | 预计分钟 | 状态 | 下次复习 |
|---|---:|---:|---:|---|
{rows}

## 模块项目

{module_lines}
- [ ] [[python学习/09-综合项目/模拟C题-城市韧性评估预测与资源配置|模拟C题]]
- [ ] 换一台电脑或新终端按README复现全部结果
"""


def cheat_sheet() -> str:
    return """---
课程: Python学习
类型: 比赛速查
tags: [Python, 数学建模, 速查]
---

# 比赛编程手速查总表

## 拿到附件后的顺序

```text
复制原始附件并只读保存
→ 记录文件名、工作表、编码、行列数
→ 检查主键、类型、缺失、重复、范围、时间连续性
→ 输出审计表与EDA图
→ 建立人工或简单基准
→ Pipeline建模/求解
→ 验证、敏感性、稳健性
→ 一键导出论文表图
```

## 常用入口

| 任务 | 模板 |
|---|---|
| 环境诊断 | [[python学习/13-VSCode代码/00-环境检查.py|00-环境检查.py]] |
| 数据读取与审计 | [[python学习/13-VSCode代码/比赛模板/01_读取与审计.py|01_读取与审计.py]] |
| 清洗与多表合并 | [[python学习/13-VSCode代码/比赛模板/02_清洗与合并.py|02_清洗与合并.py]] |
| 论文级绘图 | [[python学习/13-VSCode代码/比赛模板/03_论文绘图.py|03_论文绘图.py]] |
| 回归Pipeline | [[python学习/13-VSCode代码/比赛模板/04_回归Pipeline.py|04_回归Pipeline.py]] |
| 分类Pipeline | [[python学习/13-VSCode代码/比赛模板/05_分类Pipeline.py|05_分类Pipeline.py]] |
| 聚类与PCA | [[python学习/13-VSCode代码/比赛模板/06_聚类与PCA.py|06_聚类与PCA.py]] |
| 时间序列回测 | [[python学习/13-VSCode代码/比赛模板/07_时间序列回测.py|07_时间序列回测.py]] |
| TOPSIS评价 | [[python学习/13-VSCode代码/比赛模板/08_TOPSIS.py|08_TOPSIS.py]] |
| 优化求解 | [[python学习/13-VSCode代码/比赛模板/09_优化求解.py|09_优化求解.py]] |
| 敏感性与Bootstrap | [[python学习/13-VSCode代码/比赛模板/10_稳健性.py|10_稳健性.py]] |
| PyTorch表格MLP | [[python学习/13-VSCode代码/比赛模板/11_PyTorch_MLP.py|11_PyTorch_MLP.py]] |
| 一键项目结构 | [[python学习/13-VSCode代码/比赛模板/README|比赛模板README]] |

## 每次建模必须打印

```python
print("数据形状：", df.shape)
print("列名：", df.columns.tolist())
print("缺失：", df.isna().sum().to_dict())
print("特征形状：", X.shape, "目标形状：", y.shape)
print("随机种子：", RANDOM_SEED)
```

## 三条底线

1. 原始附件永不覆盖；所有中间表和图由代码生成。
2. 测试集不参与预处理拟合、调参和阈值选择。
3. 求解器或模型成功运行不等于结论正确，必须人工小例子、基准和稳健性验证。

理论方法选择见[[数学建模国赛/00-导航与准备/C题方法选择速查表|C题方法选择速查表]]；项目复现见[[数学建模国赛/08-竞赛实战/代码项目结构与复现清单|代码项目结构与复现清单]]。
"""


def capstone_problem() -> str:
    return """---
课程: Python学习
类型: 综合项目题面
难度: 结业
建议限时: 8小时
tags: [Python, 模拟C题, 综合项目]
---

# 模拟C题：城市韧性评估、风险预测与资源配置

某地区希望依据过去两年的城市月度监测、城市基础属性和应急项目数据，评价各城市的综合韧性，预测下一阶段风险，并在预算约束下配置应急资源。附件为本课程生成的模拟数据，存在少量缺失、重复和异常值。

## 附件

- `12-示例数据/模拟C题/附件1_城市月度监测.csv/.xlsx`
- `12-示例数据/模拟C题/附件2_城市基础信息.csv/.xlsx`
- `12-示例数据/模拟C题/附件3_应急项目.csv/.xlsx`
- `12-示例数据/模拟C题/数据字典.md`

## 问题一：数据质量与特征构造

识别并处理重复、缺失和异常记录，说明规则与影响；合并附件1和附件2，构造至少4个具有实际含义的城市韧性指标，生成描述统计和关键图表。

要求：

- 原始附件不可覆盖。
- 输出清洗日志、异常记录和城市级汇总。
- 至少比较一种替代清洗规则。

## 问题二：综合评价与城市分型

建立城市韧性综合评价模型，给出年度得分与排名；使用聚类形成城市类型并解释各类特征。

要求：

- 明确指标方向与权重来源。
- 至少采用TOPSIS；可结合熵权或AHP。
- 对权重变化做敏感性分析。
- 聚类前处理量纲并报告内部评价指标。

## 问题三：风险预测

预测每个城市下一季度的风险指标，比较至少一个简单基准和一个统计/机器学习模型。

要求：

- 严格按时间切分。
- 报告MAE、RMSE或适合的分类指标。
- 输出预测图、误差表和模型局限。
- PyTorch MLP可作为加分对照，不是必需。

## 问题四：资源配置

附件3列出候选应急项目、成本、能力提升和适用城市。在总预算1800万元、每个城市最多选择2个项目的条件下，给出资源配置方案，使预测风险下降与韧性提升的综合收益最大。

要求：

- 定义决策变量、目标和约束。
- 检查方案可行性。
- 对预算±10%和收益估计±10%做敏感性分析。
- 若使用连续近似，必须说明取整带来的问题；可使用SciPy `milp`。

## 最终交付

- 一键运行脚本或 `run_all.py`。
- 清洗后数据、模型结果Excel、至少5张300 DPI图片。
- 每个问题的结论、模型假设、局限和稳健性说明。
- `README.md`写清环境、入口、运行顺序和输出位置。

完成时使用[[python学习/09-综合项目/模拟C题-完成指南与验收|完成指南与验收]]，不要先打开完整参考实现。
"""


def capstone_guide() -> str:
    return """---
课程: Python学习
类型: 综合项目指南
tags: [Python, 模拟C题, 验收]
---

# 模拟C题完成指南与验收

## 建议时间盒

| 阶段 | 时间 | 最低输出 |
|---|---:|---|
| 审题与数据字典 | 30分钟 | 字段、单位、主键、问题链 |
| 数据审计与清洗 | 90分钟 | 清洗日志、异常表、合并表 |
| 评价与分型 | 90分钟 | 得分排名、聚类、敏感性 |
| 预测与回测 | 120分钟 | 基线、模型、误差、预测图 |
| 优化配置 | 90分钟 | 变量、目标、约束、方案 |
| 复现与表达 | 60分钟 | 一键运行、Excel、图、README |

## 分问之间的数据流

```mermaid
flowchart LR
    A["附件1 月度监测"] --> C["清洗与城市级特征"]
    B["附件2 基础信息"] --> C
    C --> D["TOPSIS评价"]
    C --> E["聚类分型"]
    C --> F["时间回测与风险预测"]
    D --> G["项目综合收益"]
    E --> G
    F --> G
    H["附件3 候选项目"] --> G
    G --> I["预算约束下资源配置"]
```

## 验收清单

### 数据

- [ ] 主键关系经过 `validate`检查。
- [ ] 清洗前后行数和规则有日志。
- [ ] 日期顺序、单位与指标方向正确。
- [ ] 原始数据未覆盖。

### 模型

- [ ] 有可解释的简单基准。
- [ ] 训练、验证、测试或时间回测边界清楚。
- [ ] 权重、阈值和随机种子可追踪。
- [ ] 指标选择与业务损失一致。

### 结果

- [ ] 排名可用极小人工样例复核。
- [ ] 优化方案逐条验证约束。
- [ ] 至少做一项敏感性和一项替代设定稳健性。
- [ ] 图表有标题、单位、图例并由代码保存。

### 工程

- [ ] 新终端中可从头运行。
- [ ] 输出目录可删除后重新生成。
- [ ] README说明依赖与运行入口。
- [ ] 队友能在5分钟内找到结果表和图。

## 参考实现使用规则

参考实现位于 `13-VSCode代码/综合项目参考实现`。至少独立工作4小时后再查看；只比较目录、函数边界和验证方法，不要直接把参考数值当自己的结果。
"""


def data_dictionary() -> str:
    return """# 模拟C题数据字典

## 附件1：城市月度监测

| 字段 | 含义 | 单位/类型 |
|---|---|---|
| 记录ID | 月度记录主键，模拟数据中含少量重复 | 文本 |
| 城市ID | 连接基础信息的键 | 文本 |
| 日期 | 月初日期 | 日期 |
| 经济活力 | 越大越好 | 分 |
| 医疗负荷 | 越小越好 | % |
| 应急响应时间 | 越小越好 | 分钟 |
| 基础设施完好率 | 越大越好 | % |
| 灾害损失率 | 风险目标，越小越好 | % |
| 降雨量 | 外部风险因素 | mm |

## 附件2：城市基础信息

| 字段 | 含义 |
|---|---|
| 城市ID | 唯一主键 |
| 城市名称 | 模拟城市名称 |
| 地区 | 东、中、西三类 |
| 常住人口 | 万人 |
| 财政能力 | 0—100分 |

## 附件3：应急项目

| 字段 | 含义 |
|---|---|
| 项目ID | 唯一主键 |
| 城市ID | 项目适用城市 |
| 项目类型 | 医疗、排水、通信或储备 |
| 成本 | 万元 |
| 预测风险下降 | 百分点 |
| 韧性提升 | 分 |

所有数据均为教学目的生成，不对应真实城市。异常和缺失是有意设置，用于训练数据审计。
"""


ENV_CHECK = r'''
from __future__ import annotations

import importlib
import os
import platform
import sys
from pathlib import Path

matplotlib_cache = Path(__file__).resolve().parents[1] / "tmp" / ".matplotlib"
matplotlib_cache.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(matplotlib_cache))


PACKAGES = [
    "numpy", "pandas", "matplotlib", "seaborn", "scipy",
    "statsmodels", "sklearn", "openpyxl", "torch",
]


def main() -> None:
    print("Python:", sys.version.replace("\n", " "))
    print("解释器:", sys.executable)
    print("系统:", platform.platform())
    for name in PACKAGES:
        try:
            module = importlib.import_module(name)
            version = getattr(module, "__version__", "未知")
            print(f"[OK] {name:<12} {version}")
        except Exception as error:
            print(f"[--] {name:<12} {type(error).__name__}: {error}")
    try:
        import torch
        print("CUDA可用:", torch.cuda.is_available())
        if torch.cuda.is_available():
            print("GPU:", torch.cuda.get_device_name(0))
    except ImportError:
        pass


if __name__ == "__main__":
    main()
'''


TEMPLATE_SCRIPTS = {
    "01_读取与审计.py": r'''
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "12-示例数据" / "环境监测数据.csv"
OUTPUT_DIR = ROOT / "tmp" / "比赛模板输出"


def audit(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "missing_count": df.isna().sum(),
        "missing_rate": df.isna().mean(),
        "unique_count": df.nunique(dropna=False),
    })


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(DATA_PATH)
    print("shape:", df.shape)
    print("columns:", df.columns.tolist())
    audit(df).to_csv(OUTPUT_DIR / "audit.csv", encoding="utf-8-sig")
    df.describe(include="all").to_csv(
        OUTPUT_DIR / "describe.csv", encoding="utf-8-sig"
    )


if __name__ == "__main__":
    main()
''',
    "02_清洗与合并.py": r'''
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "12-示例数据"
OUTPUT_DIR = ROOT / "tmp" / "比赛模板输出"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    measurements = pd.read_csv(DATA / "环境监测数据.csv", parse_dates=["日期"])
    stations = pd.read_csv(DATA / "站点信息.csv")
    measurements = measurements.drop_duplicates("记录ID").copy()
    measurements["温度"] = measurements["温度"].fillna(
        measurements.groupby("站点")["温度"].transform("median")
    )
    merged = measurements.merge(
        stations, on="站点", how="left", validate="many_to_one", indicator=True
    )
    if (merged["_merge"] != "both").any():
        raise ValueError("存在未匹配站点")
    merged.drop(columns="_merge").to_csv(
        OUTPUT_DIR / "clean_merged.csv", index=False, encoding="utf-8-sig"
    )
    print("clean shape:", merged.shape)


if __name__ == "__main__":
    main()
''',
    "03_论文绘图.py": r'''
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "12-示例数据" / "环境监测数据.csv"
OUTPUT_DIR = ROOT / "tmp" / "比赛模板输出"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(DATA, parse_dates=["日期"])
    daily = df.groupby("日期", as_index=False)["PM2.5"].mean()
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(daily["日期"], daily["PM2.5"], color="#4C78A8")
    ax.set(xlabel="Date", ylabel="PM2.5 (ug/m3)", title="Daily PM2.5")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "paper_figure.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
''',
    "04_回归Pipeline.py": r'''
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    X, y = load_diabetes(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = make_pipeline(SimpleImputer(), StandardScaler(), Ridge(alpha=1.0))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print({
        "MAE": mean_absolute_error(y_test, pred),
        "RMSE": np.sqrt(mean_squared_error(y_test, pred)),
        "R2": r2_score(y_test, pred),
    })


if __name__ == "__main__":
    main()
''',
    "05_分类Pipeline.py": r'''
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    X, y = load_breast_cancer(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
    model.fit(X_train, y_train)
    probability = model.predict_proba(X_test)[:, 1]
    prediction = (probability >= 0.5).astype(int)
    print(classification_report(y_test, prediction, zero_division=0))
    print("AUC:", roc_auc_score(y_test, probability))


if __name__ == "__main__":
    main()
''',
    "06_聚类与PCA.py": r'''
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


def main() -> None:
    X, _ = load_iris(return_X_y=True)
    X_scaled = StandardScaler().fit_transform(X)
    labels = KMeans(n_clusters=3, n_init=20, random_state=42).fit_predict(X_scaled)
    points = PCA(n_components=2).fit_transform(X_scaled)
    print("silhouette:", silhouette_score(X_scaled, labels))
    print("PCA shape:", points.shape)


if __name__ == "__main__":
    main()
''',
    "07_时间序列回测.py": r'''
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def main() -> None:
    rng = np.random.default_rng(42)
    t = np.arange(48)
    y = 100 + 0.8 * t + 10 * np.sin(2 * np.pi * t / 12) + rng.normal(0, 2, len(t))
    series = pd.Series(y, index=pd.date_range("2022-01-01", periods=48, freq="MS"))
    train, test = series.iloc[:-6], series.iloc[-6:]
    naive = np.repeat(train.iloc[-1], len(test))
    model = ExponentialSmoothing(
        train, trend="add", seasonal="add", seasonal_periods=12
    ).fit()
    pred = model.forecast(len(test))
    print("naive MAE:", mean_absolute_error(test, naive))
    print("ETS MAE:", mean_absolute_error(test, pred))


if __name__ == "__main__":
    main()
''',
    "08_TOPSIS.py": r'''
import numpy as np


def topsis(X, weights, cost_columns=()):
    X = np.asarray(X, dtype=float).copy()
    weights = np.asarray(weights, dtype=float)
    for column in cost_columns:
        X[:, column] = X[:, column].max() - X[:, column]
    denominator = np.linalg.norm(X, axis=0)
    denominator[denominator == 0] = 1
    V = X / denominator * (weights / weights.sum())
    d_pos = np.linalg.norm(V - V.max(axis=0), axis=1)
    d_neg = np.linalg.norm(V - V.min(axis=0), axis=1)
    score = d_neg / np.where(d_pos + d_neg == 0, 1, d_pos + d_neg)
    return score


def main() -> None:
    X = [[80, 20, 7], [70, 15, 9], [90, 30, 6]]
    score = topsis(X, [0.4, 0.3, 0.3], cost_columns=[1])
    print(score)
    print("ranking:", np.argsort(-score) + 1)


if __name__ == "__main__":
    main()
''',
    "09_优化求解.py": r'''
import numpy as np
from scipy.optimize import linprog


def main() -> None:
    profit = np.array([5, 7, 4], dtype=float)
    A = np.array([[2, 3, 1], [1, 2, 2]], dtype=float)
    b = np.array([180, 120], dtype=float)
    result = linprog(-profit, A_ub=A, b_ub=b,
                     bounds=[(0, None)] * 3, method="highs")
    if not result.success:
        raise RuntimeError(result.message)
    print("x:", result.x)
    print("objective:", -result.fun)
    print("feasible:", np.all(A @ result.x <= b + 1e-7))


if __name__ == "__main__":
    main()
''',
    "10_稳健性.py": r'''
import numpy as np


def bootstrap_mean(values, n_bootstrap=5000, seed=42):
    values = np.asarray(values, dtype=float)
    rng = np.random.default_rng(seed)
    samples = rng.choice(values, size=(n_bootstrap, len(values)), replace=True)
    means = samples.mean(axis=1)
    return np.quantile(means, [0.025, 0.5, 0.975])


def main() -> None:
    values = [12, 15, 14, 18, 20, 17, 16]
    print(bootstrap_mean(values))


if __name__ == "__main__":
    main()
''',
    "11_PyTorch_MLP.py": r'''
import torch
from torch import nn


def main() -> None:
    torch.manual_seed(42)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    X = torch.randn(128, 4, device=device)
    y = (2 * X[:, :1] - X[:, 1:2] + 0.1 * torch.randn(128, 1, device=device))
    model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 1)).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.02)
    loss_fn = nn.MSELoss()
    for _ in range(100):
        optimizer.zero_grad()
        loss = loss_fn(model(X), y)
        loss.backward()
        optimizer.step()
    print("device:", device, "loss:", loss.item())


if __name__ == "__main__":
    main()
''',
}


CAPSTONE_COMMON = r'''
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "12-示例数据" / "模拟C题"
OUTPUT_DIR = ROOT / "tmp" / "模拟C题输出"
FIGURE_DIR = OUTPUT_DIR / "figures"
RANDOM_SEED = 42


def ensure_directories() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
'''


CAPSTONE_SCRIPTS = {
    "01_clean.py": r'''
import json
import pandas as pd
from common import DATA_DIR, OUTPUT_DIR, ensure_directories


def main() -> None:
    ensure_directories()
    monthly = pd.read_csv(DATA_DIR / "附件1_城市月度监测.csv", parse_dates=["日期"])
    cities = pd.read_csv(DATA_DIR / "附件2_城市基础信息.csv")
    before = len(monthly)
    duplicate_count = int(monthly["记录ID"].duplicated().sum())
    monthly = monthly.drop_duplicates("记录ID").copy()
    numeric = ["经济活力", "医疗负荷", "应急响应时间", "基础设施完好率", "灾害损失率", "降雨量"]
    missing_before = monthly[numeric].isna().sum().astype(int).to_dict()
    for column in numeric:
        monthly[column] = monthly[column].fillna(
            monthly.groupby("城市ID")[column].transform("median")
        )
        monthly[column] = monthly[column].fillna(monthly[column].median())
    anomaly_rows = []
    for column in numeric:
        q1, q3 = monthly[column].quantile([0.25, 0.75])
        lower, upper = q1 - 3 * (q3 - q1), q3 + 3 * (q3 - q1)
        mask = ~monthly[column].between(lower, upper)
        if mask.any():
            part = monthly.loc[mask, ["记录ID", "城市ID", "日期", column]].copy()
            part["字段"] = column
            part["原值"] = part[column]
            anomaly_rows.append(part.drop(columns=column))
            monthly.loc[mask, column] = monthly.loc[~mask, column].median()
    merged = monthly.merge(
        cities, on="城市ID", how="left", validate="many_to_one", indicator=True
    )
    if (merged["_merge"] != "both").any():
        raise ValueError("存在无法匹配的城市ID")
    merged = merged.drop(columns="_merge")
    anomalies = pd.concat(anomaly_rows, ignore_index=True) if anomaly_rows else pd.DataFrame()
    log = {
        "清洗前行数": before,
        "重复记录数": duplicate_count,
        "清洗后行数": len(merged),
        "缺失数": missing_before,
        "异常替换数": len(anomalies),
    }
    merged.to_csv(OUTPUT_DIR / "clean_monthly.csv", index=False, encoding="utf-8-sig")
    anomalies.to_csv(OUTPUT_DIR / "anomalies.csv", index=False, encoding="utf-8-sig")
    (OUTPUT_DIR / "cleaning_log.json").write_text(
        json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(log)


if __name__ == "__main__":
    main()
''',
    "02_evaluate.py": r'''
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from common import FIGURE_DIR, OUTPUT_DIR, RANDOM_SEED, ensure_directories


def entropy_weights(X: np.ndarray) -> np.ndarray:
    minimum, span = X.min(axis=0), X.max(axis=0) - X.min(axis=0)
    Z = (X - minimum) / np.where(span == 0, 1, span)
    P = (Z + 1e-12) / (Z + 1e-12).sum(axis=0)
    entropy = -(P * np.log(P)).sum(axis=0) / np.log(len(X))
    difference = 1 - entropy
    return difference / difference.sum()


def topsis(X: np.ndarray, weights: np.ndarray) -> np.ndarray:
    denominator = np.linalg.norm(X, axis=0)
    V = X / np.where(denominator == 0, 1, denominator) * weights
    d_pos = np.linalg.norm(V - V.max(axis=0), axis=1)
    d_neg = np.linalg.norm(V - V.min(axis=0), axis=1)
    return d_neg / np.where(d_pos + d_neg == 0, 1, d_pos + d_neg)


def main() -> None:
    ensure_directories()
    df = pd.read_csv(OUTPUT_DIR / "clean_monthly.csv", parse_dates=["日期"])
    latest_year = df["日期"].dt.year.max()
    current = df.loc[df["日期"].dt.year == latest_year]
    city = current.groupby(["城市ID", "城市名称", "地区"], as_index=False).agg(
        经济活力=("经济活力", "mean"),
        医疗负荷=("医疗负荷", "mean"),
        应急响应时间=("应急响应时间", "mean"),
        基础设施完好率=("基础设施完好率", "mean"),
        灾害损失率=("灾害损失率", "mean"),
    )
    columns = ["经济活力", "医疗负荷", "应急响应时间", "基础设施完好率", "灾害损失率"]
    X = city[columns].to_numpy(float)
    X[:, [1, 2, 4]] *= -1
    weights = entropy_weights(X)
    city["韧性得分"] = topsis(X, weights)
    city["韧性排名"] = city["韧性得分"].rank(ascending=False, method="min").astype(int)
    X_scaled = StandardScaler().fit_transform(city[columns])
    labels = KMeans(n_clusters=3, n_init=30, random_state=RANDOM_SEED).fit_predict(X_scaled)
    city["城市类型"] = labels + 1
    print("silhouette:", silhouette_score(X_scaled, labels))
    city.sort_values("韧性排名").to_csv(
        OUTPUT_DIR / "city_scores.csv", index=False, encoding="utf-8-sig"
    )
    pd.DataFrame({"指标": columns, "熵权": weights}).to_csv(
        OUTPUT_DIR / "weights.csv", index=False, encoding="utf-8-sig"
    )
    fig, ax = plt.subplots(figsize=(8, 4))
    ordered = city.sort_values("韧性得分")
    ax.barh(ordered["城市名称"], ordered["韧性得分"], color="#4C78A8")
    ax.set(xlabel="Resilience score", title="City resilience ranking")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "city_ranking.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
''',
    "03_predict.py": r'''
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from common import FIGURE_DIR, OUTPUT_DIR, ensure_directories


def main() -> None:
    ensure_directories()
    df = pd.read_csv(OUTPUT_DIR / "clean_monthly.csv", parse_dates=["日期"])
    rows, forecasts = [], []
    for (city_id, city_name), group in df.groupby(["城市ID", "城市名称"]):
        series = group.sort_values("日期").set_index("日期")["灾害损失率"]
        train, test = series.iloc[:-3], series.iloc[-3:]
        naive = np.repeat(train.iloc[-1], len(test))
        model = ExponentialSmoothing(
            train, trend="add", seasonal="add", seasonal_periods=12
        ).fit(optimized=True)
        pred = model.forecast(len(test))
        rows.append({
            "城市ID": city_id, "城市名称": city_name,
            "朴素MAE": mean_absolute_error(test, naive),
            "ETS_MAE": mean_absolute_error(test, pred),
            "ETS_RMSE": np.sqrt(mean_squared_error(test, pred)),
        })
        final_model = ExponentialSmoothing(
            series, trend="add", seasonal="add", seasonal_periods=12
        ).fit(optimized=True)
        future = final_model.forecast(3)
        for day, value in future.items():
            forecasts.append({
                "城市ID": city_id, "城市名称": city_name,
                "日期": day, "预测灾害损失率": max(float(value), 0.0),
            })
    metrics = pd.DataFrame(rows)
    forecast_df = pd.DataFrame(forecasts)
    metrics.to_csv(OUTPUT_DIR / "forecast_metrics.csv", index=False, encoding="utf-8-sig")
    forecast_df.to_csv(OUTPUT_DIR / "next_quarter_forecast.csv", index=False, encoding="utf-8-sig")
    first_city = df["城市名称"].iloc[0]
    history = df.loc[df["城市名称"] == first_city].sort_values("日期")
    future = forecast_df.loc[forecast_df["城市名称"] == first_city]
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(history["日期"], history["灾害损失率"], label="history")
    ax.plot(pd.to_datetime(future["日期"]), future["预测灾害损失率"],
            marker="o", label="forecast")
    ax.legend()
    ax.set(title=f"Risk forecast: {first_city}", ylabel="Loss rate")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "risk_forecast.png", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(metrics.mean(numeric_only=True).to_dict())


if __name__ == "__main__":
    main()
''',
    "04_optimize.py": r'''
import numpy as np
import pandas as pd
from scipy.optimize import Bounds, LinearConstraint, milp
from common import DATA_DIR, OUTPUT_DIR, ensure_directories


def solve(budget: float = 1800.0, benefit_scale: float = 1.0) -> pd.DataFrame:
    projects = pd.read_csv(DATA_DIR / "附件3_应急项目.csv")
    scores = pd.read_csv(OUTPUT_DIR / "city_scores.csv")
    forecast = pd.read_csv(OUTPUT_DIR / "next_quarter_forecast.csv")
    risk = forecast.groupby("城市ID", as_index=False)["预测灾害损失率"].mean()
    projects = projects.merge(scores[["城市ID", "韧性得分"]], on="城市ID",
                              validate="many_to_one")
    projects = projects.merge(risk, on="城市ID", validate="many_to_one")
    projects["综合收益"] = benefit_scale * (
        projects["预测风险下降"] * (1 + projects["预测灾害损失率"] / 10)
        + projects["韧性提升"] * (1 + (1 - projects["韧性得分"]))
    )
    n = len(projects)
    constraints = [LinearConstraint(projects["成本"].to_numpy()[None, :], -np.inf, budget)]
    for _, index in projects.groupby("城市ID").groups.items():
        row = np.zeros(n)
        row[list(index)] = 1
        constraints.append(LinearConstraint(row[None, :], -np.inf, 2))
    result = milp(
        c=-projects["综合收益"].to_numpy(),
        integrality=np.ones(n),
        bounds=Bounds(np.zeros(n), np.ones(n)),
        constraints=constraints,
        options={"time_limit": 30},
    )
    if not result.success:
        raise RuntimeError(result.message)
    projects["是否选择"] = (result.x > 0.5).astype(int)
    chosen = projects.loc[projects["是否选择"] == 1].copy()
    if chosen["成本"].sum() > budget + 1e-6:
        raise AssertionError("预算约束未满足")
    return chosen


def main() -> None:
    ensure_directories()
    all_scenarios = []
    for budget in (1620, 1800, 1980):
        for scale in (0.9, 1.0, 1.1):
            chosen = solve(budget, scale)
            chosen["预算情景"] = budget
            chosen["收益系数"] = scale
            all_scenarios.append(chosen)
    result = pd.concat(all_scenarios, ignore_index=True)
    result.to_csv(OUTPUT_DIR / "allocation_scenarios.csv", index=False, encoding="utf-8-sig")
    base = result.loc[(result["预算情景"] == 1800) & (result["收益系数"] == 1.0)]
    print("base cost:", base["成本"].sum(), "projects:", len(base))


if __name__ == "__main__":
    main()
''',
    "05_export.py": r'''
import pandas as pd
from common import OUTPUT_DIR, ensure_directories


def main() -> None:
    ensure_directories()
    sheets = {
        "城市评价": pd.read_csv(OUTPUT_DIR / "city_scores.csv"),
        "模型评价": pd.read_csv(OUTPUT_DIR / "forecast_metrics.csv"),
        "下季预测": pd.read_csv(OUTPUT_DIR / "next_quarter_forecast.csv"),
        "资源配置": pd.read_csv(OUTPUT_DIR / "allocation_scenarios.csv"),
    }
    with pd.ExcelWriter(OUTPUT_DIR / "模拟C题结果.xlsx", engine="openpyxl") as writer:
        for sheet_name, frame in sheets.items():
            frame.to_excel(writer, sheet_name=sheet_name, index=False)
    print(OUTPUT_DIR / "模拟C题结果.xlsx")


if __name__ == "__main__":
    main()
''',
    "run_all.py": r'''
from pathlib import Path
import subprocess
import sys


def main() -> None:
    folder = Path(__file__).resolve().parent
    scripts = ["01_clean.py", "02_evaluate.py", "03_predict.py",
               "04_optimize.py", "05_export.py"]
    for script in scripts:
        print(f"\n===== RUN {script} =====")
        subprocess.run([sys.executable, str(folder / script)], check=True)


if __name__ == "__main__":
    main()
''',
}


def build_datasets() -> None:
    data_dir = ROOT / "12-示例数据"
    data_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(42)

    stations = pd.DataFrame({
        "站点": [f"S{i:02d}" for i in range(1, 7)],
        "地区": ["东区", "东区", "中区", "中区", "西区", "西区"],
        "经度": [121.2, 121.5, 120.7, 120.9, 119.8, 120.1],
        "纬度": [31.1, 31.3, 30.9, 31.0, 30.5, 30.7],
    })
    station_rows = []
    dates = pd.date_range("2026-01-01", periods=60, freq="D")
    for station_index, station in enumerate(stations["站点"]):
        for day_index, day in enumerate(dates):
            temp = 12 + 0.15 * day_index + station_index * 0.4 + rng.normal(0, 1.5)
            humidity = 72 - 0.1 * day_index + rng.normal(0, 4)
            pm25 = 35 + station_index * 2 + 6 * np.sin(day_index / 7) + rng.normal(0, 5)
            station_rows.append({
                "记录ID": f"{station}-{day:%Y%m%d}",
                "站点": station,
                "地区": stations.loc[stations["站点"] == station, "地区"].iloc[0],
                "日期": day,
                "温度": round(temp, 2),
                "湿度": round(humidity, 2),
                "PM2.5": round(pm25, 2),
                "状态": "有效",
            })
    environment = pd.DataFrame(station_rows)
    environment.loc[[15, 111, 208], "温度"] = np.nan
    environment.loc[[38, 190], "PM2.5"] = np.nan
    environment.loc[75, "PM2.5"] = 180.0
    environment.loc[140, "温度"] = -25.0
    environment = pd.concat([environment, environment.iloc[[20]]], ignore_index=True)
    environment.to_csv(data_dir / "环境监测数据.csv", index=False, encoding="utf-8-sig")
    environment.to_excel(data_dir / "环境监测数据.xlsx", index=False)
    stations.to_csv(data_dir / "站点信息.csv", index=False, encoding="utf-8-sig")
    stations.to_excel(data_dir / "站点信息.xlsx", index=False)

    city_indicators = pd.DataFrame({
        "城市": [f"城市{letter}" for letter in "ABCDEFGH"],
        "经济活力": np.round(rng.uniform(55, 95, 8), 2),
        "污染指数": np.round(rng.uniform(20, 65, 8), 2),
        "公共服务": np.round(rng.uniform(50, 90, 8), 2),
        "单位成本": np.round(rng.uniform(10, 28, 8), 2),
    })
    city_indicators.to_csv(data_dir / "城市评价指标.csv", index=False, encoding="utf-8-sig")
    city_indicators.to_excel(data_dir / "城市评价指标.xlsx", index=False)

    n = 260
    age = rng.integers(18, 70, n)
    income = rng.normal(8, 2.2, n)
    region = rng.choice(["东部", "中部", "西部"], n, p=[0.4, 0.35, 0.25])
    score = 0.05 * (age - 40) + 0.5 * (income - 8) + (region == "东部") * 0.8
    probability = 1 / (1 + np.exp(-score))
    label = rng.binomial(1, probability)
    classification = pd.DataFrame({
        "年龄": age, "收入": np.round(income, 2), "地区": region, "是否高风险": label
    })
    classification.loc[rng.choice(n, 8, replace=False), "收入"] = np.nan
    classification.to_csv(data_dir / "分类预测样本.csv", index=False, encoding="utf-8-sig")
    classification.to_excel(data_dir / "分类预测样本.xlsx", index=False)

    cap_dir = data_dir / "模拟C题"
    cap_dir.mkdir(parents=True, exist_ok=True)
    city_ids = [f"C{i:02d}" for i in range(1, 11)]
    city_base = pd.DataFrame({
        "城市ID": city_ids,
        "城市名称": [f"韧城{i}" for i in range(1, 11)],
        "地区": ["东部"] * 4 + ["中部"] * 3 + ["西部"] * 3,
        "常住人口": np.round(rng.uniform(80, 700, 10), 1),
        "财政能力": np.round(rng.uniform(50, 95, 10), 2),
    })
    months = pd.date_range("2024-01-01", periods=30, freq="MS")
    monthly_rows = []
    for city_index, city_id in enumerate(city_ids):
        quality = rng.normal(0, 1)
        for month_index, month in enumerate(months):
            seasonal = np.sin(2 * np.pi * month_index / 12)
            rain = max(20 + 45 * (seasonal + 1) + rng.normal(0, 15), 0)
            economic = 60 + city_index * 1.8 + 0.3 * month_index + rng.normal(0, 2)
            medical = 65 - quality * 3 + 5 * seasonal + rng.normal(0, 3)
            response = 42 - quality * 2 + 0.03 * rain + rng.normal(0, 2)
            infra = 72 + quality * 4 + 0.2 * month_index + rng.normal(0, 2)
            loss = (
                3.5 + 0.025 * rain + 0.04 * medical + 0.035 * response
                - 0.035 * infra - 0.012 * economic + rng.normal(0, 0.45)
            )
            monthly_rows.append({
                "记录ID": f"{city_id}-{month:%Y%m}",
                "城市ID": city_id,
                "日期": month,
                "经济活力": round(economic, 2),
                "医疗负荷": round(medical, 2),
                "应急响应时间": round(response, 2),
                "基础设施完好率": round(infra, 2),
                "灾害损失率": round(max(loss, 0.2), 3),
                "降雨量": round(rain, 2),
            })
    monthly = pd.DataFrame(monthly_rows)
    for column, indices in {
        "经济活力": [12, 87],
        "医疗负荷": [45, 133, 201],
        "应急响应时间": [76],
        "基础设施完好率": [167],
    }.items():
        monthly.loc[indices, column] = np.nan
    monthly.loc[101, "灾害损失率"] = 25.0
    monthly.loc[222, "应急响应时间"] = 180.0
    monthly = pd.concat([monthly, monthly.iloc[[55, 144]]], ignore_index=True)
    project_types = ["医疗", "排水", "通信", "储备"]
    project_rows = []
    project_number = 1
    for city_id in city_ids:
        for project_type in rng.choice(project_types, size=3, replace=False):
            project_rows.append({
                "项目ID": f"P{project_number:03d}",
                "城市ID": city_id,
                "项目类型": project_type,
                "成本": int(rng.integers(90, 260)),
                "预测风险下降": round(float(rng.uniform(0.3, 1.8)), 3),
                "韧性提升": round(float(rng.uniform(1.0, 6.0)), 3),
            })
            project_number += 1
    projects = pd.DataFrame(project_rows)
    monthly.to_csv(cap_dir / "附件1_城市月度监测.csv", index=False, encoding="utf-8-sig")
    city_base.to_csv(cap_dir / "附件2_城市基础信息.csv", index=False, encoding="utf-8-sig")
    projects.to_csv(cap_dir / "附件3_应急项目.csv", index=False, encoding="utf-8-sig")
    with pd.ExcelWriter(cap_dir / "模拟C题附件汇总.xlsx", engine="openpyxl") as writer:
        monthly.to_excel(writer, sheet_name="城市月度监测", index=False)
        city_base.to_excel(writer, sheet_name="城市基础信息", index=False)
        projects.to_excel(writer, sheet_name="应急项目", index=False)
    monthly.to_excel(cap_dir / "附件1_城市月度监测.xlsx", index=False)
    city_base.to_excel(cap_dir / "附件2_城市基础信息.xlsx", index=False)
    projects.to_excel(cap_dir / "附件3_应急项目.xlsx", index=False)
    write("12-示例数据/模拟C题/数据字典.md", data_dictionary())


def build_notebook() -> None:
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["# EDA交互练习\n", "在VS Code中选择项目`.venv`内核，然后依次运行。"],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "from pathlib import Path\n",
                    "import pandas as pd\n",
                    "root = Path.cwd().parents[1] if Path.cwd().name == 'Notebook' else Path.cwd()\n",
                    "df = pd.read_csv(root / '12-示例数据' / '环境监测数据.csv', parse_dates=['日期'])\n",
                    "df.head()\n",
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["df.info()\n", "df.isna().mean().sort_values(ascending=False)\n"],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "import matplotlib.pyplot as plt\n",
                    "df.groupby('日期')['PM2.5'].mean().plot(figsize=(9, 4), title='Daily PM2.5')\n",
                    "plt.show()\n",
                ],
            },
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python (.venv)", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.12"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    write(
        "13-VSCode代码/Notebook/EDA交互练习.ipynb",
        json.dumps(notebook, ensure_ascii=False, indent=2),
    )


def build_configs() -> None:
    write(
        "requirements.txt",
        """numpy>=2.0,<3
pandas>=2.2,<4
matplotlib>=3.9,<4
seaborn>=0.13,<1
scipy>=1.14,<2
statsmodels>=0.14,<1
scikit-learn>=1.5,<2
openpyxl>=3.1,<4
jupyter>=1.1,<2
ipykernel>=6.29,<8
""",
    )
    write(
        "requirements-pytorch.txt",
        """# 本项目已经安装CPU版PyTorch用于代码验证。
# 如需启用RTX 4060，请访问 https://pytorch.org/get-started/locally/
# 选择Windows + Pip + Python + 官方当前支持的CUDA构建，并运行选择器生成的命令。
# 不建议直接通过本文件猜测CUDA下载地址。
torch
""",
    )
    write(
        ".gitignore",
        """.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
tmp/
""",
    )
    settings = {
        "python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
        "python.terminal.activateEnvironment": True,
        "files.encoding": "utf8",
        "editor.formatOnSave": False,
        "jupyter.notebookFileRoot": "${workspaceFolder}",
        "terminal.integrated.env.windows": {
            "MPLCONFIGDIR": "${workspaceFolder}\\tmp\\.matplotlib"
        },
    }
    write(".vscode/settings.json", json.dumps(settings, ensure_ascii=False, indent=2))
    launch = {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "调试当前Python文件",
                "type": "debugpy",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "cwd": "${workspaceFolder}",
            },
            {
                "name": "运行模拟C题",
                "type": "debugpy",
                "request": "launch",
                "program": "${workspaceFolder}/13-VSCode代码/综合项目参考实现/run_all.py",
                "console": "integratedTerminal",
                "cwd": "${workspaceFolder}",
            },
        ],
    }
    write(".vscode/launch.json", json.dumps(launch, ensure_ascii=False, indent=2))
    write(
        "一键创建环境.ps1",
        r"""$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonLauncher = Get-Command py -ErrorAction SilentlyContinue
if ($pythonLauncher) {
    & py -3.12 -m venv (Join-Path $projectRoot ".venv")
} elseif (Test-Path -LiteralPath "C:\ProgramData\anaconda3\python.exe") {
    & "C:\ProgramData\anaconda3\python.exe" -m venv (Join-Path $projectRoot ".venv")
} else {
    throw "未找到py启动器或C:\ProgramData\anaconda3\python.exe，请在VS Code中先选择Python解释器。"
}
$venvPython = Join-Path $projectRoot ".venv\Scripts\python.exe"
& $venvPython -m pip install --upgrade pip
& $venvPython -m pip install -r (Join-Path $projectRoot "requirements.txt")
& $venvPython (Join-Path $projectRoot "13-VSCode代码\00-环境检查.py")
""",
    )
    write(
        "README.md",
        """# Python学习

这是面向全国大学生数学建模竞赛编程手的Python课程。Obsidian入口：

[[python学习/00-总导航与学习计划/Python数学建模学习总导航|Python数学建模学习总导航]]

## VS Code快速开始

1. 用VS Code打开整个`python学习`文件夹。
2. 按[[python学习/00-总导航与学习计划/VSCode与venv环境搭建|环境搭建]]创建`.venv`。
3. 选择`.venv/Scripts/python.exe`解释器。
4. 运行`13-VSCode代码/00-环境检查.py`。
5. 从每日计划当天的主题开始，示例代码亲手输入，不直接复制。

代码运行产生的结果放在`tmp`，可删除后重新生成；`12-示例数据`视为只读原始数据。
""",
    )


def build_course() -> None:
    for folder in [
        "00-总导航与学习计划", "01-Python基础", "02-函数文件与调试",
        "03-NumPy数值计算", "04-pandas数据处理", "05-数据可视化",
        "06-SciPy与优化", "07-统计与机器学习", "08-数学建模算法实现",
        "09-综合项目", "10-练习题", "11-参考答案", "12-示例数据",
        "13-VSCode代码",
    ]:
        (ROOT / folder).mkdir(parents=True, exist_ok=True)

    write("00-总导航与学习计划/Python数学建模学习总导航.md", navigation())
    write("00-总导航与学习计划/课程使用说明.md", course_usage())
    write("00-总导航与学习计划/VSCode与venv环境搭建.md", environment_note())
    write("00-总导航与学习计划/VSCode运行、调试与Notebook.md", vscode_note())
    write("00-总导航与学习计划/报错排查手册.md", troubleshooting_note())
    write("00-总导航与学习计划/2026-07-26至08-15每日学习计划.md", daily_plan())
    write("00-总导航与学习计划/学习进度看板.md", progress_board())
    write("00-总导航与学习计划/比赛编程手速查总表.md", cheat_sheet())

    for topic in TOPICS:
        write(f"{topic.folder}/{topic.filename}", render_topic(topic))
        if topic.code_file:
            script = (
                "# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。\n"
                + dedent(topic.example).strip()
                + "\n"
            )
            write(f"13-VSCode代码/{topic.code_file}", script)

    for folder, info in MODULE_EXERCISES.items():
        write(f"10-练习题/{folder}-练习题.md", render_exercise(folder, info))
        write(f"11-参考答案/{folder}-参考答案.md", render_answer(folder, info))
        write(
            f"13-VSCode代码/{folder}/模块综合参考.py",
            "# 完成独立尝试后再阅读本文件。\n" + dedent(info["answer"]).strip(),
        )

    write("09-综合项目/模拟C题-城市韧性评估预测与资源配置.md", capstone_problem())
    write("09-综合项目/模拟C题-完成指南与验收.md", capstone_guide())
    write("13-VSCode代码/00-环境检查.py", dedent(ENV_CHECK))
    for filename, script in TEMPLATE_SCRIPTS.items():
        write(f"13-VSCode代码/比赛模板/{filename}", dedent(script))
    write(
        "13-VSCode代码/比赛模板/README.md",
        """# 比赛模板

这些脚本是可运行的最小模板，不是万能答案。复制到新项目后修改数据路径、列名、指标方向、评价指标和验证方案。先运行环境检查，再按01—10选择需要的流程；PyTorch模板仅在数据量和验证结果支持时使用。
""",
    )
    write("13-VSCode代码/综合项目参考实现/common.py", dedent(CAPSTONE_COMMON))
    for filename, script in CAPSTONE_SCRIPTS.items():
        write(f"13-VSCode代码/综合项目参考实现/{filename}", dedent(script))
    write(
        "13-VSCode代码/综合项目参考实现/README.md",
        """# 模拟C题参考实现

至少独立工作4小时后再查看。运行：

```powershell
python 13-VSCode代码/综合项目参考实现/run_all.py
```

输出在`tmp/模拟C题输出`。参考实现只展示一条合理流程，不是唯一答案；清洗规则、权重、预测模型和优化收益定义都应在自己的报告中论证。
""",
    )
    build_datasets()
    build_notebook()
    build_configs()


if __name__ == "__main__":
    build_course()
    print(f"课程已生成：{ROOT}")
    print(f"主题笔记：{len(TOPICS)}")
    print(f"模块练习：{len(MODULE_EXERCISES)}")

---
title: ML 所需线性代数知识（完整路线图） - 飞书云文档
source: https://waytoagi.feishu.cn/wiki/UTSCw2RD5i9W55kMiLZcM6HJnZF
author:
published:
created: 2026-06-06
description: ML 所需线性代数知识
tags:
  - clippings
  - 高等代数
---
## 飞书云文档

🌈

WaytoAGI ｜ 通往AGI之路

互联网公开

问问知识库

目录

- [AI / ML 所需线性代数知识（完整路线图）](#EPPAdRVsRo8d66xjsNMcYzAznJb)
- [为什么偏偏是线性代数？](#doxcnUtoaIeUzddKWdh0XmBAwYd)
- [Phase 1：绝对基础](#doxcn9gUgyLBKr0LUWt0sgAMucc)
- [1\. 标量、向量、矩阵、张量](#doxcnZMb3TLBg6wQ9YCeadgOZFb)
- [2\. 向量运算](#doxcn0q1Wp45akPYfi89crlSNJb)
- [3\. 点积](#doxcnrFjHsUtS2EjhLOnOEtnHVe)
- [4\. 矩阵运算](#doxcnreVMTjG8e0zCn9zaXnVzHf)
- [Phase 2：你真正会用到的构件](#doxcnNIMhU4ZzYDVpA1tXzzMFjd)
- [5\. 特殊矩阵](#doxcnwvUPCOuTAwtzakqsjf5kCd)
- [6\. 矩阵逆](#doxcnFqluiwkU5Eh7xnLI2akatc)
- [7\. 线性无关与秩](#doxcnFEgTR5NCEfeNsOoLcOAUDh)
- [8\. Span、Basis 和 Subspaces](#doxcnA87vtn6ql3D0zXXxuU8Tsc)
- [Phase 3：ML 里真正重要的部分](#doxcnpePt6b53jOOuuXdkvjdbSh)
- [9\. 特征值与特征向量](#doxcn7eg2q2OE51pXRwwtHvRysd)
- [10\. 奇异值分解（SVD）](#doxcnujPy6QDhgXLtwBB6UaE9Sh)
- [11\. 矩阵分解](#doxcnu3NF1JGwCyLYTaXvEkD4Wd)
- [12\. 再看 Norm](#doxcnJOytGDZhfLEXnHclb9DZmc)
- [Phase 4：微积分与线性代数之间的桥梁](#doxcn0Szj7oQTtxXwuCxH3HXaFe)
- [13\. 梯度与 Jacobian](#doxcnH4ndObkFF5ElzJO1U1P7yc)
- [14\. Hessian 矩阵](#doxcnJCq1o8L4e1JsPmSp9cC3ph)
- [15\. 矩阵形式的链式法则](#doxcnJFzu9SHX2G77PsXZgw4fdg)
- [Phase 5：进阶主题（按需学习）](#doxcnLLrL0S0InpRAczp7NPS25b)
- [16\. 张量运算](#doxcnHt3U01zE5iwsUO6sYRwRcc)
- [17\. 矩阵微积分恒等式](#doxcnzNsx5vXBKt0Lz8spd6WEfc)
- [18\. 正定矩阵](#doxcn88D4Dmyx7for6duQl4k8Gh)
- [19\. 数值线性代数](#doxcnZfXDZcKZ2RfZnumYRF3MHd)
- [Phase 6：它们究竟在 ML 的哪里出现](#doxcnIoCpZJqo9lj8Bi0juBzZEc)
- [到底该怎么学](#doxcnnobF2STIdzr4D50xf5f8Ke)
- [真正值得看的资源](#doxcnN9p2yypf7jkEsafAruVyvh)
- [最后的建议](#doxcn2VgXIH6ZLJlvr9IDKMyc9e)

在开始罗列知识点之前，我先解释一下，为什么这门课在 ML 里这么重要。

机器学习里的一切，本质上都是数字。图像是数字网格。文本在 tokenization 之后会变成数字。音频则是一串按时间采样得到的数字。当你把所有数据都转成数字之后，你就需要一套方法来：

1.

高效存储这些数字

2.

对它们执行快速运算

3.

把它们从一种形式变换成另一种形式

线性代数本身就是完成这三件事的语言。神经网络？本质上就是矩阵乘法，再撒上一点非线性函数。主成分分析？本质是特征向量。推荐系统？本质是矩阵分解。词向量？本质是高维空间中的向量。

你绕不开它。

但你完全可以理解它。

继续往下。

Phase 1：绝对基础

这是所有人都应该开始的地方，就算你觉得自己已经会了也一样。相信我，回来重新过一遍。

1\. 标量、向量、矩阵、张量

附件不支持打印

![飞书文档 - 图片](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/v2/cover/VfFhbhUeOo0TNdxq7mYcofTPn8g/?fallback_source=1&height=1280&mount_node_token=BpAhd41WFoIr5zxL6ENcEYeGnpc&mount_point=docx_image&policy=equal&width=1280)

先从这里开始，理解它们的层级关系。

•

标量 就是一个数字，比如 5 或 3.14。

•

向量 是一串数字，比如 \[2, 4, 7\]。

•

矩阵 是一个二维数字网格，本质上就是行和列。

•

张量 是更一般化的形式，可以是 3D、4D 甚至更高维。在深度学习里，一批图像通常就是 4D 张量（batch、channel、height、width）。

为什么这很重要：你写的每一个 PyTorch 或 TensorFlow 程序都会用到这些。如果你不知道自己数据的 shape，你会在 debug 上浪费大量时间。

2\. 向量运算

你要学会：

•

两个向量相加

•

向量与标量相乘

•

求向量的长度，也就是 magnitude 或 norm

•

理解它的几何意义，也就是向量在空间中指向某个方向

norm 这个概念会一遍又一遍出现。L1 norm、L2 norm，它们会出现在 regularization 和 loss function 里。

3\. 点积

这一项非常关键。点积告诉你两个向量有多相似。它是 cosine similarity 的基础，而 cosine similarity 从搜索引擎、推荐系统，到 Transformer 里的 attention，几乎无处不在。

练到你闭着眼都能算点积。

4\. 矩阵运算

•

矩阵加法

•

矩阵上的标量乘法

•

矩阵乘法（这一项最关键）

•

矩阵转置

矩阵乘法不是逐元素乘法。这里会卡住非常多初学者。你应该在这部分多花点时间。真正理解为什么维度必须匹配，也就是为什么 (m x n) 乘 (n x p) 才能得到 (m x p)。

评论（0）

跳转至首条评论

0 字

- 帮助中心

- 效率指南
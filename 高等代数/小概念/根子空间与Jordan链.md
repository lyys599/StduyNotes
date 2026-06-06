---
title: 根子空间与Jordan链
subtitle: 严格依据北大版《高等代数》第六版体系
date: 2026-06-06
textbook: 高等代数（第六版），北京大学数学系前代数小组编，王萼芳等修订
tags:
  - 不变子空间
  - 根子空间
  - Jordan标准型
  - 概念原子
  - 循环不变子空间
summary: 由于几何重数小于代数重数，无法对角化，可以通过根子空间提供足够的广义特征向量，使得任何向量都可以化为Jordan标准型。
---

# 根子空间与Jordan链：从空间分解到标准型

> **核心定位**：根子空间是Jordan链的"容器"，Jordan链是根子空间的"骨架"。根子空间提供足够的"广义特征向量"（维数恒等于代数重数），Jordan链从中提取出循环结构，每条链对应一个Jordan块。二者的结合，使得任何方阵都能化为Jordan标准型。

---

## 一、概念图谱

```
方阵 A ∈ ℂ^{n×n}
    │
    ▼
特征值 λ₁, λ₂, ..., λₛ（代数重数 m₁, m₂, ..., mₛ，Σmᵢ = n）
    │
    ▼
空间分解：V = G_{λ₁} ⊕ G_{λ₂} ⊕ ... ⊕ G_{λₛ}
                │           │
                ▼           ▼
            根子空间 G_{λ₁}    根子空间 G_{λ₂}
                │
                ├── Jordan链1 ──→ J(λ₁, k₁)  Jordan块
                │       ξ₁
                │       (A-λ₁E)ξ₁
                │       (A-λ₁E)²ξ₁
                │       ...
                │
                ├── Jordan链2 ──→ J(λ₁, k₂)
                │       ...
                │
                └── ...
```

**三个层次**：

| 层次 | 对象 | 分解方式 | 维度信息 |
|:---:|:---:|:---:|:---:|
| 第一层 | 全空间 $V$ | $V = \bigoplus_{i=1}^{s} G_{\lambda_i}$ | $\dim G_{\lambda_i} = m_i$ |
| 第二层 | 根子空间 $G_\lambda$ | $G_\lambda = \bigoplus_{j=1}^{t} C_j$ | $\dim C_j = k_j$，$\sum k_j = m$ |
| 第三层 | 循环子空间 $C_j$ | $C_j = \text{span}\{\text{Jordan链}\}$ | $k_j$ = 链长 = Jordan块阶数 |

---

## 二、根子空间：Jordan链的容器

### 2.1 定义

$$G_\lambda = \left\{\alpha \in V \,\middle|\, (\mathscr{A} - \lambda\mathscr{E})^k \alpha = 0 \text{（某 } k \geq 1\text{）}\right\}$$

**核心性质**：

| 性质 | 内容 |
|:---:|:---|
| 子空间 | $G_\lambda$ 是 $V$ 的子空间 |
| 不变性 | $\mathscr{A}(G_\lambda) \subseteq G_\lambda$ |
| 维数 | $\dim G_\lambda = \text{代数重数}(\lambda) = m$ |
| 包含 | $V_\lambda \subseteq G_\lambda$，且 $G_\lambda = \ker(\mathscr{A} - \lambda\mathscr{E})^m$ |

**关键理解**：根子空间比特征子空间"大"，大到刚好能容纳所有Jordan链。

### 2.2 递增链

$$\{0\} \subsetneq V_\lambda = \ker(\mathscr{A}-\lambda\mathscr{E}) \subseteq \ker(\mathscr{A}-\lambda\mathscr{E})^2 \subseteq \cdots \subseteq \ker(\mathscr{A}-\lambda\mathscr{E})^m = G_\lambda$$

$$\dim V_\lambda = g, \quad \dim G_\lambda = m$$

| 维数差 | 意义 |
|:---:|:---|
| $\dim G_\lambda - \dim V_\lambda = m - g$ | 需要"广义特征向量"补上的缺口 |
| $\dim V_\lambda = g$ | 线性无关特征向量个数（= Jordan块数）|
| $\dim G_\lambda = m$ | 代数重数（= Jordan链总长）|

---

## 三、Jordan链：根子空间的骨架

### 3.1 定义

设 $\lambda$ 是 $\mathscr{A}$ 的特征值。一组向量 $\{\xi_1, \xi_2, \ldots, \xi_k\}$ 称为 **属于 $\lambda$ 的Jordan链**（长度为 $k$），如果：

$$\begin{cases} \xi_1 \neq 0, & (\mathscr{A} - \lambda\mathscr{E})\xi_1 = 0 \\ \xi_2, & (\mathscr{A} - \lambda\mathscr{E})\xi_2 = \xi_1 \\ \xi_3, & (\mathscr{A} - \lambda\mathscr{E})\xi_3 = \xi_2 \\ \vdots & \\ \xi_k, & (\mathscr{A} - \lambda\mathscr{E})\xi_k = \xi_{k-1} \end{cases}$$

**统一写成**：

$$(\mathscr{A} - \lambda\mathscr{E})\xi_1 = 0, \quad (\mathscr{A} - \lambda\mathscr{E})\xi_j = \xi_{j-1} \; (j \geq 2)$$

### 3.2 Jordan链的结构

| 向量 | 条件 | 称呼 | 所在层 |
|:---:|:---:|:---:|:---:|
| $\xi_1$ | $(\mathscr{A}-\lambda\mathscr{E})\xi_1 = 0$ | **特征向量**（真正的）| $\ker(\mathscr{A}-\lambda\mathscr{E})$ |
| $\xi_2$ | $(\mathscr{A}-\lambda\mathscr{E})\xi_2 = \xi_1$ | **广义特征向量**（1阶）| $\ker(\mathscr{A}-\lambda\mathscr{E})^2 \setminus \ker(\mathscr{A}-\lambda\mathscr{E})$ |
| $\xi_3$ | $(\mathscr{A}-\lambda\mathscr{E})\xi_3 = \xi_2$ | **广义特征向量**（2阶）| $\ker(\mathscr{A}-\lambda\mathscr{E})^3 \setminus \ker(\mathscr{A}-\lambda\mathscr{E})^2$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
| $\xi_k$ | $(\mathscr{A}-\lambda\mathscr{E})\xi_k = \xi_{k-1}$ | **广义特征向量**（$k-1$阶）| $\ker(\mathscr{A}-\lambda\mathscr{E})^k \setminus \ker(\mathscr{A}-\lambda\mathscr{E})^{k-1}$ |

**直观**：Jordan链像一条"逆流而上"的链——从真正的特征向量出发，每一步"解方程"$(\mathscr{A}-\lambda\mathscr{E})\xi_j = \xi_{j-1}$，找到越来越"广义"的向量。

### 3.3 Jordan链张成循环子空间

由一条长度为 $k$ 的Jordan链 $\{\xi_1, \ldots, \xi_k\}$ 张成的子空间：

$$C = \text{span}\{\xi_1, \xi_2, \ldots, \xi_k\}$$

称为 **循环不变子空间**。$\mathscr{A}$ 在 $C$ 上的作用：

$$\begin{aligned} \mathscr{A}\xi_1 &= \lambda\xi_1 \\ \mathscr{A}\xi_2 &= \xi_1 + \lambda\xi_2 \\ \mathscr{A}\xi_3 &= \xi_2 + \lambda\xi_3 \\ &\vdots \\ \mathscr{A}\xi_k &= \xi_{k-1} + \lambda\xi_k \end{aligned}$$

### 3.4 Jordan链对应的Jordan块

在基 $\{\xi_1, \xi_2, \ldots, \xi_k\}$ 下，$\mathscr{A}|_C$ 的矩阵为：

$$J(\lambda, k) = \begin{pmatrix} \lambda & 1 & & & \\ & \lambda & 1 & & \\ & & \lambda & \ddots & \\ & & & \ddots & 1 \\ & & & & \lambda \end{pmatrix}_{k \times k}$$

| 链长 $k$ | Jordan块 $J(\lambda, k)$ | 对应初等因子 |
|:---:|:---:|:---:|
| 1 | $(\lambda)$ | $(x - \lambda)$ |
| 2 | $\begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}$ | $(x - \lambda)^2$ |
| 3 | $\begin{pmatrix} \lambda & 1 & 0 \\ 0 & \lambda & 1 \\ 0 & 0 & \lambda \end{pmatrix}$ | $(x - \lambda)^3$ |
| $k$ | 上三角，对角 $\lambda$，上次对角 1 | $(x - \lambda)^k$ |

---

## 四、核心定理：根子空间 = Jordan链的直和

### 定理（根子空间的Jordan分解）

设 $\lambda$ 是 $\mathscr{A}$ 的特征值，代数重数为 $m$，几何重数为 $g$。则：

$$G_\lambda = C_1 \oplus C_2 \oplus \cdots \oplus C_g$$

其中每个 $C_j$ 是由一条Jordan链张成的循环子空间。

**关键数量关系**：

| 量 | 数值 | 来源 |
|:---:|:---:|:---|
| Jordan链的条数 | $g$（= 几何重数）| 线性无关特征向量个数 |
| 各链长度之和 | $m$（= 代数重数）| $\sum k_j = m$ |
| 最长链的长度 | $m(\lambda)$ 中 $(x-\lambda)$ 的幂次 | 最大Jordan块阶数 |

> **口诀**：链数 = 几何重数，链长之和 = 代数重数。

---

## 五、Jordan链的构造算法

### 算法：在根子空间 $G_\lambda$ 内找全部Jordan链

**输入**：特征值 $\lambda$，代数重数 $m$，$(A - \lambda E)^k$ 对 $k = 1, 2, \ldots, m$

**Step 1**：计算维数序列

$$d_k = \dim \ker(A - \lambda E)^k, \quad k = 0, 1, 2, \ldots, m$$

（约定 $d_0 = 0$）。序列满足 $0 = d_0 < d_1 = g \leq d_2 \leq \cdots \leq d_m = m$。

**Step 2**：计算各级"新增"向量数

$$n_k = d_k - d_{k-1} = \text{第 } k \text{ 层新增的广义特征向量个数}$$

- $n_1 = g$（真正的特征向量）
- $n_k$ = 第 $k$ 阶广义特征向量个数

**Step 3**：确定Jordan块结构

从最高层往低层"降下"：

| 层级 | 操作 |
|:---:|:---|
| 第 $m$ 层 | 在 $\ker(A-\lambda E)^m \setminus \ker(A-\lambda E)^{m-1}$ 中取 $n_m$ 个向量，各起一条新链 |
| 第 $m-1$ 层 | 用 $(A-\lambda E)$ 作用第 $m$ 层向量，得到第 $m-1$ 层终点；若 $n_{m-1} > $ 降下数，再补新链 |
| ... | 逐层下降 |
| 第 1 层 | 所有链的终点 = 特征向量，共 $g$ 个 |

**Step 4**：写出全部Jordan链

每条链 $\{\xi_1, \xi_2, \ldots, \xi_k\}$ 对应一个Jordan块 $J(\lambda, k)$。

---

## 六、完整计算示例

### 例题

求 $A = \begin{pmatrix} 3 & 1 & 0 & 0 \\ 0 & 3 & 0 & 0 \\ 0 & 0 & 3 & 1 \\ 0 & 0 & 0 & 3 \end{pmatrix}$ 的根子空间分解和Jordan链。

### 解答

**Step 1：特征值**

$A$ 是上三角分块矩阵，$A = \begin{pmatrix} J(3,2) & 0 \\ 0 & J(3,2) \end{pmatrix}$。特征值 $\lambda = 3$（代数重数 $m = 4$）。

**Step 2：计算 $(A - 3E)^k$**

$$A - 3E = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

$$(A - 3E)^2 = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

**Step 3：维数序列**

| $k$ | $(A-3E)^k$ | $r((A-3E)^k)$ | $d_k = 4 - r$ |
|:---:|:---:|:---:|:---:|
| 0 | $E$ | 4 | $d_0 = 0$（约定）|
| 1 | 见上 | 2 | $d_1 = 2$ |
| 2 | 零矩阵 | 0 | $d_2 = 4$ |

**Step 4：各级新增向量数**

- $n_1 = d_1 - d_0 = 2 - 0 = 2$（2个特征向量）
- $n_2 = d_2 - d_1 = 4 - 2 = 2$（2个2阶广义特征向量）

**Step 5：找Jordan链**

从第2层（最高层）开始：

**链1**：
- 第2层：取 $\xi_2^{(1)} = (0, 1, 0, 0)' \in \ker(A-3E)^2 \setminus \ker(A-3E)$（$e_2$方向）
- 第1层：$(A-3E)\xi_2^{(1)} = (1, 0, 0, 0)' = \xi_1^{(1)}$
- Jordan链：$\{(1,0,0,0)', (0,1,0,0)'\}$，长度2

**链2**：
- 第2层：取 $\xi_2^{(2)} = (0, 0, 0, 1)' \in \ker(A-3E)^2 \setminus \ker(A-3E)$（$e_4$方向）
- 第1层：$(A-3E)\xi_2^{(2)} = (0, 0, 1, 0)' = \xi_1^{(2)}$
- Jordan链：$\{(0,0,1,0)', (0,0,0,1)'\}$，长度2

**Step 6：验证**

$A\xi_1^{(1)} = 3\xi_1^{(1)}$ ✓，$A\xi_2^{(1)} = \xi_1^{(1)} + 3\xi_2^{(1)}$ ✓

$A\xi_1^{(2)} = 3\xi_1^{(2)}$ ✓，$A\xi_2^{(2)} = \xi_1^{(2)} + 3\xi_2^{(2)}$ ✓

**结论**：

$$G_3 = \mathbb{R}^4 = C_1 \oplus C_2$$

- $C_1 = \text{span}\{(1,0,0,0)', (0,1,0,0)'\}$，对应 $J(3, 2)$
- $C_2 = \text{span}\{(0,0,1,0)', (0,0,0,1)'\}$，对应 $J(3, 2)$

Jordan标准型：$A \sim \begin{pmatrix} J(3,2) & 0 \\ 0 & J(3,2) \end{pmatrix}$（与原矩阵一致）。

---

## 七、数量关系总结

对单一特征值 $\lambda$（代数重数 $m$，几何重数 $g$）：

```
根子空间 G_λ（dim = m）
    │
    ├── Jordan链1：长度 k₁ → J(λ, k₁)
    ├── Jordan链2：长度 k₂ → J(λ, k₂)
    │   ...
    └── Jordan链g：长度 k_g → J(λ, k_g)

约束条件：
    k₁ + k₂ + ... + k_g = m  （链长之和 = 代数重数）
    max(k₁, ..., k_g) = m(λ)中(x-λ)的幂次
    g = 几何重数 = Jordan块数 = 线性无关特征向量数
```

**维数公式**：

$$\dim G_\lambda = \sum_{j=1}^{g} \dim C_j = \sum_{j=1}^{g} k_j = m$$

---

## 八、常见误区辨析

| 误区 | 正确理解 |
|:---|:---|
| **"每条Jordan链长度相同"** | 不同链长度可以不同。如一个链长3，一个链长1 |
| **"Jordan链从特征向量出发"** | 构造时从**外层**（最高阶广义特征向量）往内找更方便 |
| **"根子空间 = 一条Jordan链"** | 根子空间是 **多条** Jordan链的直和 |
| **"(A-λE)在G_λ上是零变换"** | 只在 $V_\lambda$ 上是零。在 $G_\lambda$ 上 $(A-\lambda E)$ 是 **幂零变换** |
| **"Jordan链唯一"** | Jordan块结构唯一，但链的具体选取 **不唯一** |

---

## 九、一句话总结

> **根子空间**提供足够的广义特征向量（维数 = 代数重数），**Jordan链**从中提取出循环结构（每条链对应一个Jordan块）。二者的直和分解 $G_\lambda = \bigoplus C_j$ 使得任何方阵都能化为Jordan标准型——这是线性代数中最深刻的结构定理之一。

---

*本文严格依据北京大学数学系前代数小组编、王萼芳等修订《高等代数》第六版（高等教育出版社）的章节体系和符号约定编写。*

# 一维随机变量及其分布

* 泊松定理
* 分布函数
* 离散型随机变量
* 连续型随机变量
* 概率分布
* 泊松分布
* 二项分布
* 概率密度

## 随机变量

> 随机事件是从`静态的观点`来研究随机现象, 随机变量是从`动态的观点`来研究随机现象
> 随机变量的实质 是一个 `实值单值函数`

设随机试验 E 的样本空间为 $\Omega = \{ \omega \}$, 如果对每一个 $\omega \in \Omega$, 都有唯一的实数 $X\{\omega \}$ 与之对应, 并且对任意实数 $x$, $\{\omega | X(\omega), \omega \in \Omega \}$ 是随机事件, 则称定义在 $\Omega$ 上的实值单值函数 $X(\omega)$为随机变量.

## 分布函数

> 使用微积分作为求解工具

$$
F(x) = P ( X \leq x ) ( -\infty < x < +\infty)
$$

X 为样本值, x 为统计值

## 离散型随机变量 及其 概率分布

离散随机变量的 `正概率点`;

若随机变量 $X$ 只可能取有限个或可列无穷个值 $x_1, x_2, x_3, ...$ 则称 $X$ 为 `离散随机变量`, 称

$$
{p_i} = {P\{ X = x_i \}, i = 1,2,3... }
$$

为 $X$ 的`分布列`, `分布律` 或 `概率分布`, 记作 $X \sim p_i$

概率分布常用的表示方式有

| X | $x_1$ | $x_2$ | $x_3$ | ... |
| :----: | :----: | :----: | :----: | :----: |
| P | $p_1$ | $p_2$ | $p_3$ | ... |
或

$$
X \sim  \left (
    \begin{matrix}
    x1 \quad x2 \quad x3 \quad ... \\
    p_1 \quad p_2 \quad p_3 \quad ... \\
    \end{matrix}
\right )
$$

## 连续性随机变量 及其 概率密度

>`分布函数` 的 `概率密度`

如果随机变量 X 的分布函数可以表示为

$$
F(x) = \int_{B}{f(x)}dx,
$$

## 泊松定理

`泊松分布` $P(\lambda)$ 可以用来近似的表示`二项分布` $B(n, \ p)$

## 分布函数的概念和性质

> 分布函数 完整地描述了 随机变量 的概率规律性
>> 分布函数是事件的概率, 所以 $0 \le F(x) \le 1$, $F(x)$ 是一个有界函数

1. 概念

2. 性质
    * 单调不减
    * 右连续
    * $F(-\infty) = \lim_{x\to-\infty}{F(x)} = 0$ , $F(+\infty) = \lim_{x\to+\infty}{F(x)} = 1$

> 当分布函数是不连续的分段函数时,为保证其右连续性,自变量$x$的分段小区间除第一个小区间外,其余都应是左闭右开的

3. 应用

## 常见的随机变量分布类型

离散型:

* 二项分布 $B(n, p)$

    $$
    P(X = k) = \left (
        \begin{matrix}
        n \\
        k \\
        \end {matrix}
    \right )p^k(1-p)^{n-k}, \quad k = 0,1,2,\cdots,n
    $$

    X 表示 n重 Beronulli试验 中 事件A 发生的次数, $\ \Omega (X) = \{ 0,1,2, \cdots,n \}$; 称作: 随机变量 $X$ 服从参数为 $n, p$ 的 `二项分布`; 记作: $X \sim B(n, p), \ 0 \le p \le 1$

* 0-1 分布 $B(1, p)$

    $$
    P(X = k) = \left (
        \begin{matrix}
        1 \\
        k \\
        \end {matrix}
    \right )p^k(1-p)^{1-k}, \quad k = 0,1
    $$

    X 表示 1次 Beronulli 试验中 事件A 发生的事件, $\ \Omega (X) = \{ 0,1 \}$;

* 几何分布 $G(p)$

    $$
    P(X=k) = (1-p)^{k-1}p, \quad k = 1,2,\cdots
    $$

    $X$ 表示 在$n$ 重 Beronulli试验 中，记每次试验中事件$A$发生的概率为$p$，试验进行到 事件$A$ 出现时 或 $n$次试验完成时停止，此时所进行的试验次数 服从 几何分布

* 超几何分布 $H(n, M, N)$

    $$
    P(X=k) = \frac{C_M^kC_{N-M}^{n-k}}{C_N^n}, \quad k = 1,2, \cdots, n
    $$

    $X$ 表示 常见的产品抽样检查试验中, 由 $N$ 个产品组成的总体, 其中含有 $M$ 个不合格品, 从中随机不放回地抽取 $n$ 个, 发现 $k$ 个不合格产品的事件, 此时随机变量 $X$ 服从 `超几何分布`, , 记作 $X \sim H(n, M, N)$

* 泊松分布 $P(\lambda)$

    $$
    P(X = k) = \frac {\lambda ^ k}{ k! }e^{-\lambda}, \quad k = 0,1,\cdots
    $$

    参数 $\lambda$ 表示单位时间(或面积)内随机事件发生的平均次数

连续型:

* 均匀分布 $U(a,b)$

    $$
    f(x) = \left (
          \begin{gathered}
            \frac {1}{b-a}, \quad a \le x \le b\\
            0, \quad else
          \end{gathered}
     \right )
    $$

    > $P\{X > \frac{a+b}{2}\} = \frac{1}{2}, \quad P\{X \le \frac{a+b}{2}\} = \frac{1}{2}$

* 指数分布 $E(\lambda)$

    概率密度:

    $$
    f(x) = \left (
            \begin{gathered}
                \lambda e^{-\lambda x}, \quad x \ge 0 \\
                0, \quad else
            \end{gathered}
        \right )
    $$

    概率函数:

    $$
    F(x) = 1 - e^{-\lambda x}, \quad x \ge 0
    $$

    > 指数分布的无记忆性

* 正态分布 $N(\mu, \sigma^2)$

    $$
    f(x) = \frac {1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}, \quad
    \begin{gathered}
        -\infty \le x \le +\infty \\
        -\infty \le \mu \le +\infty \\
        \sigma \ge 0
    \end{gathered}
    $$

* 标准正态分布 $N(0,1)$


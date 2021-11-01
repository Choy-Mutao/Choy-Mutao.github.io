# 一元函数积分学的概念和计算

## 概念

不定积分(原函数)

$$
F(x) = \int{f(x)}{dx} + C
$$

反常积分

$$
\int_{-\infty}^{+\infty}{f(x)}{dx} (收敛) => \lim_{x \to \infty} = 0
$$

不定积分的存在性

$$
\begin{array}{lr}
1.\ 连续函数f(x)必有原函数F(x) \\
2.\ 第一类间断点和无穷间断点的函数在\textbf{包含}该断点区间内没有原函数
\end{array}
$$

> 不同的方法下,得到的不定积分可能不一样

定积分(黎曼积分)

$$
\int_a^b {f(x)} =\lim_{\lambda \to 0} \sum_{k=1}^{n} {f(x_k)}{\Delta{x_k}}, \lambda = \max{\{\Delta{x_k}\}} \\
= \lim_{n \to \infty} \sum_{k=1}^{n} {f(x + k\frac{b-a}{n})}{\frac{b-a}{n}}
$$

定积分存在定理

$$
\begin{array}{lr}
1.\ f(x) 在 [a,b] 上连续, \\
2.\ f(x) 在 [a,b] 上有界, \\
3.\ f(x) 在 [a,b] 上单调, \\
\end{array}
$$

> 定积分和不定积分的区别在于他们的定理关系

定积分的性质

1. 求区间长度
2. 积分的线性性质
3. 积分的可加可拆性
4. 积分的保号性
5. 估值定理
6. 中值定理

变限积分

$$
\Phi(x) = \int_{a(x)}^{b(x)}{f(t)}{dt}
$$

变限积分的性质

$$
\begin{array}{lr}
1.\ 可积则连续 \\
2.\ 连续则可导
\end{array}
$$

变限几分的求导公式

$$
F(x) = \int_{\varphi_1}^{\varphi_2}{f(t)}{dt}\\
F'(x) = f[\varphi_2(x)]\varphi'_2(x) - f[\varphi_1(x)]\varphi'_1(x)
$$

## 积分的存在性

原函数(不定积分)存在性

定积分存在性

1. 定积分存在的充分条件

2. 定积分存在的必要条件

    a. 积分区间有限
    b. 被积函数有界

## 反常积分的概念和敛散性

---

## 一元函数的积分计算方法

1. 凑微分
$$
\int{f[g(x)]g'(x)}{dx} = \int{f[g(x)]}{d[g(x)]}
$$

2. 换元法
$$
\int{f(x)}{dx} \xlongequal{x=g(u)} \int{f[g(u)]}{d[g(u)]} = \int{f[g(u)]g'(u)}{du}
$$

3. 分部积分法
$$
\int {u}{dv} = uv - \int{v}{du} \\
\int {uv^{(n+1)}}{dx} = \sum_{i=0}^{n}{(-1)^{i}}{u^{(i)}}{v^{(n-i)}} + (-1^{(n+1)})\int{u^{(n+1)}v}{dx}
$$

4. 有理函数的积分

## 定积分的计算

1. 定积分的换元法
$$
\int_{a}^{b}{f(x)}{dx} \xlongequal{x=\varphi(t)} \int_{\alpha}^{\beta}{f[\varphi(t)]}{d[\varphi(t)]} = \int_{\alpha}^{\beta}{f[\varphi(t)]\varphi'(t)}{dt}
$$
2. 定积分的分部积分法
$$
\int_{a}^{b}{uv'}{dx} = uv|_a^b - \int_{a}^{b}{vu'}{dx}
$$

## 推导定理

1. 函数连续则原函数可导
2. 函数可积,则变限积分连续
3. 连续的奇函数的一切原函数都是偶函数
4. 连续的偶函数的一个原函数是奇函数

## 区间再现公式

$$
\int_{a}^{b}{f(x)}{dx} = \int_{a}^{b}{f(a+b-x)}{dx}
$$

## 特殊的三角函数定积分

$$
\int_{0}^{\frac{\pi}{2}} {\sin^n{x}} = \int_{0}^{\frac{\pi}{2}} {\cos^n{x}} = 
\left \{
    \begin{array}{lr}
        {\frac{n-1}{n}} \cdot {\frac{n-3}{n-2}} \cdot \cdots {\frac{3}{2}} \cdot {1} \\
        {\frac{n-1}{n}} \cdot {\frac{n-3}{n-2}} \cdot \cdots {\frac{1}{2}} \cdot {\frac{\pi}{2}}
    \end{array}
\right.
$$

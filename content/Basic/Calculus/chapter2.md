# 极限和连续

## 极限的语义分析证明

$\varepsilon-\delta(N)$语言

## 数列极限 & 函数极限

## 极限的定义

## 极限的性质

1. 唯一性

   $\lim \limits_{x \to x_0} f(x) = A \Leftrightarrow f(x_0 - 0) = f(x_0 + 0) = A$

2. 有界性

   若极限存在，则函数 $f(x)$ 在点 $x_0$ 充分小的去心领域内 有界;

   若函数 $f(x)$ 在点 $x_0$ 充分小的去心领域内 无界, 则其极限一定不存在;

3. 保号性
   
   在极限值附近的值具有和极限一致的符号

## 无穷小的性质

1. $\lim \limits_{x \to x_0} f(x) = A \Leftrightarrow f(x) = A + a(x), \lim \limits_{x \to x_0} a(x) =0$
2. $if \ (x \to x_0) \ and \ (|f(x)| \le M, g(x) \to 0 ) \rightarrow \lim \limits_{x \to x_0} f(x)g(x) = 0$
3. 当 $x \to x_0$ 时,有限个无穷小的和为无穷小， 有限个无穷小的乘积为无穷小
4. $\lim \limits_{x \to x_0} a(x) = 0 \Leftrightarrow \lim \limits_{x \to x_0} |a(x)| = 0$
5. $\lim \limits_{x \to x_0} \frac{\beta(x)}{\alpha(x)} = a, a \ne \infty, \lim \limits_{x \to x_0} \alpha(x) = 0 \Rightarrow \lim \limits_{x \to x_0} \beta(x) = 0$
   - $\lim \limits_{x \to x_0} \frac{\beta(x)}{\alpha(x)} = a, a \ne 0, \lim \limits_{x \to x_0} \beta(x) = 0 \Rightarrow \lim \limits_{x \to x_0} \alpha(x) = 0$

## 无穷小的阶数

## 等价无穷小 & 同阶无穷小 & 高阶无穷小

$\alpha(x) \ne 0, \beta(x) \ne 0, \lim \limits_{x \to x_0} \alpha(x) = 0, \lim \limits_{x \to x_0} \beta(x) = 0$

1. $\lim \limits_{x \to x_0} \alpha(x)= 0, \lim \limits_{x \to x_0} \frac{\beta(x)}{\alpha(x)} = 1 \Leftrightarrow \alpha(x)$ 和 $\beta(x)$ 互为等价无穷小

2. $\lim \limits_{x \to x_0} \alpha(x)= 0, \lim \limits_{x \to x_0} \frac{\beta(x)}{\alpha(x)} = a, a \ne 0 \ and \ a \ne \infty \Leftrightarrow \alpha(x)$ 和 $\beta(x)$ 互为同阶无穷小;

3. $\lim \limits_{x \to x_0} \alpha(x)= 0, \lim \limits_{x \to x_0} \frac{\beta(x)}{\alpha(x)} = 0 \Leftrightarrow \beta(x)$ 是 $\alpha(x)$ 的高阶无穷小；
4. $\lim \limits_{x \to x_0} \alpha(x)= 0, \lim \limits_{x \to x_0} \frac{\beta(x)}{\alpha(x)} = \infty \Leftrightarrow \alpha(x)$ 是 $\beta(x)$ 的高阶无穷小；

## 常用的等价无穷小`(乘除用等价)`

> `无穷小比较` 是把各类的函数都统一到 幂函数类 的 同一种结构 进行比较

> TIPS: 使用条件：在自变量的同一变化过程 $\ x \to x_0$ 中 $\alpha(x) \to 0$ 且 $\beta(x) \to 0$

$$
\sin(kx) \sim kx, \quad \arcsin(kx) \sim kx, k \ne 0
$$

$$
\tan(kx) \sim kx, \quad \arctan(kx) \sim kx, k \ne 0
$$

$$
e^{kx} - 1 \sim kx, \quad a^{kx} - 1 \sim kx \ln {a}, a \ne 0, a \ne 1
$$

$$
1 - \cos(x) \sim \frac{1}{2}x^2, \quad \ln(kx + 1) \sim kx
$$

$$
(1 + x)^{\lambda}-1\sim \lambda x, \quad x+x^{1+\lambda} \sim x, \lambda \ge 0
$$

## 常用的泰勒公式`(加减用泰勒)`

$$
\sin(x) = {x - \frac{x^3}{3!} + \omicron(x^3)} \ , \quad \cos(x) = {1 - \frac{x^2}{2!} + \frac{x^3}{3!} + \omicron(x^4)}
$$

$$
\arcsin(x) = {x + \frac{x^3}{3!} + \omicron(x^3)} \ ,
$$

$$
\tan(x) = {x + \frac{x^3}{3} + \omicron(x^3)} \ , \quad \arctan(x) = {x - \frac{x^3}{3} + \omicron(x^3)}
$$

$$
\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} + \omicron(x^3) \ , \quad e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \omicron(x^3)
$$

$$
(1 + x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha -1)}{2!}x^2 + \omicron(x^2)
$$

## 极限的四则运算法则

> 各个因子的极限都存在，且分母的极限不为零

## 复合函数的极限

> 若$\lim \limits_{x \to x_0}\varphi(x) = u_0,$ 且 $x \ne x_0 \to \phi (x) \ne u_0,$ 令 $u=\phi(x)$

1. $\lim \limits_{u \to u_0}f(u) = A \ \Rightarrow \ \lim \limits_{x \to x_0}f[\varphi(x)] = \lim \limits_{u \to u_0}f(u)=A$
2. $\lim \limits_{u \to u_0}f(u) = \infty \ \Rightarrow \ \lim \limits_{x \to x_0}f[\varphi(x)] = \lim \limits_{u \to u_0}f(u)=\infty$
3. $\lim \limits_{u \to u_0}f(u)$ 不存在 $\nRightarrow \ \lim \limits_{x \to x_0}f[\varphi(x)] = \lim \limits_{u \to u_0}f(u)$ 不存在

## $f(x)$ 在 $x \to x_0$ 为无穷小

## $f(x)$ 在 $x \to \infty$ 为无穷大

## 领域的概念及其表达式

## 函数 $\to$ 数列 $\to$ 子数列

1. 数列收敛， 且 $\lim \limits_{n \to \infty}u_n=A$ $\quad \Leftrightarrow \quad$ $\{u_n \}$ 的任意一个子数列 $\{ u_{n_k} \}$ 都收敛且有相同极限 A;

### 无界量 & 无穷大

> 这是两个不同的概念， 无界不一定无穷大，无穷大一定无界

1. $f(x) = \frac{\frac{1}{x}}{sin(\frac{1}{x})}, x \to 0$ 是无界的 但不是无穷大
2. $f(x) = \frac{1}{x}, x\to 0$ 是无穷的

## 函数连续的定义

## 函数连续的性质

## 闭区间上连续函数的性质及应用

最大值定理

最小值定理

有界性定理

介值定理

[零点定理](./chapter6.md)

## 数列极限的计算

1. 夹逼准则
2. 定积分定义
3. 利用`幂级数`求和
4. 利用`级数收敛`的必要条件 | 级数求和理论

## 函数极限的计算

## 放缩法的整理归纳

对 和式

$$
\sum _{i=1}^{n}{u_i} = u_1 + u_2 + u_3 + \cdots + u_n
$$

进行放缩的两种典型方法:

1. 当 $n \to \infty$ 时, 则$n$

## 洛必达法则

$$
\begin{array}{lr}
if:
1.\ 当 (x \to 0) \ or \ (x \to \infty )时, f(x) 和 F(x) 都趋于 0 或无穷大\\
\qquad 2.\ f'(x) and F'(x) 存在,且 F'(x) \ne 0; \\
\qquad 3.\ \lim \frac{f'(x)}{F'(x)} 存在 或 无穷大;\\
then:
\lim \frac{f(x)}{F(x)} = \lim \frac{f'(x)}{F'(x)}
\end{array}
$$

## 高阶求导的方法

## 泰勒公式 & 麦克劳林公式 & 莱布-尼茨公式

> 同一极限号后面的同一变量的趋向具有同时性

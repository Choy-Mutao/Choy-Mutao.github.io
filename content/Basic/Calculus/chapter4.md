# 一元函数微分学的几何应用

## 极值和最值的概念

`广义`极大值极小值：存在 $x_0$ 的某个领域$U(x_0, \delta)$, 在该领域内的任意一点都有 $f(x) \le f(x_0) (极大) \& f(x) \ge f(x_0)(极小)$

`严格`极大值极小值：存在 $x_0$ 的某个去心领域$\mathring{U}(x_0, \delta)$, 在该领域内的任意一点都有 $f(x) < f(x_0) (极大) \& f(x) > f(x_0)(极小)$

`广义`最大最小值：$x_0$ 为定义域内的一点， 恒有 $f(x) \le f(x_0) (最大) \& f(x) \ge f(x_0)(最小)$

`严格`最大最小值：$x_0$ 为定义域内的一点， 恒有  $f(x) < f(x_0) (最大) \& f(x) > f(x_0)(最小)$

> 如果一个函数在它的一个区间上有最值点， 且这个最值点不是当前区间的端点， 那么这个点必然是一个极值点

## 单调性的判别

若函数$y=f(x)$在区间$I$上恒有$f'(x) > 0$, 那么函数在该区间上严格单调增加;
若函数$y=f(x)$在区间$I$上恒有$f'(x) < 0$, 那么函数在该区间上严格单调减少;

## 一阶可导点的极值性的必要条件

函数在 $x_0$ 处可导且有

## 极值的判别

1. 第一充分条件(一阶)

    1.1  
    1.2
    1.3

2. 第二充分条件(二阶)

    2.1
    2.2

3. 第三充分条件(高阶)

    3.1
    3.2

## 凹凸性和拐点的概念 ---> [多元函数凹凸性, 图像的凹凸性]() 

1. 凹凸性

    函数 $f(x)$ 在区间 $I$ 上连续, 任取两点$(x_1, x_2) \in I$ 

    1. 恒有 $f(\frac{x_1 + x_2}{2}) < \frac{f(x_1) + f(x_2)}{2}$ => $f(x)$ 在 $I$ 上的图形是凹的(`凹弧`)
    2. 恒有 $f(\frac{x_1 + x_2}{2}) > \frac{f(x_1) + f(x_2)}{2}$ => $f(x)$ 在 $I$ 上的图形是凸的(`凸弧`)

2. 拐点

    连续曲线的 `凹弧` 和 `凸弧` 的分界点

## 判别凹凸性的充分条件

函数 $f(x)$ 在区间 $I$ 上 `二阶可导`
1. 若在 $I$ 上 $f''(x) > 0$ => $f(x)$ 在 $I$ 上的图形是凹的(`凹弧`)
1. 若在 $I$ 上 $f''(x) < 0$ => $f(x)$ 在 $I$ 上的图形是凹的(`凹弧`)

## `二阶可导点`是拐点的必要条件

当 $f''(x_0)$ 存在, 且 $(x_0, f(x_0))$ 是曲线上的拐点 => $f''(x_0) = 0$

## 拐点的判别

1. 第一充分条件

2. 第二充分条件

3. 第三充分条件

## 渐近线

1. 水平渐近线

$$
\begin{array}{lr}
\lim \limits_{x \to +\infty} f(x) = y_1 \ , \quad or\\
\lim \limits_{x \to -\infty} f(x) = y_2 \ , \quad or \\
\lim \limits_{x \to +\infty} f(x) = \lim \limits_{x \to -\infty} f(x) = y_0 \\
\end{array}
$$

2. 铅锤渐近线

$$
\begin{array}{lr}
    \lim \limits_{x \to x_0^+} f(x) = \infty \ , \quad or\\
    \lim \limits_{x \to x_0^-} f(x) = \infty
\end{array}
$$

3. 斜渐近线

$$
若 \lim \limits_{x \to +\infty} \frac{f(x)}{x} = k_1, \lim \limits_{x \to +\infty} {f(x) - k_1x} = b_1 \\
若 \lim \limits_{x \to -\infty} \frac{f(x)}{x} = k_2, \lim \limits_{x \to +\infty} {f(x) - k_1x} = b_2 \\
若 \lim \limits_{x \to +\infty} = \lim \limits_{x \to +\infty} = k, \lim \limits_{x \to +\infty} {f(x) - kx} = b
$$


## 最值或者取值范围问题

---
我的一堆问题

1. 分段函数在间断点处有没有凹凸性


# 无穷级数

$$
\sum_{n=1}^n{u_n}
$$

## 正项级数

## 函数项级数

1. 常数项级数
   
   1. 

2. 幂级数

   若 $\sum \limits_{n=0}^{\infty} {u_n(x)}$ 的一般项是 n 次幂函数

   > 一般形式：
   >
   > $$
   > \sum \limits_{n=0}^{\infty} {u_n(x)} = {a_0} + {a_1(x-x_1)} + {a_2(x-x_2)^2} + \cdots + {a_n(x-x_n)^n} + \cdots
   > $$
   >
   > 标准形式：
   >
   > $$
   > \sum \limits_{n=0}^{\infty} {u_n(x)} = {a_0} + {a_1{x}} + {a_2{x^2}} + \cdots + {a_n{x^n}} + \cdots
   > $$

   其中 $a_n$是`幂级数的系数`

3. 收敛点 & 发散点

4. 收敛域

## 阿贝尔定理

1. 定理

2. 收敛半径的存在性

3. 收敛半径的计算

4. 收敛区间和收敛域

## 幂级数的求和函数

## 函数展开成幂级数 $f(x) \Rightarrow \sum \limits_{n=1}^{\infty} {u_n(x)}$

1. $f(x)$ 的泰勒级数

> 若函数 $f(x)$ 在点 $x=x_0$ 处存在任意阶导数
>
> $$
> f(x) \sim \sum \limits_{n=0}^{\infty} \frac{f^{(n)}(x_0)}{n!}{(x-x_0)^n}
> $$
>
> $$
> f(x) = \sum \limits_{n=0}^{\infty} \frac{f^{(n)}(x_0)}{n!}{(x-x_0)^n} + \delta(\xi) , \ \delta(\xi) = \lim \limits_{n \to \infty} \frac{f^{(n+1)}(\xi)}{(n +1)!}{(x-x_0)^(n + 1)} = 0
> $$

2. $f(x)$ 的麦克劳林级数

> $f(x)$ 在 $x_0 = 0$ 时的 泰勒级数
>
> $$
> f(x) \sim \sum \limits_{n=0}^{\infty} \frac{f^{(n)}(x_0)}{n!}{(x)^n}
> $$

Tips：具有任意阶导数的函数，其泰勒公式并不都能收敛于函数本身

## 幂级数展开式的求解技巧

1. 判别级数的类型

   - 正项级数
   - 函数项级数

1. 几何级数（等比级数）

# 二重积分

平面有界闭区域 D
光滑闭合曲线

## 二重积分的存在性

$$
1.\ f(x,y) 在平面区域 D 上连续 \\
2.\ f(x,y) 在平面区域 D 上有界, 且在 D 上除了有限个点和有限条光滑曲线外都是连续的 \\
$$

## 二重积分的精确定义

$$
\iint_D{f(x,y)}{d\sigma} = \lim_{n \to \infty}{\sum_{i=1}^{n}\sum_{j=1}^{n}{(a+\frac{b-a}{n}i, c+\frac{d-c}{n}j)\cdot\frac{b-a}{n}\cdot\frac{d-c}{n}}}
$$

## 二重积分的性质

$$
\begin{array}{lr}
    1.\ \iint_D{1}{d\sigma} = A(D的面积)\\
    2.\ 可积函数必有界 \\
    3.\ \iint_D[k_1{f(x,y) \pm k_2{g(x,y)}}]{d\sigma} = k_1\iint_D{f(x,y){d\sigma} \pm k_2\iint_D{g(x,y)}{d\sigma}}\\
    4.\ when: {D = D_1 \cup D_2} \And {D_1 \cap D_2 = \empty} \quad then: {\iint_D{f(x,y)}{d\sigma} = \iint_{D_1}{f(x,y)}{d\sigma} + \iint_{D_2}{f(x,y)}{d\sigma}}\\
    5.\ if: f(x,y) \le g(x,y) \quad then: \iint_{D}{f(x,y)}{d\sigma} \le \iint_{D}{g(x,y)}{d\sigma} \\
    \qquad specially: \lvert \iint_{D}{f(x,y)}{d\sigma} \rvert \le \iint_{D}\lvert{f(x,y)}\rvert{d\sigma}  \\
    6.\ (估值定理) if: m \le f(x,y) \le M \quad then: mA \le \iint_{D}{f(x,y)}{d\sigma} \le MA  \\
    7.\ (中值定理) \iint_{D}{f(x,y)}{d\sigma} = {f(\xi,\eta)}A\\
\end{array}
$$

## 普通对称性 & 轮换对称性

$$
1.\ (普通对称性) \\
2.\ (轮换对诚性) \\
$$

## 二重积分的计算

$$
1.\ (直角坐标下的计算)\\
2.\ (极坐标下的计算)\\
3.\ 直角坐标和极坐标的选择标准: f(x^2 + y^2), f(\frac{x}{y}), f(\frac{y}{x}), 积分区域和圆的关系 \\
4.\ (直角坐标和极坐标的转化)\left \{
    \begin{array}{lr}
        x = r\cos{\theta} \\
        y = r\sin{\theta}
    \end{array}
\right. \\
5.\ \\
$$

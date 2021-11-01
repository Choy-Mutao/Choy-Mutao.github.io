# 向量

## 线性关系的表示

$$
\sum_i^n{{k_i}{\vec{a_i}}} = 0;
$$

## 等价矩阵和等价向量组

- - -

## 向量空间

### 定义

以线性无关的 $\{\vec{\xi_i} \}$ 作为`基`构建 `n维`的向量空间， 空间中的任意位置表示为：

$$
\vec{\alpha} =\sum_i^n{ a_i\vec{\xi_i}}
$$

其中$[a_1,a_2,a_3,\dots,a_n]$称为`坐标`

### 过渡矩阵

设$R^n$有两个基$\{\vec{\eta_i}\},\{\vec{\xi_i}\}$

$$
[\vec{\eta_1},\vec{\eta_2},\vec{\eta_3},\dots,\vec{\eta_n}] = [\vec{\xi_1},\vec{\xi_2},\vec{\xi_3},\dots,\vec{\xi_n}]C
$$

$C$称为由$\{\vec{\xi_i}\}$到$\{\vec{\eta_i}\}$`过渡矩阵`

### 坐标变换

从基$\{\vec{\xi_i}\}$到$\{\vec{\eta_i}\}$
$$
\vec{\alpha} = [\vec{\eta_1},\vec{\eta_2},\vec{\eta_3},\dots,\vec{\eta_n}] \vec{y}= [\vec{\xi_1},\vec{\xi_2},\vec{\xi_3},\dots,\vec{\xi_n}]\vec{x} \to \vec{x} = C \vec{y}
$$
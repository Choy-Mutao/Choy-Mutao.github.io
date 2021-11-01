# 连续信道及其容量

## 连续单符号加性信道

$$
C = \max_{p(x)}H_c(Y) - H_c(n) = \max_{p(x)}H_c(Y) - \frac{1}{2}\log{2\pi e \sigma^2} \tag{3-4-1}
$$

$$
C = \frac{1}{2}\log{2\pi e P} - \frac{1}{2}\log{2\pi e \sigma^2}  = \frac{1}{2}\log{\frac{P}{\sigma^2}} = \frac{1}{2}\log(1+\frac{S}{\sigma^2}) = \frac{1}{2}\log(1+SNR) \tag{3-4-2}
$$

$$
\frac{1}{2}\log(1+\frac{S}{\sigma^2}) \le C \le \frac{1}{2}\log{2\pi e P} - H_c(n)\tag{3-4-3}
$$

> 非高斯噪声信号 和 高斯噪声信号

## 多维无记忆`加性`连续信道

$$
信道的输入随机序列 X = \{ X_1, X_2, \dots, X_L\}, 输出随机序列 Y = \{ Y_1, Y_2, \dots, Y_L\} \\
加性信道有 \textbf{y = x + n}, 其中 n 为均值为0的高斯噪声 \\
C = \max_{p(x)}I(\textbf{X};\textbf{Y}) = {\sum_{l=1}^L \frac{1}{2} \log(1+\frac{P_l}{\sigma_l^2})} {bit/L} 维自由度\tag{3-4-4} \\
拉格朗日乘子法求极值 \\
注水法
$$

## 限时限频限功率加性高斯白噪声信道
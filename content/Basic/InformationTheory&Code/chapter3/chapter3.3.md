# 离散序列信道及其容量

无记忆离散序列信道的转移概率为:
$$
p(Y|X) = \prod_{l=1}^{L}{p(Y_l|X_l)} \tag{3-3-1}
$$

如果信道无记忆
$$
I(\textbf{X};\textbf{Y}) \le \sum_{l=1}^L{I(X_I;Y_j)} \tag{3-3-2}
$$

如果输入矢量的各个分量相互独立
$$
I(\textbf{X};\textbf{Y}) \ge \sum_{l=1}^L{I(X_I;Y_j)} \tag{3-3-4}
$$

当输入矢量达到最佳分布时(信道独立且无记忆)
$$
C_L = \max_{P_X}I(\textbf{X};\textbf{Y}) = \max_{P_X}\sum_{l=1}^L{I(X_I;Y_j)} = \sum_{l=1}^{L}C(l) \tag{3-3-5}
$$

BSC信道二次扩展:
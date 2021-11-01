# (`随机变量`) & (`n维随机变量`) 的数字特征

## 重要分布的期望和方差

|               分布                |                                          分布列$p_k$ & 概率密度 $f(x)$                                           |        期望         |              方差               |
| :-------------------------------: | :--------------------------------------------------------------------------------------------------------------: | :-----------------: | :-----------------------------: |
|             0-1 分布              |                                     $P(X=k) = p^{k}(1-p)^{1-k}$ <br> $k=0,1$                                     |         $p$         |            $p(1-p)$             |
|     二项分布 <br> $B(n,\ p)$      |                          $P(X=k) = C_{n}^{k}p^{k}(1-p)^{(n-k)}$ <br> $k=0,1,2,\cdots,n$                          |        $np$         |            $np(1-p)$            |
|    泊松分布 <br> $P(\lambda)$     |                            $P(X=k) = \frac{\lambda^k}{k!}e^{-k}$ <br> $k=0,1,\cdots$                             |      $\lambda$      |            $\lambda$            |
|       几何分布 <br> $G(p)$        |                                       $P(X=k) = (1-p)^{1-k}p$ <br> $k=0,1$                                       |    $\frac{1}{p}$    |       $\frac{(1-p)}{p^2}$       |
|  超几何分布 <br> $H(n,\ N,\ M)$   |          $P(X=k) = \frac{C_{M}^{k}C_{N-M}^{n-k}}{C_N^n}$ <br> $max\{0,\ n-N+M\} \le k \le min\{ n, M\}$          |   $n \frac{M}{N}$   | $\frac{nM(N-M)(N-n)}{N^2(N-1)}$ |
|                                   |
| 正态分布 <br> $N(\mu,\ \sigma^2)$ |   $f(x) = \frac{1}{\sqrt{2\pi}{\sigma}}\exp\{-\frac{(x-\mu)^2}{2\sigma^2}\}$ <br> $x \in (-\infty,\ +\infty)$    |        $\mu$        |           $\sigma^2$            |
|     均匀分布 <br> $U(a,\ b)$      |                                    $f(x)=\frac{1}{b-a}$ <br> $x \in (a,\ b)$                                     |   $\frac{a+b}{2}$   |      $\frac{(b-a)^2}{12}$       |
|    指数分布 <br> $E(\lambda)$     |                            $f(x) = \lambda e^{-\lambda x}$ <br> $x \in (0,\ +\infty)$                            | $\frac{1}{\lambda}$ |      $\frac{1}{\lambda^2}$      |
|          $\chi^2(n)$分布          | $f(x) = \frac{x^{\frac{n}{2}-1}e^{-\frac{x}{2}}}{\Gamma(\frac{n}{2})2^{\frac{n}{2}}}$ <br> $x \in (0,\ +\infty)$ |         $n$         |              $2n$               |

## 期望

$$
EX = \sum \limits_{i=1}^{\infty} {x_i}{p_i}, \quad (绝对收敛) \\
EX = \int_{-\infty}^{+\infty}f(x)d{x}
$$

## 方差

$$
DX = Var(X) = E[(X-EX)^2] = E(X^2) - [E(X)]^2, \quad (存在)
$$

## 标准差 (均方差)

$$
\sigma (X) = \sqrt{DX}
$$

## 标准化随机变量

$$
X^* = \frac{X-EX}{\sqrt{DX}}
$$

## 切比雪夫不等式

$$
if: 随机变量 X 的方差 D(X) 存在, 则对\textbf{任意} \varepsilon > 0 \\
then: P\{|X-EX| \ge \varepsilon \} \le \frac{DX}{\varepsilon^2} \ or ,\ P\{|X-EX| < \varepsilon \} \ge {1 - \frac{DX}{\varepsilon^2}}
$$

## 协方差

$$
if: 随机变量 X 和 Y 的方差存在 \ and \ (DX > 0, DY>0) \\
then:Cov(X,Y) = E[(X-EX)(Y-EY)] = E(XY) - EX \cdot EY
$$

## n维随机变量$\textbf{X}$ 的协方差矩阵

$$
\textbf{}{\sum} = (Cov(X_i, X_j))_{n \times n}, \quad (X_i, X_j) \in \textbf{X}= \{ X_1, X_2, \dots, X_n \} \\
Cov(X_i, X_j) = Cov(X_j, X_i)
$$

## 相关系数

$$
\rho_{XY} = \frac{Cov(X,Y)}{\sqrt{DX}\sqrt{DY}}
$$

## k阶原点矩

$$
\alpha_k = E(X^k)
$$

## k阶中心矩

$$
\beta_k = E((X-EX)^k)
$$

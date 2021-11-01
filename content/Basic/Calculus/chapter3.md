# 一元函数微分学的概念和计算

## 什么是导数 和 什么是一个函数可导

$$
f'(x_0) = \lim \limits_{\Delta{x} \to 0} {\frac{\Delta{y}}{\Delta{x}}} = \lim \limits_{\Delta{x} \to 0} {\frac{f(x_0 + \Delta{x}) - f(x_0)}{\Delta{x}}} = \lim \limits_{x \to x_0} {\frac{f(x) - f(x_0)}{x-x_0}}
$$

$$
{\frac{函数的增量}{自变量增量}} = {\frac{\Delta{y}}{\Delta{x}}}
$$

定义: $f'(x_0)$ 存在 <=> $f(x)$ 在 $x_0$ 处`可导`, $f'(x_0)$ 的值记为`导数`;

## 微分定义

存在  "与 $\Delta{x}$ 无关的 A " 使等式成立, 其中 $\lim \limits_{\Delta{x} \to 0}\frac{\omicron(\Delta{x})}{\Delta{x}} = 0$ :

$$
 \Delta{y} = f(x_0 +\Delta{x}) - f(x_0) = A\Delta{x} + \omicron(\Delta{x})
$$

则称 $f(x)$ 在 $x_0$ 处可微, 其中 $A\Delta{x}$ 是 $f(x)$ 在该点的微分

## 可微的判别

1. 写出增量 $\Delta{y} = f(x_0 + \Delta{x}) - f(x_0)$
2. 写线性增量 $A\Delta{x} = f'(x_0)\Delta{}x$
3. 求极限 $\lim \limits_{\Delta{x} \to 0}\frac{\omicron(\Delta{x})}{\Delta{x}} = \frac{\Delta{y} - A\Delta{x}}{\Delta{x}}$

$\lim \limits_{\Delta{x} \to 0}\frac{\omicron(\Delta{x})}{\Delta{x}} = 0$  可微;
$\lim \limits_{\Delta{x} \to 0}\frac{\omicron(\Delta{x})}{\Delta{x}} \ne 0$  不可微;

## 什么是微分形式的不变形

## 导数的四则运算

$$
\begin{array}{lr}
[u(x) \pm v(x)]' = u'(x) \pm v'(x) \ , \quad d[u(x) \pm v(x)] = du(x) \pm dv(y) \\
[u(x)v(x) ]' = u'(x)v(x) + u(x)v'(x)\ , \quad d[u(x)v(x) ] = v(x)du(x) + u(x)dv(x) \\
\Big[ \frac{u(x)}{v(x)} \Big]' = \Big[ \frac{u'(x)v(x) - u(x)v'(x)}{v^2(x)} \Big] \ , \quad d \Big[ \frac{u(x)}{v(x)} \Big] = \Big[ \frac{v(x)du(x) - u(x)dv(x)}{v^2(x)} \Big]\\
\end{array}
$$

## 复合函数的求导

$u = g(x)$ 在 $x$ 处可导 且 $y = f(u)$ 在 $u = g(x)$ 处可导

$$
\{f(g(x))\}' = f'(u)g'(x) = f'(g(x))g'(x) \\
d\{f(g(x))\} = f'(u)g'(x) = f'(g(x))g'(x)
$$

## 反函数求导

设 $y = f(x)$ 可导, 且 $f'(x) \ne 0$ , 则存在反函数 $x=\varphi(y)$, 且 $\frac{dx}{dy} = \frac{1}{\frac{dy}{dx}} => \varphi'(y) = \frac{1}{f'(x)}$

## 参数函数求导

函数 $y=f(x)$ 由参数方程: $
\left \{
    \begin{array}{lr}
    x = \varphi(t) \\
    y = \psi(t) \\
    \end{array}
\right.
$ 确定,  其中 $\varphi(t),\psi(t)$均可导, 当 $\varphi'(t) \ne 0 => \frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{\psi'(t)}{\varphi'(t)}$;

## 分段函数的求导

## 隐函数的求导公式

## 高阶求导公式

## 如何判断一个函数是否`无穷阶可导`

## 基本初等函数的导数公式

$$
\begin{array}{}
 (c)' = 0 & (e^x)' = e^x; \\
(x^a)' = ax^{a-1}; \quad (a^x)' = ax\ln{a}; \\
(\log_a{x})' = \frac{1}{x\ln{a}}; \quad (\ln{x})' = \frac{1}{x}; \\
(\sin{x})' = \cos{x}; \quad (\cos{x})' = -\sin{x}; \\
(\arcsin{x})' = \frac{1}{\sqrt{1-x^2}}; \quad (\arccos{x})' = -\frac{1}{\sqrt{1-x^2}}; \\
(\tan{x})' = \sec^2{x} = \frac{1}{\cos^2x}; \quad (\cot{x})' = -\csc^2{x} = -\frac{1}{\sin^2x}; \\
(\arctan{x})' = \frac{1}{1+x^2}; \quad (\arcctg{x})' = -\frac{1}{1+x^2}; \\
(\sec{x})' = \sec{x}\tan{x}; \quad (\csc{x})' = -\csc{x}\cot{x}; \\
(\ln(x + \sqrt{x^2 + 1}))' = \frac{1}{\sqrt{x^2 + 1}}; \quad (\ln(x + \sqrt{x^2 - 1}))' = \frac{1}{\sqrt{x^2 - 1}}; \\
\end{array}
$$

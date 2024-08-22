---
title: Parabola(Sphere) Formula
type: docs
math: true
---

## Code

我们先简单看一段代码, 这是 SPSO 中的一个测试函数

{{< tabpane langEqualsHeader=true >}}
 {{< tab "C" >}}
 #include "structs.h"

double ParabolaShpere(struct position xs, double p)
{
    int D = xs.size; // 粒子群的 d-dimension
    double f = 0, xd;
    p = 0; // Shift
    for (int d = 0; d < D; d++)
    {
        xd = xs.x[d] - p;
        f = f + xd * xd;
    }
    return f;
}
 {{< /tab >}}
 {{< /tabpane >}}

## 数学解释

如果我们有一个 点 \\(x = (x_1, x_2, \cdots, x_D)\\), 则这段代码的输出为: \\(f = \sum_{d=0}^{D-1}(x_d - p)^2\\), 这就是点 \\(x\\) 到 \\(P = (p, p, \cdots, p)_D\\) 的欧几里得范数的平方;

## 应用场景

* 抛物面: 在计算抛物面上的某个点到原点的距离平方时使用
* 球面: 在计算球面上某个点到球心的距离平方时使用
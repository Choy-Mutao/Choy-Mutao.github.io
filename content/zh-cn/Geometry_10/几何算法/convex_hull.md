---
title: 平面凸包的求解
type: docs
math: true
---

## Pseudo Code

算法: SLOWCONVEXHULL(P)

Input: 平面点集 P

Output: 由\\(CH(P)\\)的顶点沿顺时针方向排列成的队列 \\(l\\)

```math
\displaystyle
\begin{aligned}
E \gets \emptyset
\\ for(每一有序对(p, q) \in P \times P, p \ne q)
\end{aligned}
```

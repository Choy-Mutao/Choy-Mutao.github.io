---
title: 平面凸包的求解
type: docs
math: true
---

## SlowConvexHull

 Input: 平面点集 P

 Output: 描述凸包的点集 l

 1. \\( E \gets \emptyset \\)
 2. \\( \textbf{for} (每一有序对(p,q) \in P \times P, p \ne q)  \\)
 3. \\( \quad \textbf{do} \ valid \gets true\\)
 4. \\( \quad \quad \textbf{for} (除 p 和 q 之外的所有点 r \in P)\\)
 5. \\( \quad \quad \quad \textbf{do \ if (r位于p和q所确定的有向直线的左侧)}\\)
 6. \\( \quad \quad \quad \quad \textbf{then} \ valid \gets fale\\)
 7. \\( \quad \quad \quad \quad \quad \textbf{if} \ (valid) \ \textbf{then} \ 将所有有向边 \overline{pq} 加入到 E \\)
 8. \\( 根据集合E中的各边, 找出CH(P)的所有顶点, 并按照顺时针方向将它们组织为列表 l\\)

## ConvexHull

 Input: 平面点集 P

 Output: 描述凸包的点集 l

 1. 根据 \\(x-\\) 坐标, 对所有的点进行排序, 得到序列 \\(p_1, \dots, p_n\\)
 2. \\(在 \ l_{upper} \ 中加入 p_1 和 p_2 (p_1在前)\\)
 3. \\(\textbf{for} ( i \gets 3 \ \textbf{to} \ n\\))
 4. \\( \quad \textbf{do} \ 在 \ l_{upper} \ 中加入 \ p_i \\)
 5. \\( \quad \quad \textbf{while} \ ( l_{upper} \ 中之至少还有三个点, 而且最末尾的三个点所构成的不是一个右拐) \\)
 6. \\( \quad \quad \quad \textbf{do} \ 将倒数第二个顶点从 \ l_{upper} \ 中删去 \\)
 7. \\( 在 \ l_{lower} \ 中加入 \ p_{n} 和 p_{n-1} (p_{n} \ 在前) \\)
 8. \\( \textbf{for}( i \gets {n-2} \ \textbf{downto} \ 1) \\)
 9. \\( \quad \textbf{do} \ 在 l_{lower} \ 中加入 \ p_i \\)
 10. \\( \quad \quad \textbf{while}(l_{lower} \ 中之至少还有三个点, 而且最末尾的三个点所构成的不是一个右拐) \\)
 11. \\( \quad \quad \quad \textbf{do} 将倒数第二个顶点从 \ l_{lower} \ 中删去 \\)
 12. \\( 将第一个和最后一个点从 \ l_{lower} \ 中删去(以免在上凸包与下凸包联结之后, 出现重复顶点) \\)
 13. \\( 将 \ l_{lower} \ 联结到 \ l_{upper} \ 后面(将由此得到列表记为 \ l) \\)
 14. \\( \textbf{return}(l) \\)

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

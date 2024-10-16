---
title: 直线和线段的相交求解
type: docs
---

## 描述

在求解 2D 和 3D 的线段与直线的相交性时, 一般采用 “参数方程” 来描述两者

## 参数方程

### 直线

```math
P(s) = P_0 + s(P_1 - P_0) = P_0 + s*\vec{u} \\
其中, s = d(P_0, P(s)) / d(P_0, P_1)
```

同理可定义另一条直线的方程 \\(Q(t) = Q_0 + v(Q_1 - Q_0) = Q_0 + t*\vec{v}\\)

### 平行线

当且仅当 \\(\vec{u} = a\vec{v}, \ \vec{u} = P_1-P_0, \ \vec{v} = Q_1 - Q_0\\)

### 非平行线
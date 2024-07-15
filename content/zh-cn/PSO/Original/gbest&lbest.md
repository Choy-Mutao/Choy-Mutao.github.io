---
title: PSO gbest and lbest
type: docs
date: 2024-7-15
description: 在粒子群优化（Particle Swarm Optimization，PSO）算法中，lbest模型和gbest模型是两种不同的策略，用于更新粒子的位置和速度。
---

## gbest 模型(全局最优模型)

全局最优模型的PSO中,一般定义为:

```math
\hat{y}_t \in \left\{ \vec{p}_t^1, \vec{p}_t^2, \ldots, \vec{p}_t^s \right\} \mid f(\hat{y}_t) = \min \left( \left\{ f(\vec{p}_t^1), f(\vec{p}_t^2), \ldots, f(\vec{p}_t^s) \right\} \right)
```

y作为目标粒子, 表示d维搜索空间中整个群或其邻域中最佳粒子的位置;

* 在 *gbest* 模型中，所有粒子都参考全局最优位置（全局最佳解）来更新自己的位置和速度。
* 全局最优位置是整个粒子群中所找到的最好的位置。
* 这种模型通常收敛速度较快，但容易陷入局部最优，因为所有粒子都朝向相同的目标移动。

## lbest 模型(局部最优模型)

在 局部最优模型中, 如下定义一个粒子的符合线性排序邻居粒子:

```math
N_i = \left\{ \vec{p}_t^{i-l}, \vec{p}_t^{i-l+1}, \ldots, \vec{p}_t^{i-1}, \vec{p}_t^i, \vec{p}_t^{i+1}, \ldots, \vec{p}_t^{i+l-1}, \vec{p}_t^{i+l} \right\}
```

则 lbest模型公式如下

```math
\hat{y}_t \in N_i \mid f(\hat{y}_t) = \min \left( \left\{ f(\vec{a}) \right\} \right), \forall \vec{a} \in N_i
```

* 在 *lbest* 模型中，每个粒子仅参考其邻域内的最优位置来更新自己的位置和速度。
* 邻域的定义可以是粒子群中的一小部分粒子，通常是该粒子周围的某个固定数量的邻居粒子。
* 这种模型能够更好地保持多样性，减少陷入局部最优的风险，但收敛速度可能较慢

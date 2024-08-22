---
title: 标准粒子群算法
linkTitle: 标准 PSO 算法
description: Maurice.Clerc于[Standard PSO Descriptions](https://hal.science/hal-00764996)中提出了 StandardPSO 的概念
type: docs
date: 2024-07-15
weight: 1
---

## 0.介绍

自2006年以来，三种连续的标准PSO版本已在[Particle Swarm Central](https://www.particleswarm.info/)线上发布，分别是SPSO 2006、2007和2011。这些版本的基本原理大致相同，但由于设计时利用了*当时*最新的理论分析，其具体公式略有不同。

## 1. 基本概念

* 解空间: 粒子的特性所处的问题的边界
* 适应函数: 每个粒子的位置有一个对应的适应度值, 用于衡量该位置的优劣
* 粒子群(群): 对问题描述的的解的集合
* 粒子: 组成粒子群的单位
* 位置: 对粒子的特性的描述,一般用一个 n 维向量表示
* 速度: 位置的变化率

## 2.Particle Swarm Optimisation

PSO 的计算过程主要是在迭代的过程中逐步优化问题的解 --- 以一簇粒子群为初始步骤, 逐步迭代, 群中的每个粒子都知道截至当前迭代步的解空间中, 群内的 *全局最佳位置* 和 *个体最佳位置*, 故而 PSO 中的 群 和 个体 是有记忆的.

在每一步的迭代中, 群中的每个粒子 *位置* 和 *速度* 受所在群中全局和个体的 *记忆最优解* 影响, 通过重复 "变动" 的过程来, 比对解空间的 "适应度" 函数, 来渐进逼近问题的真实最优解;

算法的描述:

### 2.0 环境条件(全局变量)

* S: 粒子群容量
* K: 指定个体的最大通知数
* T: 信息链路的拓扑结构
* w: 第一置信系数(first cognitive/confident coefficient)
* c: 第二置信系数(second cognitive/confidence coefficient)
* R: random distribution of c
* B: 边界条件

[SPSO2006](/content/zh-cn/PSO/Original/SPSO2006/_index.md)

[SPSO2007]

[SPSO2011]

### 2.1 群体的初始化

粒子群中的每个粒子在搜索空间内随机初始化位置和速度

[SPSO2006]

[SPSO2007]

[SPSO2011]

### 2.2 迭代过程

* 更新粒子的速度和位置
* 速度更新公式的各个版本的定义
* 更新位置信息
* 计算新位置的适应度值并更新粒子的最佳位置

### 2.3 停止条件

* 对目标函数结果的收敛

## 代码框架

{{< tabpane langEqualsHeader=true >}}
 {{< tab "C" >}}
 #include <stdio.h>
 #include <stdlib.h>
 int main(void)
 {
    puts("Hello World!");
    return EXIT_SUCCESS;
 }
 {{< /tab >}}
 {{< tab "python" >}}
 #include <stdio.h>
 #include <stdlib.h>
 int main(void)
 {
    puts("Hello World!");
    return EXIT_SUCCESS;
 }
 {{< /tab >}}
 {{< tab "c#" >}}
 using namespace math
 int main(void)
 {
    puts("Hello World!");
    return EXIT_SUCCESS;
 }
 {{< /tab >}}
 {{< /tabpane >}}

## 速度的公式表示

```math
\vec{V}_{t+1}^{i} = \vec{V}_{t}^{i} + \varphi_{1} R_{1t}^{i} (\vec{p}_{t}^{i} - \vec{x}_{t}^{i}) + \varphi_{2} R_{2t}^{i} (\vec{g}_{t} - \vec{x}_{t}^{i})
```
\\(\omega_1\\),和 \\(\omega_2\\) 为 *加速系数*, 来控制全局和个体最佳位置对粒子的 *移动速度* 和 *移动方向* 的影响程度

\\(R_1\\) 和 \\(R_2\\) 是符合均匀随机分布的单位向量, 用于来维护群体的各异性

\\(\vec{p}_t^i\\)是群中 \\(粒子_i\\) 在 \\(t\\)代迭代的个体最优位置

\\(\vec{g}_t^i\\)是群中 \\(粒子_i\\) 在 \\(t\\)代迭代的全局最优位置

## 位置变化公式

```math
\vec{x}_{t+1}^i = \vec{x}_{t}^i + \vec{V}_{t+1}^i
```

记 \\(\vec{x}_0^i\\) 和 \\(\vec{V}_0^i\\) 是符合均匀随机分布的初始量, 其中,个体最优位置的初始化与它的初始位置相同: \\(\vec{p}_0^i = \vec{x}_0^i\\)

## PSO 是一种独立于问题的算法

因此它有非常广泛的应用场景，因为运行算法所需的唯一信息是适应度评估每个候选解决方案(有时候会增加问题的约束集)

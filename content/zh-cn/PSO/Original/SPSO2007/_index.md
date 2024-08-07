---
title: Standard PSO Version 2007
type: docs
description: 这与原始版本（1995）非常接近，基于最近的一些工作，只做了一些改进。
---

## 与 SPSO2006 之间的主要区别

1. 增加控制项: "使算法对搜索空间的旋转变换不敏感"
   > Note: 减低性能可能不会对结果有太大改善.(做了更多的尝试)
2. 增加控制项 "是否每次迭代随机前置换粒子的位置"
   > Note: 减低性能可能不会对结果有太大改善(做了更多的尝试)
3. 增加控制项 "是否约束粒子边界"
   > Note: 在极少数情况下，如果停止标准是最大评估次数，则不限制位置可能会导致无
   > 限运行
4. 一个特定粒子是另一个粒子的通知者的概率 p。在 SPSO-06 中，它是隐式的（通过构建
   随机信息网络）。在这里，默认值直接作为（S，K）的函数计算，因此信息网络与
   SPSO-07 中的完全相同。然而，现在它可以被“操纵”（即可以分配任何值）
5. 搜索空间可以量化,但该算法不适用于组合问题

> 额外的, 在随机数的计算上提供了一些其他的方法

## 1. SPSO2007 介绍

在项目结构上, 在不着重考虑性能的情况下, 对算法的逻辑进行了更详细的*结构化*, 将算
法中涉及到的数据进行了封装, 分为:

## 1.1 SPSO2007 Structs

```c
struct quantum
{
 double q[D_max];
 int size;
};

struct SS
{
 int D;
 double max[D_max];
 double maxInit[D_max];
 double min[D_max];
 double minInit[D_max];
 struct quantum q;  // Quantisation step size. 0 => continuous problem
};

struct param
{
 double c;  // Confidence coefficient
 int clamping; // Position clamping or not
 int K;   // Max number of particles informed by a given one
 double p;  // Probability threshold for random topology
 // (is actually computed as p(S,K) )
 int randOrder; // Random choice of particles or not
 int rand; // 0 => use KISS. Any other value: use the standard C RNG
 int initLink; // How to re-init links
 int rotation; // Sensitive to rotation or not
 int S;   // Swarm size
 int stop;  // Flag for stop criterion
 double w;  // Confidence coefficient
};

struct fitness
{
 int size;
 double f[fMax];
};

struct position
{
 double f;
 int improved;  // *** add improved to SPSO2006
 int size;
 double x[D_max];
};

struct velocity
{
 int size;
 double v[D_max];
};
struct problem
{
 double epsilon;  // Admissible error
 int evalMax;   // Maximum number of fitness evaluations
 int function;   // Function code
 double objective;  // Objective value
 // Solution position (if known, just for tests)
 struct position solution;
 struct SS SS;  // Search space
};

struct swarm
{
 int best;      // rank of the best particle
 struct position P[S_max]; // Previous best positions found by each particle
 int S;       // Swarm size
 struct velocity V[S_max]; // Velocities
 struct position X[S_max]; // Positions
};

struct result
{
 double nEval;   // Number of evaluations
 struct swarm SW; // Final swarm
 double error;  // Numerical result of the run
};
struct matrix  // Useful for "non rotation sensitive" option
{
 int size;
 double v[D_max][D_max];
};
```

## 全局变量

```c
#define D_max 114 //搜索空间的最大维度数
#define R_max 500 //最大运行次数
#define S_max 910 //最大群容量
#define fMax 6 //最大约束数+1
#define zero  0 //1.0e-30//避免数值不稳定
```

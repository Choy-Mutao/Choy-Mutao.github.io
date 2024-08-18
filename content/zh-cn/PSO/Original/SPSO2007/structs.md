---
title: 参数结构体
type: docs
---

## 全局变量

```c
#define D_max 114 //搜索空间的最大维度数
#define R_max 500 //最大运行次数
#define S_max 910 //最大群容量
#define fMax 6 //最大约束数+1
#define zero  0 //1.0e-30//避免数值不稳定
```

## 粒子群(Swarm)

定义粒子群中包含

- P: 粒子局部最优位置队列(上一代)
- X: 当前每个粒子的位置特征
- V: 当前每个粒子的迭代速度
- best: 全局最优位置

```c
struct swarm
{
 int best;                  // rank of the best particle
 int S;                     // Swarm size
 struct Position P[S_max];  // Previous best positions found by each particle
 struct Velocity V[S_max];  // Velocities
 struct Position X[S_max];  // Positions
};
```

其中:

### 位置(Position)

- f: 当前位置的评估误差
- improved: 增加了判断参数
- x: 解数组

```c
struct Position
{
 double f;
 int improved;  // *** add improved to SPSO2006
 int size;
 double x[D_max];
};
```

### 速度(Velocity)

- v: 速度数组

```c
struct Velocity
{
 int size;
 double v[D_max];
};

```

## 控制(环境)参数(Param)

一种粒子群算法的通用控制参数:

- S: 粒子群容量
- K: 每次移动的通知数
- w: 关于速度生成公式的第一变量
- c: 关于速度生成公式的第二变量

```c
struct Param
{
 int clamping;  // Position clamping or not
 double p;      // Probability threshold for random topology
                // (is actually computed as p(S,K) )
 int randOrder; // Random choice of particles or not
 int rand;      // 0 => use KISS. Any other value: use the standard C RNG
 int initLink;  // How to re-init links
 int rotation;  // Sensitive to rotation or not
 int S;         // Swarm size
 int K;         // Max number of particles informed by a given one
 int stop;      // Flag for stop criterion
 double w;      // Confidence coefficient
 double c;      // Confidence coefficient
};
```

## 问题描述(Problem)

- SearchSpace 问题的解空间
- objective 通常一个优化问题是有一个目标值的
- epsilon 允许误差(对目标值)
- function 适应度函数

```c
struct Problem
{
 double epsilon;            // Admissible error
 int evalMax;               // Maximum number of fitness evaluations
 int function;              // Function code
 double objective;          // Objective value
 struct Position solution;  // Solution position (if known, just for tests)
 struct SearchSpace SS;     // Search space
};
```

## 解空间描述(SearchSpace)

- D 问题的维度
- max 上边界
- min 下边界
- maxInit 初始化上边界
- minInit 初始化下边界

```c
struct SearchSpace
{
 int D;
 double max[D_max];
 double maxInit[D_max];
 double min[D_max];
 double minInit[D_max];
 struct quantum q;  // Quantisation step size. 0 => continuous problem
};
```

## 结果(Result)

```c
struct result
{
 struct swarm SW; // Final swarm
 double nEval;   // Number of evaluations
 double error;  // Numerical result of the run
};
```

## 子数据

```c
struct quantum
{
 double q[D_max];
 int size;
};

struct fitness
{
 int size;
 double f[fMax];
};

struct matrix  // Useful for "non rotation sensitive" option
{
 int size;
 double v[D_max][D_max];
};
```

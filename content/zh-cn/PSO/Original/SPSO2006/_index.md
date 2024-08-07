---
title: Standard PSO Version 2006
type: docs
description: 非常接近 1995 版本的算法, 所以一般说 SPSO2006 版本指(w=0.8)
---

## 定义 位置&速度 结构体

```c
struct position
{
  int size;
  double* x;
  float f;
}

struct velocity
{
  int size;   // d-dimension
  double* v; // value of velocity
}
```

## 环境数据

```c
int D = 2; // 设置问题的搜索空间维度为 2;

// 设置搜索空间的边界
for(d = 0; d< D; d++)
{
  xmin[d] = -100;
  xmax[d] = 100;
}
int S = 10+( int )(2*sqrt(D)); if (S>S_max) S=S_max;
int K = 3;
double w = 1 / ( 2 * log( 2 ) ); double c = 0.5 + log( 2 );

int best_index; // 从 P[] 中找到全局最佳的位置;
struct position *P; // P[] 最佳位置, 和 X 有数据对齐的关系;
```

## 初始化粒子群

```c
// init: 粒子群初始化
init:
X = (struct position_06*)malloc(S * sizeof(struct position_06));
V = (struct velocity_06*)malloc(S * sizeof(struct velocity_06));
if (X == NULL || V == NULL)
{
  return -1;
}

for (int s = 0; s < S; s++)
{
  X[s].size = D;
  V[s].size = D;
  double* d_array = (double*)malloc(D* sizeof(double));
  double* v_array = (double*)malloc(D * sizeof(double));
  if (d_array == NULL || v_array == NULL)
  {
    return -1;
  }
  for (int d = 0; d < D; d++)
  {
    d_array[d] = alea_06(xmin[d], xmax[d]);
    v_array[d] = (alea_06(xmin[d], xmax[d]) - d_array[d]) / 2;
  }
  X[s].x = d_array;
  V[s].v = v_array;
  free(d_array);
  free(v_array);
}

// 初始化 局部最佳位置&全局最佳位置
for (int s = 0; s < S; s++)
{
  X[s].f = fabs(0 - 0); //TODO: 定义适应度函数
  P[s] = X[s];// Best Position = current one
}

// Find the best
best_index = 0;
for (int s = 1; s < S; s++)
  if (P[s].f < P[best_index].f)
    best_index = s;

```

## 迭代移动

```c
loop:
    // The swarm MOVES
    for (s = 0; s < S; s++) // For each particle ...
    {
        // .. find the best informant
        g = s;
        for (m = 0; m < S; m++)
        {
            if (LINKS[m][s] == 1 && P[m].f < P[g].f) g = m;
        }

        // ... compute the new velocity, and move
        for (d = 0; d < D; d++)
        {
            V[s].v[d] = w * V[s].v[d] + alea_06(0, c) * (P[s].x[d] - X[s].x[d]);
            V[s].v[d] = V[s].v[d] + alea_06(0, c) * (P[g].x[d] - X[s].x[d]);
            X[s].x[d] = X[s].x[d] + V[s].v[d];
        }

        // ... interval confinement (keep in the box)
        for (d = 0; d < D; d++)
        {
            if (X[s].x[d] < xmin[d])
            {
                X[s].x[d] = xmin[d]; V[s].v[d] = 0;
            }
            if (X[s].x[d] > xmax[d])
            {
                X[s].x[d] = xmax[d]; V[s].v[d] = 0;
            }
        }


        // ... evaluate the new position
        X[s].f = fabs(perf_06(s, function) - f_min);


        // ... update the best previous position
        if (X[s].f < P[s].f)
        {
            P[s] = X[s];
            // ... update the best of the bests
            if (P[s].f < P[best].f) best = s;
        }
    }
```

## 环境判断条件(退出的时机)

```c
// Check if finished
// If no improvementd, information links will be reinitialized
error = P[best_index].f;
if (error >= error_prev) init_links = 1;
else init_links = 0;
error_prev = error;

if (error > eps && nb_eval < eval_max) goto loop;
if (error > eps) n_failure = n_failure + 1;

```

## T(information links topology) 信息链路拓扑

关于这个话题已经做了很多工作。主要结果是没有 “最佳”拓扑。因此，SPSO2006 版本使用了随机方法。
> K=3 这并不意味着每个粒子都由K个粒子通知：通知给定粒子的粒子数量可以是1（对于每个粒子通知自己）和S之间的任何值。

```c
if (init_links == 1)
{
    // Who informs who, at random
    for (s = 0; s < S; s++)
    {
        for (m = 0; m < S; m++) LINKS[m][s] = 0; // Init to "no link"
        LINKS[s][s] = 1; // Each particle informs itself
    }

    for (m = 0; m < S; m++) // Other links
    {
        for (i = 0; i < K; i++)
        {
            s = alea_integer_06(0, S - 1);
            LINKS[m][s] = 1;
        }
    }
}
```

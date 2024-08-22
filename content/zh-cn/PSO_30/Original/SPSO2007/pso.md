---
title: 主逻辑
type: docs
---

## 初始化

相较于 SPSO2006, 该版本增加了`量化`的步骤, 用于处理离散问题的优化

## 筛选最优解

相较于 SPSO2006, 该版本定义了两种筛选方法

1. 比较评价函数的值与目标值的误差
2. 比较当前位置(解)与目标位置(目标解)的误差

## 更新拓扑通知

## 迭代移动

相较于 SPSO2006, 该版本在移动过程中增加了如下步骤

- 在每次开始移动前对粒子群中的粒子进行随机排序
- 更新了一种新的速度生成策略

### 速度生成逻辑

## 环境判断条件(退出的时机)

相较于 SPSO2006, 该版本增加了更多推出条件, 防止陷入死循环

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
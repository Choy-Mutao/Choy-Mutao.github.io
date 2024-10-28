---
title: AVL树(Tree)
type: docs
math: true
---

## 描述

AVL(Adelson-Velskii and Landis) 是带有 *平衡条件(balance condition)* 的 *二叉查找树(BST)*,通过自动调整树的结构，AVL树可以确保查找、插入和删除操作的时间复杂度为 \\(O(\log{n})\\)。

用来衡量其"平衡程度"的标准是树中某个节点的左右子树的高度差

树的 *高度* 是指树中 *层数* 的总数。

## 平衡条件

AVL树中的每个节点的左右子树高度差（称为平衡因子）最多为1，(这样的约束确保了树的高度在\\(O(\log{n})\\)范围内)。即左右子树的高度差为 -1、0 或 1。否则，树需要通过旋转操作进行重新平衡。

## 树的旋转（为了保证平衡性）

- 左左(外-单)
- 左右(内-双)
- 右左(内-双)
- 右右(外-单)

### 单旋转

### 双旋转
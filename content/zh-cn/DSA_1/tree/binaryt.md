---
title: 二叉树(Binary Tree)
type: docs
---

## 描述

一颗每个结点的子节点不多于两个

## 实现

```c
struct BNode
{
    Object element;     // The data in the node
    BNode *left;        // Left child
    BNode *right;       // Right child
}
```

## 应用

### 表达式树

表达树中的树叶是 **操作数(operand)**

其他的节点是 **操作符(operator)**

### 中缀表达式(infix expresion) / 中缀遍历(inorder traversal)

写一种算法将**后缀表达式** 转变为 **表达式树**

将 **中缀表达式** 转变为 **后缀表达式** 的算法

**从两种常用类型的输入生成表达式树**
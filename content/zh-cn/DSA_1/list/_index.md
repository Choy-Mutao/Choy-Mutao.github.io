---
title: 数据结构---链表(List)
type: docs
weight: 2
---

## 描述

链表以 **节点** 为单位，每个元素都是一个独立对象，在内存空间的存储是 **非连续的**。

```cpp
struct ListNode {
    int val;        // 节点值
    ListNode *next; // 后继节点引用
    ListNode(int x) : val(x), next(NULL) {}
};
```

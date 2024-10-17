---
title: 查找树ADT---二叉查找树(Binary Search Tree)
type: docs
---

## 描述

二叉查找树， 是二叉树在*查找*中的应用。 使二叉树变为二叉查找树的方法， 是增加一个性质： 对于树中的每个结点Node， 它的左子树中的所有项的值， 都小于X中的项， 而它的右子树中所有的项目的值大于 X 中的项。 其中(小于&大于)仅表达某种的排列规则在结点之间递归传递

## 二叉查找树的框架

```c
template<typename Comparable>
class BinarySearchTree
{
    public:
        BinarySearchTree();
        BinarySearchTree(const BinarySearchTree &node);
        ~BinarySearchTree();

        const Comparable &findMin() const;
        const Comparable &findMax() const;
        bool contains(const Comparable &node) const;
        bool isEmpty() const;
        void printTree() const;

        void makeEmpty();
        void insert(const Comparable &node);
        void remove(const Comparable &node);

        const BinarySearchTree & operator=(const BinarySearchTree &rhs);
    
    private:
        struct BinaryNode
        {
            Comparable element;
            BinaryNode *left;
            BinaryNode *right;

            BinaryNode(const Comparable &theelement, BinaryNode *lt, BinaryNode *rt): element(theelement), left(lt), right(rt)
        }

        BinaryNode *root;

        // =========== recuris sub progress
        void insert(const Comparable &node, BinaryNode *&t) const;
        void remove(const Comparable &node, BinaryNode *&t) const;
        BinaryNode *findMin(BinaryNode *t) const;
        BinaryNode *findMax(BinaryNode *t) const;
        bool contains(const Comparable &x, BinaryNode *&t) const;
        void makeEmpty(BinaryNode *&t);
        
        void printTree(BinaryNode *t) const;
        BinaryNode *clone(BinaryNode *t) const;
}
```


## 随机生成二叉查找树


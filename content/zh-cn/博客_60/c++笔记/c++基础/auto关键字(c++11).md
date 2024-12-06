---
title: auto关键字(c++11)
type: blog
date: 2018-01-28
---

## 描述

在早期的 C/C++中 auto 的含义是：使用 auto 修饰的变量是具有自动存储器的局部变量，
但遗憾的是一直没有人去使用它。

在 C++11 中，标准委员会赋予了 auto 全新的含义：auto 不再是一个存储类型指示符，而
是作为一个新的类型指示符来指示编译器，auto 声明的变量必须由编译器在编译时期推导
而得。

```cpp
#include <iostream>
using namespace std;
double Fun()
{
    return 3.14;
}
int main()
{
    int a = 10;
    auto b = a;
    auto c = 'A';
    auto d = Fun();
    //打印变量b,c,d的类型
    cout << typeid(b).name() << endl;//打印结果为int
    cout << typeid(c).name() << endl;//打印结果为char
    cout << typeid(d).name() << endl;//打印结果为double
    return 0;
}
```

> 使用 auto 变量时必须对其进行初始化，在编译阶段编译器需要根据初始化表达式来推导
> auto 的实际类型。因此，auto 并非是一种“类型”的声明，而是一个类型声明的“占位符
> ”，编译器在编译期会将 auto 替换为变量实际的类型

## auto 的使用细则

### 1. auto 与指针和引用结合起来使用

用 auto 声明指针类型时，用 auto 和 auto\*没有任何区别，但用 auto 声明引用类型时
必须加&。

```cpp
#include <iostream>
using namespace std;
int main()
{
    int a = 10;
    auto b = &a;   //自动推导出b的类型为int*
    auto* c = &a;  //自动推导出c的类型为int*
    auto& d = a;   //自动推导出d的类型为int
    //打印变量b,c,d的类型
    cout << typeid(b).name() << endl;//打印结果为int*
    cout << typeid(c).name() << endl;//打印结果为int*
    cout << typeid(d).name() << endl;//打印结果为int
    return 0;
}
```

> 注意：用 auto 声明引用时必须加&，否则创建的只是与实体类型相同的普通变量

### 2. 在同一行定义多个变量

当在同一行声明多个变量时，这些变量必须是相同的类型，否则编译器将会报错，因为编译
器实际只对第一个类型进行推导，然后用推导出来的类型定义其他变量。

```cpp
int main()
{
    auto a = 1, b = 2; //正确
    auto c = 3, d = 4.0; //编译器报错：“auto”必须始终推导为同一类型
    return 0;
}
```

## auto 不能推导的场景

### 1. auto 不能作为函数的参数

```cpp
// 以下代码编译失败，auto不能作为形参类型，因为编译器无法对x的实际类型进行推导。
void TestAuto(auto x) {}
```

### 2. auto 不能直接用来声明数组

```cpp
int main()
{
    int a[] = { 1, 2, 3 };
    auto b[] = { 4, 5, 6 };//error
    return 0;
}
```

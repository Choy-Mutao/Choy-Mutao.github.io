---
title: c++基础
type: blog
date: 2024-08-14
---

## 什么是 C++

C 语言是结构化和模块化的语言，适合处理较小规模的程序。对于复杂的问题，规模较大的
程序，需要高度的抽象和建模时，C 语言则不合适。为了解决软件危机，20 世纪 80 年代
，计算机界提出了 [OOP(object_oriented_programming：面向对象)] 思想，支持面向对象
的程序设计语言应运而生。

1982 年，Bjarne Stroustrup 博士在 C 语言的基础上引入并扩充了面向对象的概念，发明
了一种新的程序语言。为了表达该语言与 C 语言的渊源关系，命名为 C++。因此，C++是基
于 C 语言而产生的，它既可以进行 C 语言的过程化程序设计，又可以进行以抽象数据类型
为特点的基于对象的程序设计，还可以进行面向对象的程序设计。

## C++ 发展史

1979 年，贝尔实验室的本贾尼等人试图分析 unix 内核的时候，试图将内核模块化于是在
C 语言的基础上进行扩展，增加了类的机制，完成了一个可以运行的预处理程序，称之为 C
with classes。

- **c with class**: 类及派生类、公有和私有成员、类的构造析构、友元、内联函数、赋
  值运算符重载等
- **c++1.0**: 添加虚函数概念，函数和运算符重载，引用、常量等
- **c++2.0**: 更加完善支持面向对象，新增保护成员、多重继承、对象的初始化、抽象类
  、静态成员以及 const 成员函数
- **c++3.0**: 进一步完善，引入模板，解决多重继承产生的二义性问题和相应构造和析构
  的处理
- **c++98**: _C++标准第一个版本_，绝大多数编译器都支持，得到了国际标准化组织
  （ISO）和美国标准化协会认可，以模板方式重写 C++标准库，引入了 STL（标准模板库
  ）
- **c++03**: C++标准第二个版本，语言特性无大改变，主要 ∶ 修订错误、减少多异性
- **c++05**: C++标准委员会发布了一份计数报告（Technical Report，TR1），正式更名
  C++0x，即 ∶ 计划在本世纪第一个 10 年的某个时间发布
- **c++11**: 增加了许多特性，使得 C++更像一种新语言，比如 ∶ 正则表达式、基于范围
  for 循环、auto 关键字、新容器、列表初始化、标准线程库等
- **c++14**: 对 C++11 的扩展，主要是修复 C++11 中漏洞以及改进，比如 ∶ 泛型的
  lambda 表达式，auto 的返回值类型推导，二进制字面常量等
- **c++17**: 在 C++11 上做了一些小幅改进，增加了 19 个新特性，比如
  ∶static_assert（）的文本信息可选，Fold 表达式用于可变的模板，if 和 switch 语句
  中的初始化器等

## C++关键字(C++98)

### 基本类型

`void`,`char`,`int`,`double`, `float`, `short`, `long`, `bool`, `false`, `true`,
`signed`, `unsigned`,

### 面向对象

`typedef`, `typename`, `enum`,`struct`, `class`,`friend`,`private`, `protected`,
`public`,`virtual`, `namespace`,`template`,

### 程序控制

`do`,`while`, `if`,`else`, `return`, `try`, `catch`,`throw`,`for`, `continue`,
`break`,`switch`, `case`,`goto`,`delete`,

### 特殊

`const`,`auto`, `inline`, `sizeof`,`static`, `asm`, `dynamic_cast`, `typeid`,
`mutable`, `union`, `wchar_t`, `explicit`, `static_cast`, `default`, `export`,
`new`, `using`, `extern`, `operator`, `register`, `const_cast`,`this`,
`volatile`, `reinterpret_cast`

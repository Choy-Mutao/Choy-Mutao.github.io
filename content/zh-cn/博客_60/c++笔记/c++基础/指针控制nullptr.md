---
title: 指针控制nullptr
type: blog
date: 2019-02-19
---

## C++98 中的空指针

在良好的 C/C++编程习惯中，在声明一个变量的同时最好给该变量一个合适的初始值，否则
可能会出现不可预料的错误。比如未初始化的指针，如果一个指针没有合法的指向，我们基
本都是按如下方式对其进行初始化：

```cpp
int *p1 = NULL;
int *p2 = 0;
```

NULL 其实是一个宏，在传统的 C 头文件(stddef.h)中可以看到如下代码：

```cpp
/* Define NULL pointer value */
#ifndef NULL
#ifdef __cplusplus
#define NULL    0
#else  /* __cplusplus */
#define NULL    ((void *)0)
#endif  /* __cplusplus */
#endif  /* NULL */
```

可以看到，NULL 可能被定义为字面常量 0，也可能被定义为无类型指针(void\*)的常量。
但是不论采取何种定义，在使用空值的指针时，都不可避免的会遇到一些麻烦，例如：

```cpp
#include <iostream>
using namespace std;
void Fun(int p)
{
	cout << "Fun(int)" << endl;
}
void Fun(int* p)
{
	cout << "Fun(int*)" << endl;
}
int main()
{
	Fun(0);           //打印结果为 Fun(int)
	Fun(NULL);        //打印结果为 Fun(int)
	Fun((int*)NULL);  //打印结果为 Fun(int*)
	return 0;
}
```

程序本意本意是想通过 Fun(NULL)调用指针版本的 Fun(int\* p)函数，但是由于 NULL 被
定义为 0，Fun(NULL)最终调用的是 Fun(int p)函数。

> 在 C++98 中字面常量 0，既可以是一个整型数字，也可以是无类型的指针(void\*)常量
> ，但编译器默认情况下将其看成是一个整型常量，如果要将其按照指针方式来使用，必须
> 对其进行强制转换。

## C++11 中的指针空值

对于C++98中的问题，C++11引入了关键字nullptr

1. 在使用nullptr表示指针空值时，不需要包含头文件，因为nullptr是C++11作为关键字引入的。
2. 在C++11中，sizeof(nullptr)与sizeof((void*)0)所占的字节数相同。
3. 为了提高代码的健壮性，在后序表示指针空值时建议最好使用nullptr。
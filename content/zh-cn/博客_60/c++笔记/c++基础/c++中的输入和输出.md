---
title: c++中的输入和输出
type: blog
date: 2021-09-02
---

## 描述

最后一种方式就是通过”using namespace 命名空间名称“将命名空间中的全部成员引入。这
样一来，在该语句之后的代码中就可以直接使用该命名空间内的全部成员了。

```cpp
#include <iostream>
using namespace std;
int main()
{
    cout <<"hello world"<< endl;
    return 0;
}
```

在 C 语言中有标准输入输出函数 `scanf` 和 `printf，而在` C++中有 `cin` 标准输入和
`cout` 标准输出。在 C 语言中使用 `scanf` 和 `printf` 函数，需要包含头文件
`stdio.h`。在 C++中使用 `cin` 和 `cout`，需要包含头文件 `iostream` 以及 `std` 标
准命名空间。

C++的输入输出方式与 C 语言相比是更加方便的，因为 C++的输入输出不需要增加数据格式
控制，例如：整型为%d，字符型为%c

```cpp
#include <iostream>
using namespace std;
int main()
{
    int i;
    double d;
    char arr[20];
    cin >> i;
    cin >> d;
    cin >> arr;
    // 其中, 每次的 endl 会刷新一次输出缓存;
    cout << i << endl;
    cout << d << endl;
    cout << arr << endl;
    return 0;
}
```

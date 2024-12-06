---
title: std&stl
type: blog
date: 2017-11-01
---

## `std::` 和 `stl::` 的区别

在 C++ 编程中，`std` 和 `STL` 是两个经常被提及的概念，但它们之间存在一些重要的区
别。下面详细解释这两个概念及其区别：

### `std` 命名空间

`std` 是 C++ 标准库中的命名空间，几乎所有标准库中的组件都定义在这个命名空间中
。`std` 包括了各种容器（如 `vector`, `list`, `map`）、算法（如 `sort`, `find`）
、输入输出流（如 `cin`, `cout`）、字符串（如 `string`）、智能指针（如
`shared_ptr`, `unique_ptr`）等。

#### 示例

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::sort(vec.begin(), vec.end());

    for (const auto& elem : vec) {
        std::cout << elem << " ";
    }

    return 0;
}
```

### STL (Standard Template Library)

STL 是 C++ 标准模板库的缩写，它是 C++ 标准库的一部分，但并不是全部。STL 主要包含
以下四个部分：

1. **容器（Containers）**：用于存储数据的结构，如 `vector`, `list`, `deque`,
   `set`, `map` 等。
2. **算法（Algorithms）**：用于处理容器中的数据的函数，如 `sort`, `find`,
   `copy`, `transform` 等。
3. **迭代器（Iterators）**：用于访问容器中元素的对象，类似于指针。
4. **函数对象（Function Objects）**：可调用的对象，也称为仿函数（functors），如
   `less`, `greater` 等。

#### 示例

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

int main() {
    std::vector<int> vec = {5, 3, 4, 1, 2};
    std::sort(vec.begin(), vec.end(), std::greater<int>());

    for (const auto& elem : vec) {
        std::cout << elem << " ";
    }

    return 0;
}
```

### 区别

1. **范围不同**：

   - `std` 命名空间包含整个 C++ 标准库的所有组件。
   - STL 是 `std` 命名空间的一部分，主要关注容器、算法、迭代器和函数对象。

2. **内容不同**：

   - `std` 包含的内容更广泛，包括但不限于 STL 的所有组件。例如，`std` 还包含输入
     输出流（如 `cin`, `cout`）、字符串（如 `string`）、智能指针（如
     `shared_ptr`, `unique_ptr`）等。
   - STL 专注于提供高效的数据结构和算法，主要用于处理数据集合。

3. **设计目的不同**：
   - `std` 的设计目的是提供一个全面的工具集，支持 C++ 程序员进行各种开发任务。
   - STL 的设计目的是提供高效的、通用的、可复用的数据结构和算法。

### 总结

- `std` 是 C++ 标准库的命名空间，包含所有标准库组件。
- STL 是 `std` 命名空间的一部分，专注于容器、算法、迭代器和函数对象。

理解这两者的区别有助于更好地利用 C++ 标准库提供的功能，提高编程效率和代码质量。

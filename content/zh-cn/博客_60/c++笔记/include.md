---
title: include 的细节
type: blog
date: 2024-09-17
---

## #include "headername" 和 #include \<headername\> 的区别

`#include "headername"` 和 `#include <headername>` 的主要区别在于头文件的搜索路
径。虽然在包含标准库文件（如 iostream）时，两者的行为通常没有区别，但在实际开发
中，两者有不同的语义，尤其是在包含自定义头文件时。

### 1.#include "headername"

- 含义：首先在当前目录（即源文件所在的目录）中搜索头文件。如果没有找到该头文件，
  编译器会在标准的系统路径中继续查找。

- 用法：这种方式常用于包含用户自定义的头文件（非标准库头文件）。

- 搜索路径：

  1. 当前源文件所在目录。
  2. 如果在当前目录找不到头文件，编译器会在标准的包含路径（如 /usr/include/ 或
     C:\Program Files\...）中继续查找

### 2.#include \<headername\>

- 含义：编译器会直接在系统的标准路径中搜索头文件，而不检查当前目录。

- 用法：这种方式通常用于包含标准库头文件，例如 iostream、vector 等。

- 搜索路径：直接在系统的标准头文件路径中查找，不查找当前目录。

### 区别

1. 主要区别是搜索路径：
   - `#include "headername"`：先查找当前目录，然后再查找系统标准目录。
   - `#include <headername>`：只查找系统标准目录，不查找当前目录。
2. 使用场景：
   - `#include "headername"`：主要用于用户自定义的头文件，开发者可以将头文件放在
     当前项目目录中。
   - `#include <headername>`：主要用于标准库头文件或系统级头文件，编译器会从系统
     的标准路径中查找。

> 对于标准库头文件（如 `#include <iostream>`），两者的区别在很多编译器中不大，因
> 为即使你使用 `#include "iostream"`，编译器也会在标准路径中找到标准库头文件。但
> 是，规范上推荐使用 `#include <iostream>` 来包含标准库头文件，因为它更明确且可
> 以避免潜在的冲突。

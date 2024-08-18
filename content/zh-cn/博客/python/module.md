---
title: 如何理解 python 中的 module
type: blog
date: 2024-05-23
---

## 1.1 什么是 module

`module` 是一个包含 Python 代码的文件，它可以定义函数、类、变量，也可以包含可执
行的代码。模块是 Python 代码的组织单位，有助于将代码分割成更小、更可管理的部分。
换而言之, Python 中的任意 .py 文件都可以作为模块（module）来使用。

## 1.2 创建 module

一个模块就是一个 Python 文件（.py 文件），文件名即为模块名。例如，创建一个名为
my_module.py 的文件：

```python
# my_module.py

def greet(name):
    return f"Hello, {name}!"

PI = 3.14159
```

## 1.3 导入模块并使用

在另一个 Python 文件或交互式环境中，可以使用 import 语句导入模块：

```python
# main.py

import my_module

print(my_module.greet("Alice"))  # 输出: Hello, Alice!
print(my_module.PI)              # 输出: 3.14159
```

## 1.0 模块的结构和组织 --- 包(packages)

包是模块的集合，实际上是包含多个模块的目录(一个包含一些.py 文件的 folder)。包目
录中必须包含一个 `__init__.py` 文件（即使它为空），表示这是一个包。

```text
# directory structure
my_package/
    __init__.py
    module1.py
    module2.py
```

## 1.1 '**init**.py' 文件

`__init__.py` 文件用于初始化包。它可以包含初始化代码，或者用来定义包的公共接口
。Python 3.3 及以后的版本中，**init**.py 文件不是必须的，但它仍然被广泛使用

## 1.2 '**init**.py' 的功能

## 1.2.1 空的 **init**.py 文件

如果你只是想将目录标记为一个包，没有其他需求，可以将 **init**.py 文件保持为空。

```python
# __init__.py
```

## 1.2.2 初始化代码

如果你需要在包被导入时执行一些初始化代码，可以在 **init**.py 文件中编写这些代码
。例如：

```python
# __init__.py
print("Initializing the package")

# 初始化代码
def initialize():
    print("Package has been initialized")
```

## 1.2.3 定义包的公共接口

可以在 `__init__.py` 文件中导入包内的重要模块或函数，以便用户在导入包时能直接访
问这些功能。例如：

```python
# __init__.py
from .moduleA import functionA
from .moduleB import ClassB

__all__ = ['functionA', 'ClassB']
```

这里的 **all** 列表用于定义 from package import \* 时要导入的模块或对象。

## 1.2.4 将当前目录临时加入到 pythonpath 中

当 `module1` 试图引用 `module2` 时, 可能会报错 "No module named 'module2'"

```python
import os
import sys

current_dir = os.path.dirname(__file__)

if current_dir not in sys.path:
    sys.path.append(current_dir)

print("Init", __file__)
```

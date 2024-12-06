```
title: OpenGL现代编程
type: docs
```

## 描述

一般它被认为是一个 API(Application Programming Interface, 应用程序编程接口)，包
含了一系列可以操作图形、图像的函数。然而，OpenGL 本身并不是一个 API，它仅仅是一
个由 Khronos 组织制定并维护的规范(Specification)。

OpenGL 规范严格规定了每个函数该如何执行，以及它们的输出值。至于内部具体每个函数
是如何实现(Implement)的，将由 OpenGL 库的开发者自行决定（译注：这里开发者是指编
写 OpenGL 库的人）。

## OpenGL具体的库

1. 核心库
   * **OpenGl库**: 核心库提供了基本的 OpenGL 功能, 由显卡提供者提供和维护, 通常包含 opengl32.lib 和 glu32.lib
     * **GL**: 核心库, 包含基本的 OpenGL 函数
     * **GLU**: OpenGL Utility Library, 负责提供高级的图形处理函数, 如投影变换和曲面细分
   * Windows: 通常不需要额外安装 OpenGl库, 因为它们已经包含在系统中, 可以通过更新显卡驱动来获取最新版本的OpenGL支持
   * maxOS: 通常预安装 OpenGL 库
   * Linux: 可以通过包管理器来安装 OpenGL 库, 如 Ubuntu 上: `sudo apt-get install libgl1-mesa-dev`
2. 扩展库
   * **GLEW(OpenGL Extension Wrangler Library)**: 用于管理 OpenGl 扩展的库, 提供了访问最新 OpenGL 扩展功能的方法
   * **GLAC**: 轻量的 GLEW, 支持自定义加载器生成
3. 实用工具库
4. 着色器和纹理处理库
5. 数学库
6. 其他工具和库
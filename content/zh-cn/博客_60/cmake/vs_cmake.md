---
title: 在 visual studio 上如何使用 CMake 生成项目
type: blog
date: 2018-01-31
---

## 准备工作

确保系统已经安装了 Visual Studio 并且包含了 C++ 开发工具。此外，Visual Studio 自
带了 CMake 支持，所以你不需要单独安装 CMake

## 创建或获取 CMake 项目

- 已有项目：如果已有一个使用 CMake 的项目，可以直接跳到“导入项目”部分。
- 新项目：如果要从头开始创建一个项目，先创建一个包含 CMakeLists.txt 文件的目录结
  构。CMakeLists.txt 是 CMake 的配置文件，其中定义了如何构建你的项目。

## 导入项目

- 打开 Visual Studio。
- 选择 "File" > "Open" > "CMake..." 菜单项。
- 浏览并选择你的 CMakeLists.txt 文件所在的目录，然后点击 "打开" 按钮。

## 配置 CMake

- 在解决方案资源管理器中，会看到项目已经被列出来了。Visual Studio 会自动检测W
  CMakeLists.txt 文件并尝试解析它。
- 如果需要指定特定的 CMake 参数或选项，可以在 Visual Studio 的 "CMake 设置" 对话
  框中进行设置。右击解决方案资源管理器中的项目名，然后选择 "CMake Settings" 进行
  编辑。
- 在这里你可以更改生成器、配置类型（如 Debug 或 Release）、以及添加额外的 CMake
  变量等。

## 构建项目

- 一旦项目被正确识别和配置，就可以直接从 Visual Studio 内部构建项目了。点击顶
  部菜单栏的 "Build" > "Build All" 来编译整个项目。
- 也可以右击解决方案资源管理器中的具体目标（Target），然后选择 "Build" 来只构建
  该项目的目标

## 注意事项

- 确保 CMake 版本与 Visual Studio 兼容。
- 如果遇到任何问题，检查输出窗口中的错误信息，这可以帮助你快速定位问题所在。
- 使用 CMake 的高级功能可能需要更深入地了解 CMake 语法和概念。

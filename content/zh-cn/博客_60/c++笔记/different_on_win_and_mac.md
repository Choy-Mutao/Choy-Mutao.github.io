---
title: c++ 在visual studio和XCode上的差异
type: blog
date: 2021-09-18
---

## 描述

Visual Studio 和 Xcode 在处理 C++ 方面的主要差异在于它们所使用的编译器、工具链以及它们各自的集成开发环境（IDE）特性。以下是一些关键的不同点：

### 1. 编译器

- **Visual Studio** 使用的是 Microsoft 的 C++ 编译器（MSVC），该编译器有自己的语法扩展和特性，虽然它也支持大部分的 C++ 标准。
- **Xcode** 使用的是 LLVM/Clang 编译器，这是一个开源编译器，其设计目标之一就是提供清晰的诊断信息，并且它对现代 C++ 标准的支持非常好。

### 2. IDE 特性

- **Visual Studio** 提供了丰富的功能，如智能感知（IntelliSense）、实时模板编辑、重构工具等，这些都是针对微软的开发环境优化的。
- **Xcode** 也有类似的功能，如自动补全（Code Completion）、实时错误提示（Live Issue Identification）等，这些功能针对 macOS 和 iOS 开发进行了优化。

### 3. API 和库支持

- 在 **Visual Studio** 中，可以使用 Windows API 来开发应用程序，以及 Microsoft 提供的其他库。
- 在 **Xcode** 中，更可能使用 Cocoa 或 Cocoa Touch（对于 iOS 开发）API，以及 BSD 和 POSIX 的相关库。

### 4. 构建系统

- **Visual Studio** 使用 MSBuild 构建系统来管理项目。
- **Xcode** 使用自己的构建系统，不过也可以配置使用外部构建工具如 CMake。

### 5. 调试工具

- **Visual Studio** 自带强大的调试工具，如 WinDbg。
- **Xcode** 使用 LLDB 作为调试器，LLDB 提供了现代化的命令行接口和 GUI 调试体验。

### 6. 用户界面

- **Visual Studio** 的用户界面设计适合 Windows 用户，具有熟悉的 Windows 风格界面。
- **Xcode** 的用户界面则更适合 macOS 用户，遵循苹果的设计指南。

### 7. 跨平台支持

- 如果在 **Visual Studio** 中开发跨平台的 C++ 代码，可能会使用像 CMake 这样的工具来帮助管理跨平台的构建过程。
- 在 **Xcode** 中，虽然主要面向 macOS 和 iOS 开发，但也可以通过配置支持跨平台的开发，尤其是在使用像 CMake 这样的工具时。

### 总结

尽管两者在很多方面有所不同，但在编写符合 C++ 标准委员会定义的标准 C++ 代码时，这些差异并不显著。如果目标是编写可移植的 C++ 代码，应该尽量避免使用**特定于编译器**的特性，并遵循 C++ 标准。此外，使用像 CMake 这样的跨平台构建工具可以在多个平台上保持一致性。

---
title: 如何使用visual-studio开发qt项目
type: blog
date: 2020-10-16
---

## 描述

使用 Visual Studio 开发 Qt 项目是一种高效的方法，特别是对于那些已经熟悉 Visual
Studio 开发环境的开发者。以下是一个详细的步骤指南，帮助在 Visual Studio 中设置
和开发 Qt 项目。

### 步骤 1: 安装 Visual Studio

1. **下载并安装 Visual Studio**：
   - 访问 [Visual Studio 官网](https://visualstudio.microsoft.com/) 下载并安装
     Visual Studio。
   - 在安装过程中，选择“使用 C++ 的桌面开发”工作负载，这将安装必要的 C++编译器和
     工具。

### 步骤 2: 安装 Qt

1. **下载并安装 Qt**：
   - 访问 [Qt 官网](https://www.qt.io/download) 下载并安装 Qt。
   - 在安装过程中，选择需要的 Qt 版本（例如 Qt 5.x 或 Qt 6.x）和组件，包括适用
     于 Windows 的编译器（如 MinGW 或 MSVC）。

### 步骤 3: 安装 Qt VS Tools 插件

1. **安装 Qt VS Tools 插件**：
   - 打开 Visual Studio。
   - 点击 `Extensions` -> `Manage Extensions`。
   - 在搜索框中输入 `Qt VS Tools`，找到插件并安装。
   - 安装完成后，重启 Visual Studio。

### 步骤 4: 配置 Qt 版本

1. **配置 Qt 版本**：
   - 打开 Visual Studio。
   - 点击 `Tools` -> `Options`。
   - 在选项对话框中，展开 `Qt VS Tools`，然后选择 `Qt Versions`。
   - 点击 `Add` 按钮，浏览并选择安装的 Qt 版本目录。
   - 确保选择了正确的编译器版本（例如，如果使用的是 MSVC 编译器，选择对应的
     MSVC 版本）。

### 步骤 5: 创建新的 Qt 项目

1. **创建新的 Qt 项目**：

   - 点击 `File` -> `New` -> `Project`。
   - 在项目模板中，选择 `Qt` 类别下的 `Qt Widgets Application` 或其他适合的模板
     。
   - 输入项目名称和保存路径，然后点击 `Next`。

2. **选择 Qt 版本和编译器**：
   - 在下一个页面中，选择之前配置的 Qt 版本和编译器。
   - 点击 `Next`，然后点击 `Create` 完成项目创建。

### 步骤 6: 编写代码

1. **打开 main.cpp 文件**：

   - 在解决方案资源管理器中找到 `main.cpp` 文件并双击打开。

2. **编辑代码**：

   - 将默认生成的代码替换为以下内容：

   ```cpp
   #include <QApplication>
   #include <QLabel>

   int main(int argc, char *argv[])
   {
       QApplication app(argc, argv);

       QLabel label("Hello, World!");
       label.show();

       return app.exec();
   }
   ```

### 步骤 7: 构建和运行项目

1. **构建项目**：

   - 点击工具栏上的 `Build` 按钮（或按下 `Ctrl+Shift+B`）来构建项目。

2. **运行项目**：
   - 点击工具栏上的 `Start` 按钮（或按下 `F5`）来运行项目。

### 步骤 8: 查看结果

1. **查看窗口**：
   - 如果一切正常，应该会看到一个显示 “Hello, World!” 的小窗口。

### 扩展功能

1. **添加按钮**：

   - 可以通过添加按钮和其他控件来扩展应用程序的功能。例如，添加一个按钮并在点
     击时显示消息框。

   ```cpp
   #include <QApplication>
   #include <QLabel>
   #include <QPushButton>
   #include <QVBoxLayout>
   #include <QMessageBox>

   int main(int argc, char *argv[])
   {
       QApplication app(argc, argv);

       QWidget window;
       QVBoxLayout *layout = new QVBoxLayout(&window);

       QLabel *label = new QLabel("Hello, World!");
       QPushButton *button = new QPushButton("Click Me");

       layout->addWidget(label);
       layout->addWidget(button);

       QObject::connect(button, &QPushButton::clicked, [&]() {
           QMessageBox::information(&window, "Message", "Button clicked!");
       });

       window.show();

       return app.exec();
   }
   ```

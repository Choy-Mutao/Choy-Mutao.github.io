---
title: windows上开发第一个qt软件
type: blog
date: 2023-12-21
---

在 Windows 上使用 Qt 开发第一个桌面应用程序是一个很好的起点，下面是一个详细的步
骤指南，帮助你完成这一任务。我们将创建一个简单的“Hello World”应用程序。

### 步骤 1: 安装 Qt 和 Qt Creator

1. **下载 Qt 安装程序**：

   - 访问 [Qt 官方网站](https://www.qt.io/download) 并下载适用于 Windows 的在线
     安装程序。
   - 运行安装程序，按照提示选择你需要的 Qt 版本和组件。建议选择最新的稳定版 Qt
     和默认的组件。

2. **安装 Qt**：
   - 在安装向导中选择安装路径。
   - 选择要安装的组件，至少需要选择以下几项：
     - Qt
     - Tools > Qt Creator
     - Tools > MinGW（如果你没有其他编译器）

### 步骤 2: 启动 Qt Creator

1. **启动 Qt Creator**：

   - 安装完成后，启动 Qt Creator。

2. **配置 Qt Creator**：
   - 如果这是第一次启动 Qt Creator，它会引导你进行一些基本配置，包括选择 Qt 版本
     和编译器。选择你刚刚安装的 Qt 版本和 MinGW 编译器。

### 步骤 3: 创建一个新的 Qt Widgets 应用程序

1. **新建项目**：

   - 在 Qt Creator 中，点击 `File` -> `New File or Project...`。
   - 选择 `Application` 类别下的 `Qt Widgets Application`，然后点击
     `Choose...`。

2. **填写项目信息**：

   - 输入项目名称（例如 `HelloWorld`）和保存路径。
   - 点击 `Next`。

3. **选择模块**：

   - 选择所需的 Qt 模块，通常情况下默认的选择已经足够。
   - 点击 `Next`。

4. **选择套件**：

   - 选择你刚刚配置的 Qt 版本和编译器。
   - 点击 `Next`。

5. **完成创建**：
   - 点击 `Finish` 完成项目创建。

### 步骤 4: 编写代码

1. **打开 main.cpp 文件**：

   - 在项目树中找到 `main.cpp` 文件并双击打开。

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

### 步骤 5: 构建和运行项目

1. **构建项目**：

   - 点击工具栏上的 `Build` 按钮（或按下 `Ctrl+B`）来构建项目。

2. **运行项目**：
   - 点击工具栏上的 `Run` 按钮（或按下 `Ctrl+R`）来运行项目。

### 步骤 6: 查看结果

1. **查看窗口**：
   - 如果一切正常，你应该会看到一个显示 “Hello, World!” 的小窗口。

### 扩展功能

1. **添加按钮**：

   - 你可以通过添加按钮和其他控件来扩展应用程序的功能。例如，添加一个按钮并在点
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

通过以上步骤，你就可以在 Windows 上使用 Qt 创建一个简单的桌面应用程序了。希望这
对你有所帮助！如果有任何问题，欢迎随时提问。

---
title: FreeCAD 项目结构
type: docs
---

## 描述

FreeCAD 的架构由以下几个主要部分组成：

* **Core System**: 包括应用框架（基于 Python 和 C++），如 App 和 Gui 模块
* **Workbenches**: 提供特定功能的模块，例如 Part, Mesh, FEM, Draft 等
* **OpenCASCADE**: 提供几何建模核心功能，处理 NURBS 曲线、BRep 模型等
* **Python Bindings**: FreeCAD 的核心功能通过 Python 接口暴露，允许用户编写自定义脚本
* **Dependency Libraries**: 包括 Qt（GUI）、Coin3D（3D 渲染）、PySide（Python-Qt 绑定）等

## 代码目录

* src/App: 包含 FreeCAD 核心的应用逻辑（例如对象注册和序列化）
* src/Gui: 提供 GUI 功能，基于 Qt 和 Coin3D
* src/Mod: FreeCAD 的模块工作台，例如 Part, Mesh, FEM 等
* src/Base: 提供基础类和工具函数，例如日志系统、矩阵计算
* src/Tools: 包含构建工具和脚本

## 主程序入口

* 主程序入口在 src/Main/MainGui.cpp
* App 初始化在 src/App/Application.cpp 中

## 理解 FreeCAD 的工作台概念
---
title: Task.Run() 和 Task.Factory.StartNew() 的区别
type: blog
date: 2024-08-30
---

## 描述

**Task.Run** 和 **Task.Factory.StartNew** 都用于创建和启动任务，但它们有一些区别：

- *默认行为*：Task.Run 是 Task.Factory.StartNew 的一个`简化版本`，通常使用`默认的 TaskCreationOptions` 和 `TaskScheduler`。Task.Factory.StartNew 提供了更多的配置选项。

- *配置选项*：Task.Factory.StartNew 允许你设置更多的参数，比如 TaskCreationOptions 和 TaskScheduler。而 Task.Run 是为了简化任务创建，默认使用 TaskCreationOptions.DenyChildAttach 和当前线程的调度器。

- *延续性*：Task.Run 的`延续性（ContinueWith）`可以更简单地处理，因为它默认使用线程池来执行任务，适用于大多数常见的并行处理场景。

综上所述，如果你需要更多控制和配置，可以使用 Task.Factory.StartNew；而如果只是需要简单地创建和启动一个任务，Task.Run 是更方便的选择

## TaskCreationOptions

## TaskScheduler
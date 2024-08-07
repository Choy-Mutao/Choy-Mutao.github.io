---
title: C 动态分配二维数组的内存
type: blog
date: 2024-07-21
---

## 指针数组

使用指针数组, 每个指针指向一维数组的起始位置

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int rows = 3;
    int cols = 4;

    // 分配行指针数组
    double **array = (double **)malloc(rows * sizeof(double *));
    if (array == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // 为每一行分配内存
    for (int i = 0; i < rows; i++) {
        array[i] = (double *)malloc(cols * sizeof(double));
        if (array[i] == NULL) {
            printf("Memory allocation failed\n");
            // 释放已分配的内存
            for (int j = 0; j < i; j++) {
                free(array[j]);
            }
            free(array);
            return 1;
        }
    }

    // 初始化并打印二维数组
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            array[i][j] = i * cols + j;
            printf("%f ", array[i][j]);
        }
        printf("\n");
    }

    // 释放内存
    for (int i = 0; i < rows; i++) {
        free(array[i]);
    }
    free(array);

    return 0;
}
```

## 连续内存块

分配一个连续的内存块，并使用指针数组管理。

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int rows = 3;
    int cols = 4;

    // 分配行指针数组
    double **array = (double **)malloc(rows * sizeof(double *));
    if (array == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // 分配一个连续的内存块
    double *data = (double *)malloc(rows * cols * sizeof(double));
    if (data == NULL) {
        printf("Memory allocation failed\n");
        free(array);
        return 1;
    }

    // 使每个行指针指向连续内存块的对应位置
    for (int i = 0; i < rows; i++) {
        array[i] = data + i * cols;
    }

    // 初始化并打印二维数组
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            array[i][j] = i * cols + j;
            printf("%f ", array[i][j]);
        }
        printf("\n");
    }

    // 释放内存
    free(data);
    free(array);

    return 0;
}
```

## 指向指针的指针

分配一个指向指针的指针，然后分配每一行的内存.

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int rows = 3;
    int cols = 4;

    // 分配指向指针的指针
    double **array = (double **)malloc(rows * sizeof(double *));
    if (array == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // 为每一行分配内存
    for (int i = 0; i < rows; i++) {
        array[i] = (double *)malloc(cols * sizeof(double));
        if (array[i] == NULL) {
            printf("Memory allocation failed\n");
            // 释放已分配的内存
            for (int j = 0; j < i; j++) {
                free(array[j]);
            }
            free(array);
            return 1;
        }
    }

    // 初始化并打印二维数组
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            array[i][j] = i * cols + j;
            printf("%f ", array[i][j]);
        }
        printf("\n");
    }

    // 释放内存
    for (int i = 0; i < rows; i++) {
        free(array[i]);
    }
    free(array);

    return 0;
}
```

## 总结

* 方法一：适合简单的二维数组分配，但每行的内存不一定是连续的。
* 方法二：内存是连续的，适合需要频繁访问二维数组元素的情况，性能较好。
* 方法三：类似于方法一，但更灵活，可以用于更复杂的结构。
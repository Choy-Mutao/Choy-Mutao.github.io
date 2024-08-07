---
title: 在 C 函数中建议 move data to heap 时
type: blog
date: 2024-07-20
description: 在 C 语言中，将数据移动到堆内存（heap）上，可以通过动态内存分配函数来实现。这些函数包括 malloc、calloc、realloc
---

## `malloc`

`malloc`（memory allocation）函数用于分配指定字节数的内存，并返回指向这块内存的指针。内存未初始化。

```c
#include <stdlib.h>

int main() {
    // 分配内存用于存储10个整数
    int *array = (int *)malloc(10 * sizeof(int));
    if (array == NULL) {
        // 处理内存分配失败的情况
        return 1;
    }

    // 使用分配的内存
    for (int i = 0; i < 10; i++) {
        array[i] = i;
    }

    // 释放内存
    free(array);

    return 0;
}
```

## calloc

`calloc`(contiguous allocation) 函数用于分配指定数量的元素, 每个元素大小为指定字节数, 并将分配的内存初始化为 zero;

```c
#include <stdlib.h>
int main()
{
    // 分配内存用于存储 10 个整数, 并初始化为 zero
    int *array = (int*)calloc(10, sizeof(int));
    if(array == NULL)
    {
        // 处理内存分配失败的情况
        return 1;
    }

    // 使用分配的内存
    for(int i = 0; i < 10; i++>)
    {
        // array[i] 已初始化为 0
    }

    // 释放内存
    free(array);

    return 0;
}
```

## realloc

`realloc` (re-allocation) 函数用于调整之前分配的内存块的大小, 如果新的内存大于旧的内存, 新的内存部分未初始化

```c
#include <stdlib.h>

int main()
{
    // 分配内存用于存储 10 个整数
    int *array = (int *)malloc(10 * sizeof(int));
    if(array == NULL)
    {
        // 处理内存分配失败的情况
        return 1;
    }

    // 调整 内存块的大小以存储 20 个整数
    array = (int *)realloc(array, 20 * sizeof(int));
    if(array == NULL)
    {
        // 处理内存分配失败的情况
        return 1;
    }

    // 使用调整后的内存
    for(int i = 0; i < 20; i++)
    {
        array[i] = i;
    }

    // 释放内存
    free(array);

    return 0;
}
```

## Note: 注意事项

1. 内存泄漏：确保每个通过 malloc、calloc 或 realloc 分配的内存块最终都被 free 释放，否则会导致内存泄漏。
2. 空指针检查：在使用分配的内存之前，始终检查返回的指针是否为 NULL，以确保内存分配成功。
3. 内存初始化：使用 calloc 可以确保分配的内存被初始化为零，而 malloc 分配的内存则未初始化。

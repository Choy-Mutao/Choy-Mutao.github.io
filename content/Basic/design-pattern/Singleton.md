# 单例模式

## 创建模式

## 目的

保持某个对象的唯一性

## 实现方式

1. 懒汉模式

```typescript
export class Singleton {
    protected static instance: Object | undefined;
    constructor() {
        if(instance) {
            return this;
        }
    }
}
```
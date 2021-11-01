# Registry

## Abstract

注册模式： 目的是为了在应用程序中存储需要经常使用的对象实例
实现方式： 通常是使用只有静态方法的抽象类，或者是单例模式实现的类
tips： 这里的使用可能会引入全局变量，需要使用以来注入来避免出现这样的情况。

## Thinks

实际是初始化一个方便查询的字典，这个字典的特点是可以在应用程序的任意地方可以查词，且添加新词，
字典实体： map , tree, 字典的一般实现方式，
字典的索引规则：
词的实现接口规则：
词的方法的限制：

## Pratice 

---

```typescript
private static dictionary: Map<string, Object | Function> = new Map();

export class Registry {
    constructor(name: string){
        // ...
    }

    public checkIn(hashId: string, obj: Object) {
        this.dictionary.set(hashId, obj);/** 无检验注入 **/
    }
}
```

---

## Applying

* Zend framework
* Yii framework
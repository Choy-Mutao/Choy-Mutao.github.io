# 观察者模式
> 观察者模式定义了一种一对多的以来关系，让多个观察者对象同时监听一个主题对象。当这个主体对象在状态发生改变的时候，会通知所有观察对象，使他们能够自动更新自己。也称为发布-订阅模式、 模型-试图模式[DP]

## 抽象类

1. 观察者
2. 订阅者

```typescript
// TS 代码实现// 抽象观察者
interface Observer {
  response(): void;
}

// 抽象目标（通知者，变化者）
export abstract class Subject {
  protected observers: Array<Observer> = new Array<Observer>();

  public loadObserver(observer: Observer): void {
    this.observers.push(observer);
  }
  public unloadObserver(observer: Observer): void {
    this.observers.pop();
  }

  public abstract notifyObservers(): void;
}

// 具体的目标
export class ConcreteSubject extends Subject {

  public function_1() {
    // dosomething
    this.notifyObservers();
  }
  public function_2() {
    // dosomething
    this.notifyObservers();
  }

  public notifyObservers(): void {
    this.observers.forEach(observer => {
      observer.response();
    })
  }
}

// 具体的观察者1
export class ConcreteObserver1 implements Observer {
  public response() {
    console.log('Observer1 Update')
  }
}

// 具体的观察者2
export class ConcreteObserver2 implements Observer {
  public response() {
    console.log('Observer2 Update')
  }
}

/**
 * @description 这种实现方式，需要在实体对象中加载一定的Observer
 */
function Client1Job() {

  const subject = new ConcreteSubject();
  subject.loadObserver(new ConcreteObserver1())
  subject.loadObserver(new ConcreteObserver2())

  subject.function_1();
  subject.function_2();
}

Client1Job()
```

## 观察者模式中存在的不足

> 即使将通知者和观察者都进行了抽象，但是在代码中，仍然需要
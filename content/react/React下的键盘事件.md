# React 下的键盘事件

## 问题来源

```html
...
<div class="div1">
  <div class="div2">
    <list v in datalist>
      <input class="input" />
      <button class="btn"></button>
    </list>
  </div>
</div>
...
```

我希望在 `div1` 层处理键盘的监听 `onKeyDwon()`,`onKeyPress()`,`onKeyUp()`,来监听 ctrl isPressed。

因为用了 react + typescript 的 dev framework,

```tsx
export class CustomdivElement extends React.Component {
  private _handleKeyDown() {
    console.log("keydown");
  }

  private _handleKeyPress() {
    console.log("keypress");
  }

  private _handleKeyUp() {
    console.log("keyup");
  }

  render() {
    return (
      <div class="div1">
        <div class="div2">
          ...
          <list>
            <input class="input" />
            <button class="btn"></button>
          </list>
          ...
        </div>
      </div>
    );
  }
}
```

### React 下绑定键盘事件的方法

1. 绑定原生事件

```javascript
<textarea onKeyDown={(e) => {console.log(e.keyCode)}}>
```

2. 通过声明周期直接绑定到 document 的事件上面

```tsx
export class KeyBind extends React.Component {
  componentDidMount() {
    document.addEventListener("keydown", this.onKeyDown);
  }

  componentWillUnmount() {
    document.removeEventListener("keydown", this.onKeyDown);
  }

  onKeyDown = (e) => {
    switch (e.keyCode) {
      case 13: //回车事件
        break;
    }
  };
}
```

## Handling Events with React elements && Handling Events on Dom Elements

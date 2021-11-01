1. 最近在学习 React-Handling Events的时候出现了一个问题

描述： 在我 ctrl-c 了一段官网的代码后

```tsx
class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};

    // This binding is necessary to make `this` work in the callback
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState(state => ({
      isToggleOn: !state.isToggleOn
    }));
  }

  render() {
    return (
      <button onClick={this.handleClick}>
        {this.state.isToggleOn ? 'ON' : 'OFF'}
      </button>
    );
  }
}

ReactDOM.render(
  <Toggle />,
  document.getElementById('root')
);
```

visual-studio-code 提示了一个错误 `Property 'isToggleOn' does not exist on type 'Readonly<{}>'.`

意思是，参数 `isToggleON` 在 `state: Readonly<{}>` 中不存在;

在 React.Component 源码
```typescript
  interface Component<P = {}, S = {}, SS = any> extends ComponentLifecycle<P, S, SS> { }
```

所以在写 tsx 文件的时候，需要定义 `state` 的参数类型

改写就是

```tsx
class Toggle extends React.Component <any, {isToggleON: boolean}> {
  ...
}
```
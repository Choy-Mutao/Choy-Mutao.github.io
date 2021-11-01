# React 下的鼠标事件

1. 如何阻止鼠标事件onMouseOver, onMouseOut对子组件的影响。

问题回顾:

有一个页面结构如下

```html
<div id="layer1">
    ...
    <div id="layer2">
        ...
    </div>

    <div id="layer2">
        ...
    </div>
    ...
</div>
```

我要在鼠标进入 layer1 的时候，显示 mouseIn， 鼠标离开 layer1 的时候，显示 mouseOut；

在tsx文件下使用js原生事件如下

```tsx
export class CustomDiv extends React.Component{
    public _handleMouseIn(e: React.MouseEvent<HTMLDivElement>) {
        e.stopPropagation()
        // dosomething
    }
    public _handleMouseOut(e: React.MouseEvent<HTMLDivElement>) {
        e.stopPropagation()
        // dosomething
    }
    public render() {
        return(
            <div id="layer1" onMouseOver = {this._handleMouseIn} onMouseOut = {this._handleMouseOut }>
                ...
                <div id="layer2">
                    ...
                </div>

                <div id="layer2">
                    ...
                </div>
                ...
            </div>
        )
    }
}
```

这里涉及到为什么 有一行 `e.stopPropagation()`, 是为了阻止事件的向下穿透。

结果是当我在进入 第一层 的 div 后，再进入第二层的div时，会触发第一层 div 下的 mouseOut；

原因：

解决方法： 使用 React 自带的事件属性 `onMouseEnter`,`onMouseLeave`

```tsx
export class CustomDiv extends React.Component{
    public _handleMouseIn(e: React.MouseEvent<HTMLDivElement>) {
        e.stopPropagation()
        // dosomething
    }
    public _handleMouseOut(e: React.MouseEvent<HTMLDivElement>) {
        e.stopPropagation()
        // dosomething
    }
    public render() {
        return(
            <div id="layer1" onMouseEnter = {this._handleMouseIn} onMouseLeave = {this._handleMouseOut }>
                ...
                <div id="layer2">
                    ...
                </div>

                <div id="layer2">
                    ...
                </div>
                ...
            </div>
        )
    }
}
```

## React 监听键盘事件的集中方法。
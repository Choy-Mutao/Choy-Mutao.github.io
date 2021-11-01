# Threejs 中 Renderer 的 Constants

## Cull Face Modes 
[什么是 threejs 中的 face culling]()
```javascript
THREE.CullFaceNone // 关闭 face culling
THREE.CullFaceBack // default cull back faces
THREE.CullFaceFront // cull front faces
THREE.CullFaceFrontBack // cull front and back faces
```

## Shadow Types
[什么是 threejs 中的 shadow]()

这些主要用于 `WebGLRender` 的 `shadowMap.type` 属性的设置

```javascript
THREE.BasicShadowMap // 提供了一个未经过筛选的 shadow maps --- 很快，但是很没质量
THREE.PCFShadowMap // 使用 PCF 算法过滤的 shadow maps --- 这个是默认的
THREE.PCFSoftShadowMap // 使用 PCF 算法过滤的 shadow maps 但有更柔和的光影效果。 --- 尤其在使用第分辨率的阴影贴图的时候。
THREE.VSMShadowMap // 使用 VSM 算法过滤的 shadow maps --- 在这个模式下，所有的 shadow receivers 也会反射 shadow
```

## Tone Mapping
[什么是 theeejs 中的 tone]()

这些主要用于 `WebGLRender` 的 `toneMapping` 属性的设置

> 这部分的设置和 HDR 相关。

```javascript
THREE.NoToneMapping
THREE.LinearToneMapping
THREE.ReinhardToneMapping
THREE.CineonToneMapping
THREE.ACESFilmicToneMapping
```


### References： 
* [ 什么是HDR ]()
* [ 详解 PCF 算法 ]()
* [ 详解 VSM 算法 ]()
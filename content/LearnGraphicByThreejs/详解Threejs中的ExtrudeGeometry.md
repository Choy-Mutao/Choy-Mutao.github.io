---
title: "详解Treejs.ExtrudeGeomety"
date: 2021-07-05T18:15:44+08:00
draft: true
---

## ExtrudeGeometry(shapes : Array, options : Object)

shapes — 形状的轮廓线（2D）
options — 操作参数包含一下项目：.

```typescript
options = {
    curveSegments — int. Number of points on the curves. Default is 12.
    steps — int. Number of points used for subdividing segments along the depth of the extruded spline. Default is 1.
    depth — float. Depth to extrude the shape. Default is 100.
    bevelEnabled — bool. Apply beveling to the shape. Default is true.
    bevelThickness — float. How deep into the original shape the bevel goes. Default is 6.
    bevelSize — float. Distance from the shape outline that the bevel extends. Default is bevelThickness - 2.
    bevelOffset — float. Distance from the shape outline that the bevel starts. Default is 0.
    bevelSegments — int. Number of bevel layers. Default is 3.
    extrudePath — THREE.Curve. A 3D spline path along which the shape should be extruded. Bevels not supported for path extrusion.
    UVGenerator — Object. object that provides UV generator functions
}
```

## 拉伸的理论图解

将shapes中的2D轮廓离散化

![2D-discretization.png](.\assets\2D-discretization.png)

将shapes沿空间曲线扫掠

![3D-sweepint&discretization.png](.\assets\3D-sweepint&discretization.png)

## 代码实现分析

```typescript
  super();

  this.type = 'ExtrudeGeometry';

  // 参数数据
  this.parameters = {
   shapes: shapes,
   options: options
  };

  shapes = Array.isArray(shapes) ? shapes : [shapes];

  const scope = this;

  const verticesArray = [];
  const uvArray = [];

  for (let i = 0, l = shapes.length; i < l; i++) {

   const shape = shapes[i];
   addShape(shape); // 主要数据计算方法

  }

  // build geometry

  this.setAttribute('position', new Float32BufferAttribute(verticesArray, 3));
  this.setAttribute('uv', new Float32BufferAttribute(uvArray, 2));

  this.computeVertexNormals();
```

## addshape 数据的准备和计算

```typescript
    // step one

   let splineTube, binormal, normal, position2;
   if (extrudePath) { 

    extrudePts = extrudePath.getSpacedPoints(steps); // 扫掠路径的离散点

    extrudeByPath = true;
    bevelEnabled = false;

    splineTube = extrudePath.computeFrenetFrames(steps, false); // 延扫掠路径上的 frenet-frames

    binormal = new Vector3(); // 初始化副法线
    normal = new Vector3(); // 初始化主法线
    position2 = new Vector3(); // 初始化点坐标

   }

   // Safeguards if bevels are not enabled

   if (!bevelEnabled) {

    bevelSegments = 0;
    bevelThickness = 0;
    bevelSize = 0;
    bevelOffset = 0;

   }
```

> extrudePath 和 bevel不会共存

```typescript
// step two
```

```typescript
// inner function
// 2d 点的偏移
function scalePt2(pt, vec, size) {
    //...
}

// 2d 点的切线
function getBevelVec(inPt, inPrev, inNext) {
    //...
}

// 画顶面
function buildLidFaces() {
    //...
}

// 画边面
function buildSideFaces() {
    //...
}

// 画边面
function sidewalls(contour, layeroffset) {
    //...
}

```

## 对网格的拓扑关系处理的好方法

```typescript
// 临时存储点的位置信息，同时记录点的序列
   function v(x, y, z) {
    placeholder.push(x); // point3D.x
    placeholder.push(y); // point3D.y
    placeholder.push(z); // point3D.z
   }

// a,b,c 是网格化后的点的index
   function f3(a, b, c) {

    addVertex(a);
    addVertex(b);
    addVertex(c);

    const nextIndex = verticesArray.length / 3;
    const uvs = uvgen.generateTopUV(scope, verticesArray, nextIndex - 3, nextIndex - 2, nextIndex - 1);

    addUV(uvs[0]);
    addUV(uvs[1]);
    addUV(uvs[2]);

   }
// a,b,c,d 是网格化后的点的index
   function f4(a, b, c, d) {

    addVertex(a);
    addVertex(b);
    addVertex(d);

    addVertex(b);
    addVertex(c);
    addVertex(d);


    const nextIndex = verticesArray.length / 3;
    const uvs = uvgen.generateSideWallUV(scope, verticesArray, nextIndex - 6, nextIndex - 3, nextIndex - 2, nextIndex - 1);

    addUV(uvs[0]);
    addUV(uvs[1]);
    addUV(uvs[3]);

    addUV(uvs[1]);
    addUV(uvs[2]);
    addUV(uvs[3]);

   }

// 从临时存储空间中 取得准确的空间位置信息，放入verticesArray中
   function addVertex(index) {

    verticesArray.push(placeholder[index * 3 + 0]);
    verticesArray.push(placeholder[index * 3 + 1]);
    verticesArray.push(placeholder[index * 3 + 2]);

   }


   function addUV(vector2) {

    uvArray.push(vector2.x);
    uvArray.push(vector2.y);

   }
```

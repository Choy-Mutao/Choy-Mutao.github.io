## Inference 和 Promise.all 的改进

最近发布的 3.7 版本主要更新了对 `Promise.all` 和 `Promise.race` 的描述。 但不巧的是，这部分引入了一些版本回退， 尤其在联合类型中使用 `null` 和 `undefined` 时。

```typescript
interface Lion {
  roar(): void;
}

interface Seal {
  singKissFromARose(): void;
}

async function visitZoo(
  lionExhibit: Promise<Lion>,
  sealExhibit: Promise<Seal | undefined>
) {
  let [lion, seal] = await Promise.all([lionExhibit, sealExhibit]);
  lion.roar(); // uh oh
  //  ~~~~
  // Object is possibly 'undefined'.
}
```

这里得到了一个很奇怪的结果。

## 新加了两个注解 `//@ts-expect-error` & `//@ts-ignore`
Pick ts-expect-error if:

you’re writing test code where you actually want the type system to error on an operation
you expect a fix to be coming in fairly quickly and you just need a quick workaround
you’re in a reasonably-sized project with a proactive team that wants to remove suppression comments as soon affected code is valid again
Pick ts-ignore if:

you have an a larger project and and new errors have appeared in code with no clear owner
you are in the middle of an upgrade between two different versions of TypeScript, and a line of code errors in one version but not another.
you honestly don’t have the time to decide which of these options is better.



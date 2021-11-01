[toc]

# 基于Hugo在GitPage上部署Blog

## Hugo官方文档 [*Host On Github*](https://gohugo.io/hosting-and-deployment/hosting-on-github/)

关键提炼三个要点
1. 本地git版本在2.8及以上
2. 有个githu账户
3. 有个hugo项目

简单介绍一些 Github Pages的两种类型

1. User/Organization Pages
2. Project Pages

重要信息:
> GitHub 执行您的软件开发工作流程。每次将代码推送到 Github 存储库时，Github Actions 都会自动构建站点。
> 在 .github/workflows/gh-pages.yml 中创建一个包含以下内容的文件（基于 actions-hugo）：
```yml
name: github pages

on:
  push:
    branches:
      - main  # Set a branch to deploy
  pull_request:

jobs:
  deploy:
    runs-on: ubuntu-20.04
    steps:
      - uses: actions/checkout@v2
        with:
          submodules: true  # Fetch Hugo themes (true OR recursive)
          fetch-depth: 0    # Fetch all history for .GitInfo and .Lastmod

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'
          # extended: true

      - name: Build
        run: hugo --minify

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        if: github.ref == 'refs/heads/main'
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```


## 在Github上开启GitPage服务

## 设计仓库branch 
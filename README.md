# インタラクティブ教科書

MDXを原稿として使い、概念を操作しながら理解できるWeb教科書です。Astroで静的HTMLへ生成し、GitHub Pagesで公開します。

## 開発

```bash
npm ci
npm run dev
```

本番ビルドは `npm run build`、ローカル確認は `npm run preview` です。

## 執筆

通常の本文は `src/pages/` のMDXに書きます。動かすことが理解につながる箇所は `src/components/` にインタラクティブ教材として実装し、MDXから読み込みます。Webサイトが正本ですが、本文とコンポーネントを分離し、文章の差分を読みやすく保ちます。

## 公開

`master` へのpushを契機にGitHub Actionsがビルドし、GitHub Pagesへデプロイします。リポジトリの Settings → Pages → Build and deployment で Source を **GitHub Actions** に設定してください。

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

https://fukuya-fs.com — 飲食店専門のSNS・MEOコンサルティング「Fukuya Food & SNS Consulting」の1ページ完結型LP。個人事業主のサイト。もともとAntigravityで開発され、Claude Codeに移行した。

## 構成

ビルド工程なしの純粋な静的サイト。フレームワーク・パッケージマネージャ・テストは存在しない。

- `index.html` — サイト全体(マークアップ・スタイル・JSすべてこの1ファイルに集約)
- `thanks.html` — フォーム送信後のサンクスページ(Netlifyが `/thanks` で配信)
- `styles.css` — スクロールバー等の補助スタイルのみ(ほぼ未使用。主要スタイルはindex.html内)
- `images/fukuya-logo.png` — ロゴ(168×168px。元の2048px版は必要ならユーザーに確認)
- `images/ogp.png` — OGP画像(1200×630px)
- `images/profile-avatar.svg` — 代表プロフィール用の架空男性イラスト(顔写真を使わない方針のため)
- `robots.txt` / `sitemap.xml` — SEO用。ページを追加したらsitemap.xmlにも追記すること

### index.html の内部構造

- **Tailwind CSS を CDN(`cdn.tailwindcss.com`)で読み込み**、`<head>` 内のインラインスクリプトで `tailwind.config` を定義。カスタムカラーは `fukuya-*`(dark / orange / blue など)、アニメーションは float / fadeUp / kenburns
- **AOS(Animate On Scroll)** をCDNで読み込み、末尾の `<script>` で初期化。スクロールアニメーションは `data-aos` 属性で制御
- セクション構成(id): `pain` → `worldview` → `pricing` → `spots` → `reasons` → `promises` → `profile` → `faq` → `contact`
- `<head>` にJSON-LD構造化データが2つ(ProfessionalService と FAQPage)ある。**FAQセクションの文言を変えたらFAQPage JSON-LDも必ず同期させること**(Googleのガイドラインで表示内容と一致が必須)
- 代表者は寺島久雄(サイト上に公開済み。顔写真は使わない方針)
- 末尾のインラインJS: AOS初期化とスマホメニュー(`#menu-btn` / `#mobile-menu`)の開閉のみ

### お問い合わせフォーム(重要)

`#contact` のフォームは **Netlify Forms** を使用(`data-netlify="true"`、honeypot付き、`action="/thanks"`)。ホスティングはNetlify。フォームを編集する際は `name="contact"`、`data-netlify` 属性、hidden の `form-name` フィールドを壊さないこと。

## 開発方法

ビルド不要。ローカル確認は index.html をブラウザで開くか、簡易サーバーを立てる:

```
python -m http.server 8000
```

※ Netlify Forms はローカルでは動作しない(送信テストは本番/Netlifyプレビューでのみ可能)。

## デプロイ(重要)

GitHub `terra369369/fukuya-website` の **mainブランチにプッシュすると、Netlifyが自動で本番(fukuya-fs.com)にデプロイする**(2026-07-20連携設定済み。ビルドコマンドなし・ルート配信)。つまりmainへのプッシュ=即本番公開。未確認の変更はブランチを切って作業し、プッシュ前に必ずローカルで表示確認すること。

## 既知の問題

- Tailwind CDN版は本番利用非推奨(公式警告あり)。将来的にはビルド版への移行を検討

## 履歴メモ

2026-07-20の移行時、`index.html` の `#spots` セクション周辺がタグ破損で消失していたため、本番サイト(fukuya-fs.com)の公開版を参照して復元した。メニュー作成 ¥35,000 / LP作成 ¥59,800〜 という価格は本番版から引き継いだもの。

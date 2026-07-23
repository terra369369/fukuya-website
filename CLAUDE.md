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
- セクション構成(id): `pain` → `worldview` → `pricing` → `spots` → `apps` → `reasons` → `promises` → `profile` → `faq` → `contact`
- `<head>` にJSON-LD構造化データが2つ(ProfessionalService と FAQPage)ある。**FAQセクションの文言を変えたらFAQPage JSON-LDも必ず同期させること**(Googleのガイドラインで表示内容と一致が必須)
- 代表者は寺島久雄(サイト上に公開済み。顔写真は使わない方針)
- **対応エリアポリシー(2026-07-23決定):** 撮影・対面を伴うサービス(スタンダードプラン/メニュー・LP制作)は東京都内・神奈川・埼玉・千葉(一部地域は要相談)。ライトプランとアプリ開発は全国オンライン対応。エリア表記はヒーロー・料金カード・スポット注記・FAQ・JSON-LD(areaServed)・プロフィールに分散しているので、変更時はすべて同期させること
- **アプリ開発の公開価格(2026-07-23決定):** オーダーメイド開発 初期¥300,000〜(税抜・個別見積)/月額運用・保守¥15,000〜(税抜)。自社アプリは「開発中・近日公開」のジャンル予告のみ(詳細・名称はリリースまで非公開)
- 売りの軸:「毎日最新AIで市場・アルゴリズムを分析する根拠のあるSNS運用」。誇大表現(「必ず伸びる」等)は景表法リスクがあるため使わない
- 末尾のインラインJS: AOS初期化とスマホメニュー(`#menu-btn` / `#mobile-menu`)の開閉のみ

### お問い合わせフォーム(重要)

`#contact` のフォームは **FormSubmit**(formsubmit.co)を使用。送信先は `info@fukuya-fs.com`(Google Workspace)。フォームを編集する際は以下を壊さないこと:

- `action="https://formsubmit.co/info@fukuya-fs.com"`
- hidden フィールド: `_subject`(メール件名)/ `_next`(送信後リダイレクト先 = thanks.html)/ `_captcha=false` / `_template=table`
- honeypot: `name="_honey"` の隠し入力欄(スパム対策)
- 送信者メール欄は `name="email"` のままにする(FormSubmitが自動でReply-Toに設定する)

※ 2026-07-20まではNetlify Formsを使用していたが、フォーム検出が無効でずっと不通だったことが判明し、GitHub Pages移行と同時にFormSubmitへ置き換えた。

## 開発方法

ビルド不要。ローカル確認は index.html をブラウザで開くか、簡易サーバーを立てる:

```
python -m http.server 8000
```

※ フォーム(FormSubmit)への実送信テストは本番でのみ行うこと。

## デプロイ(重要)

ホスティングは **GitHub Pages**(リポジトリ `terra369369/fukuya-website`、**公開リポジトリ**、mainブランチ/ルート配信、カスタムドメイン fukuya-fs.com)。**mainにプッシュすると自動で本番に反映される**(通常1〜2分)。つまりmainへのプッシュ=即本番公開。未確認の変更はブランチを切って作業し、プッシュ前に必ずローカルで表示確認すること。

- リポジトリ直下の `CNAME` ファイル(GitHubが自動管理)を削除しないこと
- DNSはWix管理(ネームサーバー wixdns.net)。メール(MX)はGoogle Workspace — サイト移設時もMXレコードには触れないこと
- 旧ホスティングはNetlify(2026-07-20まで。クレジット枯渇でデプロイ不能になりGitHub Pagesへ移行した)

## 既知の問題

- Tailwind CDN版は本番利用非推奨(公式警告あり)。将来的にはビルド版への移行を検討

## 履歴メモ

2026-07-20の移行時、`index.html` の `#spots` セクション周辺がタグ破損で消失していたため、本番サイト(fukuya-fs.com)の公開版を参照して復元した。メニュー作成 ¥35,000 / LP作成 ¥59,800〜 という価格は本番版から引き継いだもの。

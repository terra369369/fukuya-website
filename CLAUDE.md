# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

https://fukuya-fs.com — 飲食店専門のSNS・MEOコンサルティング「Fukuya Food & SNS Consulting」の1ページ完結型LP。個人事業主のサイト。もともとAntigravityで開発され、Claude Codeに移行した。

## 構成

ビルド工程なしの純粋な静的サイト。フレームワーク・パッケージマネージャ・テストは存在しない。

- `index.html` — サイト全体(マークアップ・スタイル・JSすべてこの1ファイルに集約)
- `thanks.html` — フォーム送信後のサンクスページ
- `sns.html` / `lp.html` / `app.html` / `menu.html` — サービス別ページ(2026-09-03新設。検索語の受け皿)。**手で編集せず `tools/gen_service_pages.py` のPAGESデータを直して `python tools/gen_service_pages.py` で再生成する**(FAQPage/Service/Breadcrumb JSON-LDは同一データから自動生成されるため常に一致)。価格・エリア・プラン内容を変えたらindex.html・llms.txtと同時にこちらも更新
- `privacy.html` — プライバシーポリシー+免責事項(フォーム脇とフッターからリンク)。特商法表記はオンライン決済がないため意図的に未掲載(住所・電話の公開回避)。アプリ正式リリース時は利用規約・アプリ用ポリシー等が別途必要
- `styles.css` — スクロールバー等の補助スタイルのみ(ほぼ未使用。主要スタイルはindex.html内)
- `images/fukuya-logo.png` — ロゴ(168×168px。元の2048px版は必要ならユーザーに確認)
- `images/ogp.png` — OGP画像(1200×630px)
- `images/profile-avatar.png` — 代表プロフィール用の男性イラストアイコン(顔写真を使わない方針のため。336×336px、元画像1000pxはユーザーのDownloadsに)
- `robots.txt` / `sitemap.xml` — SEO用。ページを追加したらsitemap.xmlにも追記すること。robots.txtはAIクローラー(GPTBot等)を明示許可している
- `llms.txt` — AI検索(LLM)向けの事業サマリー。**サービス内容・価格を変更したらこのファイルも必ず同期すること**

### index.html の内部構造

- **Tailwind CSS を CDN(`cdn.tailwindcss.com`)で読み込み**、`<head>` 内のインラインスクリプトで `tailwind.config` を定義。カスタムカラーは `fukuya-*`(dark / orange / blue など)、アニメーションは float / fadeUp / kenburns
- **AOS(Animate On Scroll)** をCDNで読み込み、末尾の `<script>` で初期化。スクロールアニメーションは `data-aos` 属性で制御
- セクション構成(id): `pain` → `worldview` → `pricing`(SNSプラン) → `lp`(LP制作。AIO標準搭載の訴求バンドあり) → `apps` → `menu`(メニュー作成) → `reasons` → `promises` → `profile` → `faq` → `contact`。※2026-08-02にサービス順を「SNS→LP→アプリ→メニュー」に再編。旧id `spots` は廃止
- 世界観の軸: 「IT会社でも広告代理店でもなく、飲食の現場出身」という差別化。ヒーローのバッジ・painセクション末尾・各サービスのキャッチ・プロフィールで一貫させる
- `<head>` にJSON-LD構造化データが2つ(ProfessionalService と FAQPage)ある。**FAQセクションの文言を変えたらFAQPage JSON-LDも必ず同期させること**(Googleのガイドラインで表示内容と一致が必須)
- 代表者は寺島久雄(サイト上に公開済み。顔写真は使わない方針)
- **対応エリアポリシー(2026-07-23決定):** 撮影・対面を伴うサービス(スタンダードプラン/メニュー・LP制作)は東京都内・神奈川・埼玉・千葉(一部地域は要相談)。ライトプランとアプリ開発は全国オンライン対応。エリア表記はヒーロー・料金カード・スポット注記・FAQ・JSON-LD(areaServed)・プロフィールに分散しているので、変更時はすべて同期させること
- **アプリ開発の公開価格(2026-07-23決定):** オーダーメイド開発 初期¥300,000〜(税抜・個別見積)/月額運用・保守¥15,000〜(税抜)
- **自社アプリの掲載ポリシー(2026-08-21更新):** スマ仕入(sumaden.fukuya-fs.com=納品書読取・原価計算)/スマ売上(sumauriage.fukuya-fs.com=売上伝票撮影・自動集計/ローカル: C:\antigravity-app\fukuya-check-app)/スマ棚(sumadana.fukuya-fs.com=音声棚卸/ローカル: C:\antigravity-app\fukuya-inventory-app)の3本とも、名称・内容・リンクの紹介はOK。ただし**クライアント向けモニター提供段階で一般販売は未開始**のため、料金は載せず「モニター提供中・一般提供は準備中」と表記すること。アプリを追加・変更したらllms.txtも同期
- **LP制作の公開価格(2026-08-02改定):** 初回制作費¥69,800(税抜。企画・原稿作成/デザイン・スマホ対応/AI検索(AIO)・SEO・MEO対策一式/公開設定)+月額¥9,800(税抜。維持・管理/メニュー・写真の月次更新)。相場比較の出典: Web幹事・STOCK SUN等 2026年(相場を盛らないこと)。価格変更時はFAQ表示・FAQPage/ProfessionalService JSON-LDも同期
- **スタンダードプランの内容(2026-08-02改定):** 撮影 月1〜2回/Instagram投稿・リール運用代行 週2〜3回/月1回オンラインMTG/ライトプラン全内容包含。**MEO情報更新・口コミ管理はプラン内容から削除済み**(MEOの分析・レポートはライトプラン側に含まれる)。個別外注比較は「SNS運用10〜30万+撮影1回2〜5万=月12万前後〜」ベース
- **料金の見せ方(2026-08-02統一):** 全サービス(ライト/スタンダード/メニュー/LP)を「左=一般相場の価格帯リスト(グレー)/右=FUKUYA強調カード(黒+ゴールド、バッジ付き)」の比較レイアウトで統一
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
- DNSは**Cloudflare管理**(2026-08-02にWixから移管。スマ仕入のサブドメイン運用のため)。メール(MX)はGoogle Workspace — MXレコードには触れないこと。本体サイトのA/CNAMEはプロキシOFF(DNS only)のままにすること(GitHub Pagesの証明書更新のため)
- サブドメイン `sumaden.fukuya-fs.com` = 自社アプリ「スマ仕入」(納品書読み取り・原価計算)。別リポジトリ `terra369369/fukuya-smaden`(ローカル: C:\fukuya-smaden、Cloudflare Workers+OpenNext、デプロイは `npm run deploy:cf`)
- 旧ホスティングはNetlify(2026-07-20まで。クレジット枯渇でデプロイ不能になりGitHub Pagesへ移行した)

## 既知の問題

- Tailwind CDN版は本番利用非推奨(公式警告あり)。将来的にはビルド版への移行を検討

## 履歴メモ

2026-07-20の移行時、`index.html` の `#spots` セクション周辺がタグ破損で消失していたため、本番サイト(fukuya-fs.com)の公開版を参照して復元した。メニュー作成 ¥35,000 / LP作成 ¥59,800〜 という価格は本番版から引き継いだもの。

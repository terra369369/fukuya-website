# -*- coding: utf-8 -*-
"""サービス別ページ(sns/lp/app/menu)を共通テンプレート+ページ別データから生成する。
FAQPage JSON-LD は表示FAQと同じデータから自動生成するので不整合が起きない。"""
import json, html

OUT = r"C:\fukuya-website"
BASE = "https://fukuya-fs.com"
AREA = "東京都内・神奈川・埼玉・千葉（一部地域は要相談）"
SOURCE_NOTE = "※ 価格はすべて税抜表記です。※ 相場は Web幹事・STOCK SUN等のWeb制作費用調査（2026年）ほか、制作会社・代理店・クラウドソーシング等の公開料金をもとにした当社調べの目安です。"

NAV = [("index.html", "トップ"), ("sns.html", "SNS運用代行"), ("lp.html", "LP制作"), ("app.html", "アプリ開発"), ("menu.html", "メニュー作成")]

CHECK = '<span style="color:#c8a97e" class="mt-0.5 flex-shrink-0 font-bold">✓</span>'

def head(p):
    ld = [p["service_ld"], p["faq_ld"], p["breadcrumb_ld"]]
    ld_html = "\n".join(f'    <script type="application/ld+json">\n{json.dumps(d, ensure_ascii=False, indent=4)}\n    </script>' for d in ld)
    return f'''<!DOCTYPE html>
<html lang="ja" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(p["title"])}</title>
    <meta name="description" content="{html.escape(p["description"])}">
    <link rel="canonical" href="{BASE}/{p["file"]}">
    <link rel="icon" type="image/png" href="images/fukuya-logo.png">
    <link rel="apple-touch-icon" href="images/fukuya-logo.png">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="Fukuya Food &amp; SNS Consulting">
    <meta property="og:title" content="{html.escape(p["og_title"])}">
    <meta property="og:description" content="{html.escape(p["description"])}">
    <meta property="og:url" content="{BASE}/{p["file"]}">
    <meta property="og:image" content="{BASE}/images/ogp.png">
    <meta property="og:locale" content="ja_JP">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Noto+Sans+JP:wght@300;400;500;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{ theme: {{ extend: {{
            fontFamily: {{ sans: ['"Noto Sans JP"', '"Inter"', 'sans-serif'] }},
            colors: {{ fukuya: {{ blue: '#1a1a2e', light: '#f5f5f5', orange: '#c8a97e', dark: '#0a0a0a', gray: '#f9f9f9', sand: '#fafafa', warm: '#f7f4f0', accent: '#b8985a', mid: '#6b6b6b' }} }}
        }} }} }}
    </script>
    <style>
        :root {{ --gold: #9a8060; }}
        * {{ box-sizing: border-box; }}
        h1, h2, h3 {{ letter-spacing: 0.06em; font-weight: 700; }}
        .label-tag {{ letter-spacing: 0.28em; font-size: 0.62rem; font-weight: 700; text-transform: uppercase; }}
        .gold-line {{ width: 32px; height: 1px; background: var(--gold); display: inline-block; }}
        section {{ padding-top: 5rem; padding-bottom: 5rem; }}
        @media (min-width: 768px) {{ section {{ padding-top: 7rem; padding-bottom: 7rem; }} }}
        @media (max-width: 640px) {{ h2 {{ font-size: 1.45rem !important; line-height: 1.45 !important; }} h3 {{ font-size: 1.1rem !important; }} p {{ line-height: 1.8 !important; }} }}
        details summary::-webkit-details-marker {{ display: none; }}
        details summary {{ list-style: none; }}
    </style>
{ld_html}
</head>'''

def header(p):
    links = "".join(
        f'<a href="{h}" class="text-xs font-medium tracking-widest transition {"text-fukuya-dark" if h == p["file"] else "text-gray-400 hover:text-fukuya-dark"}">{t}</a>'
        for h, t in NAV)
    return f'''
<body class="bg-white text-fukuya-dark antialiased leading-relaxed font-sans">
    <header class="bg-white/98 backdrop-blur-md border-b border-gray-100 sticky top-0 z-50">
        <div class="container mx-auto px-4 py-3 md:py-4 flex items-center justify-between max-w-6xl gap-4">
            <a href="index.html" class="flex items-center gap-x-3 hover:opacity-70 transition flex-shrink-0">
                <img src="images/fukuya-logo.png" alt="Fukuya 飲食店専門デジタルパートナー" class="h-10 md:h-12 w-auto object-contain">
                <span class="flex flex-col leading-tight">
                    <span class="text-sm md:text-base font-bold text-fukuya-dark tracking-widest">Fukuya</span>
                    <span class="text-[9px] font-medium text-gray-400 tracking-[0.2em] uppercase">Food &amp; SNS Consulting</span>
                </span>
            </a>
            <nav class="hidden lg:flex items-center gap-6">{links}</nav>
            <a href="index.html#contact" class="inline-flex items-center justify-center bg-fukuya-dark text-white px-4 md:px-5 py-2.5 text-xs font-medium tracking-[0.15em] hover:bg-fukuya-orange transition-all whitespace-nowrap">無料診断を予約</a>
        </div>
    </header>

    <!-- パンくず -->
    <div class="container mx-auto px-6 max-w-5xl pt-5">
        <nav aria-label="パンくず" class="text-[11px] text-gray-400 tracking-wider">
            <a href="index.html" class="hover:text-fukuya-dark transition">トップ</a><span class="mx-2">/</span><span class="text-gray-600">{p["short"]}</span>
        </nav>
    </div>'''

def hero(p):
    return f'''
    <!-- ヒーロー -->
    <section class="bg-white" style="padding-top:3rem">
        <div class="container mx-auto px-6 max-w-5xl">
            <div class="max-w-3xl">
                <div class="inline-flex items-center gap-3 mb-5">
                    <span class="gold-line"></span>
                    <span class="label-tag text-fukuya-mid tracking-[0.2em]">{p["label"]}</span>
                </div>
                <h1 class="text-2xl md:text-4xl font-bold text-fukuya-dark mb-5" style="line-height:1.4">{p["h1"]}</h1>
                <p class="text-sm md:text-base text-gray-600 font-light leading-relaxed mb-5">{p["lead"]}</p>
                <p class="text-xs text-gray-400 font-light border-l-2 pl-3 mb-8" style="border-color:#9a8060">{p["area_line"]}</p>
                <div class="flex flex-col sm:flex-row gap-3">
                    <a href="index.html#contact" class="inline-flex items-center justify-center gap-2 bg-fukuya-orange text-white px-7 py-3.5 font-medium tracking-widest hover:bg-fukuya-accent transition-all text-sm">無料相談を予約する →</a>
                    <a href="#pricing" class="inline-flex items-center justify-center border border-fukuya-dark text-fukuya-dark px-7 py-3.5 text-sm font-light tracking-widest hover:bg-fukuya-dark hover:text-white transition-all">料金を見る</a>
                </div>
                <p class="mt-4 text-gray-400 text-xs tracking-widest">✓ 今すぐの契約不要　✓ 無理な営業なし</p>
            </div>
        </div>
    </section>'''

def pains(p):
    cards = "".join(f'''
                <div class="bg-gray-50 border border-gray-100 p-6">
                    <div class="text-2xl mb-3">{e}</div>
                    <h3 class="font-bold text-base mb-2 text-fukuya-dark">{t}</h3>
                    <p class="text-gray-500 leading-relaxed text-sm font-light">{d}</p>
                </div>''' for e, t, d in p["pains"])
    return f'''
    <!-- お悩み -->
    <section class="bg-fukuya-warm">
        <div class="container mx-auto px-6 max-w-5xl">
            <div class="text-center mb-10">
                <span class="label-tag text-gray-400 block mb-3">お悩み</span>
                <h2 class="text-2xl md:text-3xl font-bold text-fukuya-dark">{p["pain_title"]}</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">{cards}
            </div>
            <div class="mt-10 text-center">
                <div class="inline-block bg-fukuya-dark text-white px-7 py-5 max-w-xl">
                    <p class="font-bold text-sm md:text-base text-gray-200 mb-1">{p["pain_close_main"]}</p>
                    <p class="text-gray-400 text-xs font-light">IT会社でも広告代理店でもなく、"飲食の現場出身"。20年の現場経験を持つ右腕が伴走します。</p>
                </div>
            </div>
        </div>
    </section>'''

def features(p):
    blocks = "".join(f'''
                <div class="bg-white border border-gray-200 p-7 md:p-8">
                    <h3 class="text-lg font-bold text-fukuya-dark mb-4">{t}</h3>
                    <ul class="space-y-2.5 text-sm">{"".join(f'<li class="flex items-start gap-3">{CHECK}<span class="text-gray-600 font-light">{i}</span></li>' for i in items)}</ul>
                </div>''' for t, items in p["features"])
    cols = "md:grid-cols-2" if len(p["features"]) == 2 else "md:grid-cols-1 max-w-2xl mx-auto"
    extra = p.get("features_extra", "")
    return f'''
    <!-- サービス内容 -->
    <section class="bg-white">
        <div class="container mx-auto px-6 max-w-5xl">
            <div class="text-center mb-10">
                <div class="inline-flex items-center gap-3 mb-5"><span class="gold-line"></span><span class="label-tag text-fukuya-mid tracking-[0.2em]">SERVICE</span><span class="gold-line"></span></div>
                <h2 class="text-2xl md:text-3xl font-bold text-fukuya-dark mb-3">{p["features_title"]}</h2>
                <p class="text-sm text-gray-500 font-light max-w-xl mx-auto leading-relaxed">{p["features_lead"]}</p>
            </div>
            <div class="grid grid-cols-1 {cols} gap-6">{blocks}
            </div>{extra}
        </div>
    </section>'''

def compare(title, sub, rows, card, badge_label="FUKUYA"):
    row_html = ""
    for i, (lab, val, note) in enumerate(rows):
        border = "" if i == len(rows) - 1 else " border-b border-gray-200"
        v = f'<span class="text-sm text-gray-500">{val}</span>' + (f'<span class="block text-[10px] text-gray-400 font-light">{note}</span>' if note else "")
        row_html += f'''
                    <li class="flex items-baseline justify-between gap-4 py-3{border}">
                        <span class="text-sm text-gray-600 font-light flex-shrink-0">{lab}</span>
                        <span class="text-right">{v}</span>
                    </li>'''
    items = "".join(f'<li class="flex items-start gap-3">{CHECK}<span class="text-gray-300 font-light">{i}</span></li>' for i in card["items"])
    return f'''
            <div class="mb-12">
                <div class="text-center mb-8">
                    <h3 class="text-xl md:text-2xl font-bold text-fukuya-dark mb-2">{title}</h3>
                    <p class="text-sm text-gray-500 font-light">{sub}</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-stretch">
                    <div class="bg-gray-50 border border-gray-100 p-7 md:p-8">
                        <p class="label-tag text-gray-400 tracking-[0.15em] mb-5">{card["rows_label"]}</p>
                        <ul>{row_html}
                        </ul>
                    </div>
                    <div class="bg-fukuya-dark text-white p-7 md:p-8 flex flex-col relative">
                        <div class="absolute top-6 right-6"><span class="label-tag tracking-[0.15em]" style="color:#c8a97e">{badge_label}</span></div>
                        <p class="mb-4"><span class="inline-block bg-fukuya-orange text-white text-[10px] font-bold px-2.5 py-1 tracking-wider">{card["badge"]}</span></p>
                        <p class="text-xs text-gray-400 font-light mb-1">{card["price_label"]}</p>
                        <div class="flex items-end gap-2 mb-5">
                            <span class="text-3xl md:text-4xl font-bold text-white" style="letter-spacing:-0.02em">{card["price"]}</span>
                            <span class="text-gray-400 font-light text-sm mb-1">{card["unit"]}</span>
                        </div>
                        <ul class="space-y-2.5 text-sm flex-grow mb-6">{items}</ul>
                        <a href="index.html#contact" class="mt-auto block text-center bg-fukuya-orange text-white px-6 py-3 font-medium tracking-widest text-sm hover:bg-fukuya-accent transition-all">{card["cta"]}</a>
                    </div>
                </div>
            </div>'''

def pricing(p):
    return f'''
    <!-- 料金 -->
    <section id="pricing" class="bg-fukuya-warm">
        <div class="container mx-auto px-6 max-w-5xl">
            <div class="text-center mb-12">
                <div class="inline-flex items-center gap-3 mb-5"><span class="gold-line"></span><span class="label-tag text-fukuya-mid tracking-[0.2em]">PRICE</span><span class="gold-line"></span></div>
                <h2 class="text-2xl md:text-3xl font-bold text-fukuya-dark mb-3">{p["pricing_title"]}</h2>
                <p class="text-sm text-gray-500 font-light max-w-xl mx-auto leading-relaxed">{p["pricing_lead"]}</p>
            </div>{"".join(p["compares"])}
            <p class="text-center text-[11px] text-gray-400 font-light leading-relaxed max-w-3xl mx-auto">{p.get("pricing_note", "")}{SOURCE_NOTE}</p>
        </div>
    </section>'''

def steps(p):
    items = "".join(f'''
                <div class="bg-white border border-gray-200 p-6">
                    <div class="label-tag mb-3" style="color:#b8985a">STEP {i+1:02d}</div>
                    <h3 class="font-bold text-base text-fukuya-dark mb-2">{t}</h3>
                    <p class="text-xs text-gray-500 font-light leading-relaxed">{d}</p>
                </div>''' for i, (t, d) in enumerate(p["steps"]))
    return f'''
    <!-- 流れ -->
    <section class="bg-white">
        <div class="container mx-auto px-6 max-w-5xl">
            <div class="text-center mb-10">
                <div class="inline-flex items-center gap-3 mb-5"><span class="gold-line"></span><span class="label-tag text-fukuya-mid tracking-[0.2em]">FLOW</span><span class="gold-line"></span></div>
                <h2 class="text-2xl md:text-3xl font-bold text-fukuya-dark">ご依頼の流れ</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4">{items}
            </div>
            <p class="mt-6 text-center text-xs text-gray-400 font-light">ご契約は内容にご納得いただいてから。無理な営業は一切いたしません。</p>
        </div>
    </section>'''

def faq(p):
    items = "".join(f'''
                <details class="group border-b border-gray-200 py-5">
                    <summary class="flex items-center justify-between cursor-pointer font-bold text-sm md:text-base text-fukuya-dark gap-4">
                        <span>{q}</span>
                        <span class="text-fukuya-orange flex-shrink-0 text-xl font-light transition-transform group-open:rotate-45">＋</span>
                    </summary>
                    <p class="mt-3 text-sm text-gray-500 font-light leading-relaxed">{a}</p>
                </details>''' for q, a in p["faq"])
    return f'''
    <!-- FAQ -->
    <section class="bg-fukuya-warm">
        <div class="container mx-auto px-6 max-w-3xl">
            <div class="text-center mb-10">
                <span class="label-tag text-gray-400 block mb-3">FAQ</span>
                <h2 class="text-2xl md:text-3xl font-bold text-fukuya-dark">{p["short"]}のよくある質問</h2>
            </div>
            <div>{items}
            </div>
            <p class="mt-8 text-center text-xs text-gray-400"><a href="index.html#faq" class="underline hover:text-fukuya-dark transition">サービス全体のよくある質問を見る</a></p>
        </div>
    </section>'''

def cta(p):
    return f'''
    <!-- CTA -->
    <section class="bg-fukuya-dark text-white">
        <div class="container mx-auto px-6 max-w-3xl text-center">
            <span class="label-tag block mb-4" style="color:#c8a97e">CONTACT</span>
            <h2 class="text-2xl md:text-3xl font-bold mb-5">{p["cta_title"]}</h2>
            <p class="text-sm text-gray-300 font-light leading-relaxed mb-8 max-w-xl mx-auto">今すぐの契約は必要ありません。「とりあえず話だけ聞きたい」「自分のお店に合うか分からない」——そんな段階でも、ぜひご連絡ください。返信は1営業日以内です。</p>
            <a href="index.html#contact" class="inline-flex items-center justify-center gap-2 bg-fukuya-orange text-white px-10 py-4 font-medium tracking-widest hover:bg-fukuya-accent transition-all text-sm">無料相談・お問い合わせフォームへ →</a>
            <p class="mt-6 text-xs text-gray-500">メールでも：<a href="mailto:info@fukuya-fs.com" class="underline hover:text-white transition">info@fukuya-fs.com</a></p>
        </div>
    </section>'''

def footer():
    links = "".join(f'<a href="{h}" class="text-gray-400 text-xs hover:text-white transition">{t}</a>' for h, t in NAV[1:])
    return f'''
    <footer class="bg-fukuya-dark text-white py-10 border-t border-gray-800">
        <div class="container mx-auto px-4 max-w-6xl">
            <div class="flex flex-col md:flex-row items-center justify-between gap-5">
                <a href="index.html" class="flex items-center gap-x-3 hover:opacity-80 transition">
                    <img src="images/fukuya-logo.png" alt="Fukuya" class="h-10 w-auto object-contain">
                    <span class="flex flex-col leading-tight"><span class="text-sm font-black tracking-tight">Fukuya</span><span class="text-[10px] font-bold text-gray-400 tracking-widest uppercase">Food &amp; SNS Consulting</span></span>
                </a>
                <nav class="flex items-center gap-4 flex-wrap justify-center">{links}<a href="index.html#faq" class="text-gray-400 text-xs hover:text-white transition">よくある質問</a><a href="privacy.html" class="text-gray-400 text-xs hover:text-white transition">プライバシーポリシー</a></nav>
            </div>
            <div class="mt-6 pt-5 border-t border-gray-800 flex flex-col md:flex-row items-center justify-between gap-3">
                <p class="text-gray-600 text-xs">&copy; 2025 Fukuya Food &amp; SNS Consulting. All rights reserved.</p>
                <div class="flex items-center gap-5">
                    <a href="mailto:info@fukuya-fs.com" class="text-gray-400 text-xs hover:text-white transition">info@fukuya-fs.com</a>
                    <a href="https://x.com/terajima_fukuya" target="_blank" rel="noopener" class="text-gray-400 text-xs hover:text-white transition">𝕏 @terajima_fukuya</a>
                    <a href="https://note.com/long_clover8311" target="_blank" rel="noopener" class="text-gray-400 text-xs hover:text-white transition">✎ note</a>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>
'''

def build(p):
    p["faq_ld"] = {"@context": "https://schema.org", "@type": "FAQPage",
                   "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]}
    p["breadcrumb_ld"] = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "トップ", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": p["short"], "item": f"{BASE}/{p['file']}"}]}
    return head(p) + header(p) + hero(p) + pains(p) + features(p) + pricing(p) + steps(p) + faq(p) + cta(p) + footer()

PROVIDER = {"@type": "ProfessionalService", "name": "Fukuya Food & SNS Consulting", "url": BASE + "/", "founder": {"@type": "Person", "name": "寺島 久雄"}}
def service_ld(name, desc, url, offers, area):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc, "url": url, "provider": PROVIDER,
            "areaServed": area, "offers": [{"@type": "Offer", "name": n, "price": pr, "priceCurrency": "JPY"} for n, pr in offers]}

AREA4 = ["東京都", "神奈川県", "埼玉県", "千葉県"]
STEPS_COMMON_1 = ("無料相談・診断", "フォームまたはメールでご連絡ください。無料の「店舗デジタル力診断」で、現状と課題を一緒に整理します。")

# ============================================================ ページデータ
PAGES = []

# ---------- SNS運用代行
PAGES.append({
    "file": "sns.html", "short": "SNS運用代行", "label": "SNS / INSTAGRAM / MEO",
    "title": "飲食店のSNS運用代行・Instagram運用代行【東京・都内近郊】月額4万円〜 | Fukuya Food & SNS Consulting",
    "og_title": "飲食店のSNS運用代行・Instagram運用代行【東京・都内近郊】| Fukuya",
    "description": "飲食店専門のInstagram運用代行・撮影代行・MEOコンサルティング。毎日AIで市場を分析する根拠のある運用を、ライトプラン月額40,000円／スタンダードプラン月額59,800円（税抜）で。撮影込みのスタンダードは東京都内・神奈川・埼玉・千葉、ライトは全国オンライン対応。",
    "h1": "飲食店の<span style=\"color:#9a8060\">SNS運用代行</span><br>Instagram運用・MEO対策を、撮影から分析まで",
    "lead": "飲食業界20年の元・販促責任者が、毎日最新のAIで市場とアルゴリズムを分析。\"なんとなく投稿\"ではなく、データの根拠がある運用でSNSをお店の「資産」に育てます。個別に外注すれば月10万円を超える運用・撮影を、一気通貫だから月額59,800円で。",
    "area_line": "対応エリア：スタンダードプラン（撮影あり）は東京都内・神奈川・埼玉・千葉　／　ライトプランは全国オンライン対応",
    "pain_title": "Instagram・MEOで、こんなお悩みはありませんか？",
    "pains": [("😰", "更新する時間も余裕もない", "営業終わりでクタクタ。何を投稿すればいいか分からないし、写真を撮る余裕もない。"),
              ("🤔", "投稿しても反応がない", "フォロワーは増えず、来店にもつながらない。何が正解なのか、判断の根拠がない。"),
              ("🗣️", "業者は現場を分かってくれない", "キッチンの導線や原価構造を無視した提案ばかり。机上の空論には、もう疲れた。")],
    "pain_close_main": "「毎日AIで分析する、根拠のあるSNS運用」で解決します。",
    "features_title": "2つのプラン、どちらも「根拠のある運用」",
    "features_lead": "コンサルティング特化のライトプランから始めて、撮影・投稿まで丸ごと任せるスタンダードプランへステップアップできます。",
    "features": [("ライトプラン（コンサルティング特化）", ["Instagram & MEO 毎月の分析・改善レポート", "プロフィール案の提案", "投稿台本の提案（週1本）", "月1回のオンラインミーティング", "質問対応（週1回まで）", "全国対応・オンライン完結"]),
                 ("スタンダードプラン（撮影から運用まで）", ["店舗での写真・動画撮影（月1〜2回）", "Instagram投稿・リールの運用代行（週2〜3回）", "月1回のオンラインミーティング", "ライトプランの全内容を包含", "対応エリア：" + AREA])],
    "features_extra": '''
            <div class="mt-8 bg-fukuya-dark text-white p-6 md:p-7 flex items-start gap-4">
                <div class="text-2xl flex-shrink-0">📊</div>
                <div>
                    <p class="font-bold text-sm md:text-base mb-1.5" style="color:#c8a97e">毎日AIを走らせる「根拠のあるSNS運用」</p>
                    <p class="text-xs md:text-sm text-gray-300 font-light leading-relaxed">最新のAIツールを毎日稼働させ、市場動向・SNSアルゴリズムの変化・競合の動きを継続的に分析しています。「なんとなく良さそう」という感覚ではなく、データの根拠にもとづいた施策だけを実行。分析結果は毎月のレポートで共有します。</p>
                </div>
            </div>''',
    "pricing_title": "料金と、一般的な相場との比較",
    "pricing_lead": "SNS運用と撮影を個別に外注すれば月10万円を超えるのが一般的——一気通貫だから、この価格で提供できます。",
    "compares": [
        compare("ライトプラン", "コンサルティング特化（撮影はお客様）。全国対応・オンライン完結。",
                [("SNSコンサルティング会社", "月5万〜10万円", ""), ("運用代行まで依頼した場合", "月10万〜30万円", "")],
                {"rows_label": "SNSコンサルの一般的な価格帯", "badge": "相場の下限を下回る価格", "price_label": "月額", "price": "¥40,000", "unit": "/ 月（税抜）",
                 "items": ["Instagram &amp; MEO 毎月の分析・改善レポート", "プロフィール案の提案", "投稿台本の提案（週1本）", "月1回のオンラインミーティング", "質問対応（週1回まで）"], "cta": "このプランで相談する"}),
        compare("スタンダードプラン", "撮影から運用まで、まるごとお任せ。対応エリア：東京都内・神奈川・埼玉・千葉。",
                [("SNS運用代行（投稿・リール）", "月10万〜30万円", ""), ("店舗・料理の撮影（単発）", "1回2万〜5万円", ""), ("合計イメージ", "月12万円前後〜", "")],
                {"rows_label": "個別に外注した場合の価格帯", "badge": "個別外注の約半額", "price_label": "月額", "price": "¥59,800", "unit": "/ 月（税抜）",
                 "items": ["店舗での写真・動画撮影（月1〜2回）", "Instagram投稿・リールの運用代行（週2〜3回）", "月1回のオンラインミーティング", "ライトプランの全内容を包含"], "cta": "このプランで相談する"}, "RECOMMENDED"),
    ],
    "pricing_note": "※ ご契約期間は原則６か月以上となります。",
    "steps": [STEPS_COMMON_1, ("ヒアリング", "お店の強み・客層・現状のSNSを拝見し、目標を共有します（ライトプランはオンラインで完結）。"),
              ("ご提案・お見積り", "プランと運用方針をご提案。内容にご納得いただいてからご契約です。"),
              ("運用開始", "撮影・投稿・分析をスタート。毎月のレポートとミーティングで数字を見ながら改善を続けます。")],
    "faq": [("SNSの知識が全くなくても大丈夫ですか？", "はい、問題ありません。スタンダードプランでは撮影から投稿・分析までFukuyaがすべて代行しますので、オーナー様はお店の運営に集中していただけます。また、ノウハウ共有やスタッフ研修を通じて、お店に知識と仕組みを残すことも大切にしています。"),
            ("ライトプランとスタンダードプランの違いは何ですか？", "ライトプランは分析レポート・投稿台本のご提案などコンサルティングに特化したプランで、撮影と投稿はお客様ご自身で行っていただきます。スタンダードプランは月1〜2回の店舗撮影から週2〜3回のInstagram投稿・リール運用までをFukuyaが代行します。"),
            ("撮影はどのように行われますか？", "スタンダードプランでは月1〜2回、プロがお店に伺って料理や店内の写真・動画を撮影します。オーナー様側での準備や手間は最小限で構いません。撮影の対応エリアは東京都内・神奈川・埼玉・千葉です（一部地域は要相談）。"),
            ("契約期間に縛りはありますか？", "月額プランのご契約期間は原則6か月以上とさせていただいています。SNSやMEOの成果は積み上げ型のため、短期間では効果測定が難しいことが理由です。ご不安な点は無料相談の際に遠慮なくお尋ねください。"),
            ("解約したら、それまでの投稿やノウハウはどうなりますか？", "アカウントも投稿もすべてお店の資産としてそのまま残ります。Fukuyaは契約中からノウハウ共有・スタッフ研修を行い、お店が自走できる仕組みづくりを重視していますので、解約後もご自身で運用を続けていただけます。")],
    "cta_title": "まずは、お店のSNSの現状をお聞かせください。",
    "service_ld": service_ld("飲食店向けSNS運用代行・Instagram運用代行・MEOコンサルティング",
                             "飲食店専門のInstagram運用代行・店舗撮影・MEOコンサルティング。毎日AIで市場を分析する根拠のある運用。",
                             BASE + "/sns.html", [("ライトプラン（SNS・MEOコンサルティング特化、月額）", "40000"), ("スタンダードプラン（店舗撮影・Instagram投稿・リール運用代行、月額）", "59800")], AREA4 + ["日本"]),
})

# ---------- LP制作
PAGES.append({
    "file": "lp.html", "short": "LP制作", "label": "LANDING PAGE / AIO",
    "title": "飲食店のホームページ・LP制作【AI検索（AIO）対応】初回¥69,800＋月額¥9,800 | Fukuya Food & SNS Consulting",
    "og_title": "飲食店のホームページ・LP制作【AI検索（AIO）対応】| Fukuya",
    "description": "飲食店専門のホームページ（LP）制作。企画・原稿作成からデザイン・スマホ対応、AI検索（AIO）・SEO・MEO対策一式、公開設定まで初回69,800円（税抜）。月額9,800円で維持管理とメニュー・写真の月次更新込み。制作会社相場の約1/6。",
    "h1": "飲食店の<span style=\"color:#9a8060\">ホームページ（LP）制作</span><br>AI検索（AIO）対応を標準搭載",
    "lead": "格安AI制作に近い価格で、制作会社の内容を。ChatGPTやGoogleのAI検索など「AIに聞いてお店を選ぶ」時代に先回りするLPを、初回69,800円＋月額9,800円（税抜）で制作・運用します。原稿づくりから公開設定、毎月の更新まで、丸ごとお任せください。",
    "area_line": "全国からご依頼可能（オンライン対応）　／　対面でのお打ち合わせ・撮影をご希望の場合は " + AREA,
    "pain_title": "お店のホームページで、こんなお悩みはありませんか？",
    "pains": [("💸", "グルメサイト頼みで、毎月の掲載料が重い", "自前のホームページがなく、検索されても情報はグルメサイト任せ。掛け捨ての費用が続いている。"),
              ("🏢", "制作会社は高すぎる", "見積もりは30万〜60万円。小さなお店には現実的でない金額を提示される。"),
              ("🤖", "格安AI制作は「原稿・SEO対策は範囲外」", "安く作れても、文章づくりや検索対策、写真調整は別料金。結局「見つからない」ページになってしまう。")],
    "pain_close_main": "「AI検索対応 × 制作会社の内容 × 格安AI制作に近い価格」で解決します。",
    "features_title": "初回制作に含まれるもの・月額に含まれるもの",
    "features_lead": "「作って終わり」ではなく、公開後の維持・更新まで含めた設計です。",
    "features": [("初回制作費 ¥69,800（税抜）に含まれるもの", ["AI検索（AIO）・SEO・MEO対策一式（標準搭載）", "企画・原稿作成", "デザイン・スマホ対応", "公開設定"]),
                 ("月額 ¥9,800（税抜）に含まれるもの", ["サイトの維持・管理", "メニュー・写真の月次更新"])],
    "features_extra": '''
            <div class="mt-8 bg-fukuya-dark text-white p-6 md:p-7 flex items-start gap-4">
                <div class="text-2xl flex-shrink-0">🤖</div>
                <div>
                    <p class="font-bold text-sm md:text-base mb-1.5" style="color:#c8a97e">AI検索（AIO）対策を標準搭載</p>
                    <p class="text-xs md:text-sm text-gray-300 font-light leading-relaxed">ChatGPTやGoogleのAI検索など、「AIに聞いてお店を選ぶ」利用者が急増しています。FukuyaのLPは、AIがお店の情報を正しく理解・引用できる構造化データとコンテンツ設計まで含めて制作。従来のSEO・MEOに加えて、これからの検索に対応します。この公式サイト自体も同じ設計で作られています。</p>
                </div>
            </div>''',
    "pricing_title": "料金と、世の中の価格帯との比較",
    "pricing_lead": "制作費は3階層の相場を正直に。月額は「更新込み」かどうかで大きく違います。",
    "compares": [
        compare("制作費", "格安AI制作に近い価格で、制作会社の内容を。",
                [("制作会社", "30万〜60万円", "LP平均55.4万円・中央値40万円"), ("フリーランス", "8万〜15万円", ""), ("AI・テンプレート格安制作", "1万〜5万円", "※原稿作成・AI検索対策・写真調整は範囲外が通例")],
                {"rows_label": "制作費の一般的な価格帯", "badge": "制作会社相場の約1/6", "price_label": "LP制作費（初回のみ）", "price": "¥69,800", "unit": "（税抜）",
                 "items": ["<strong class=\"text-white font-medium\">AI検索（AIO）・SEO・MEO対策一式</strong>（標準搭載）", "企画・原稿作成", "デザイン・スマホ対応", "公開設定"], "cta": "LP制作を相談する"}),
        compare("月額費用", "毎月の更新込みでこの価格。",
                [("更新作業込みの運用", "月2万〜3万円", ""), ("保守のみ（更新なし）", "月5千〜2万円", "管理費は平均4.1万円・中央値1.1万円")],
                {"rows_label": "月額費用の一般的な価格帯", "badge": "毎月の更新込みでこの価格", "price_label": "月額", "price": "¥9,800", "unit": "/ 月（税抜）",
                 "items": ["サイトの維持・管理", "メニュー・写真の月次更新"], "cta": "LP制作を相談する"}),
    ],
    "steps": [STEPS_COMMON_1, ("ヒアリング・企画", "お店の強み・客層・掲載したいメニューを伺い、ページの構成と原稿の方向性を決めます。"),
              ("制作・確認", "デザインと原稿を制作し、ご確認いただきながら仕上げます。AI検索・SEO・MEO対策も組み込みます。"),
              ("公開・月次更新", "公開設定まで対応。以降は月額で維持管理と、メニュー・写真の月次更新を行います。")],
    "faq": [("AI検索（AIO）対策とは何ですか？", "ChatGPTやGoogleのAI検索といった「AIに質問して答えを得る」検索で、お店の情報が正しく理解・引用されるための対策です。具体的には、AIが読み取りやすい構造化データの設置と、事実ベースのコンテンツ設計を行います。FukuyaのLP制作では標準搭載しています。"),
            ("料金はいくらですか？", "初回制作費69,800円（税抜）に、企画・原稿作成、デザイン・スマホ対応、AI検索（AIO）・SEO・MEO対策一式、公開設定が含まれます。公開後は月額9,800円（税抜）で、サイトの維持・管理とメニュー・写真の月次更新を行います。"),
            ("写真や原稿は自分で用意する必要がありますか？", "原稿作成は初回制作費に含まれていますので、お店の情報を伺って当方で作成します。写真はお手持ちのものをご提供いただくほか、対面でのお打ち合わせ・撮影をご希望の場合は東京都内・神奈川・埼玉・千葉（一部地域は要相談）で対応します。"),
            ("公開後の更新は自分でやるのですか？", "月額9,800円（税抜）にメニュー・写真の月次更新が含まれていますので、変更内容をお知らせいただくだけで当方が更新します。"),
            ("遠方でも依頼できますか？", "はい。LP制作はオンラインでのやり取りで完結できますので、全国からご依頼いただけます。")],
    "cta_title": "「AIに聞いても見つかるお店」を、一緒につくりましょう。",
    "service_ld": service_ld("飲食店向けホームページ（LP）制作・AI検索（AIO）対応",
                             "飲食店専門のLP制作。企画・原稿作成、デザイン・スマホ対応、AI検索（AIO）・SEO・MEO対策一式、公開設定を含む。月額で維持管理と月次更新。",
                             BASE + "/lp.html", [("LP制作（初回制作費）", "69800"), ("LPの維持・管理、メニュー・写真の月次更新（月額）", "9800")], ["日本"]),
})

# ---------- アプリ開発
APP_CARDS = [{'n': 'スマ仕入', 'img': 'app-sumaden.webp', 'h': 1229, 'alt': 'スマ仕入のホーム画面（納品書を撮る・今月の集計・業者管理・品目マスタ・レシピ管理）', 'p1': '納品書をスマホで撮るだけ、AIが自動で読み取り・記録する飲食店向け業務アプリ。レシピを登録しておけば（手書きレシピの撮影でもOK）、納品書を撮るたびに仕入れ値の変動を反映した<strong class="text-white font-medium">レシピごとの最新原価率をリアルタイムに算出</strong>。原価超過のメニューは<strong class="text-white font-medium">アラートでお知らせ</strong>します。', 'p2': '業者ごとの発注額や、品目ごとの仕入単価の変動も一覧で確認でき、「どの業者から何がいくらで入ったか」が迷わず分かります。', 'p3': '"仕入れ値の上昇に気づかず、利益が消えていた"を防ぐ——飲食の現場出身だから作れたツールです。', 'bg': '#101427'}, {'n': 'スマ売上', 'img': 'app-sumauriage.webp', 'h': 1218, 'alt': 'スマ売上のホーム画面（伝票を撮る・今日の売上・週間・月間・ABC分析・メニュー管理）', 'p1': 'レジのない小さなお店のための売上管理アプリ。手書きの売上伝票を営業終わりにスマホで撮るだけ——AIが自動で読み取り、日次・週次・月次の集計から<strong class="text-white font-medium">売れ筋ランキング、ABC分析まで自動化</strong>します。', 'p2': 'ダッシュボードでは前週比・前月比や客単価、パレート図によるABC分析まで確認でき、データはスプレッドシートにも自動連携。"感覚"の店舗経営が"数字"に変わります。', 'p3': '営業終わりの"ノートと電卓"での集計作業をゼロに。どのメニューが売上をつくっているかが見えるから、メニュー改定や仕込み量の判断が変わります。', 'bg': '#101427'}, {'n': 'スマ棚', 'img': 'app-sumadana.webp', 'h': 1199, 'alt': 'スマ棚の棚卸画面（声で数える・業者ごとの在庫一覧）', 'p1': '"ハンズフリー"の音声棚卸アプリ。スタッフがマイクに向かって品名と数量を話すだけで、<strong class="text-white font-medium">AIが在庫マスタと照合し、棚卸表に自動で記録</strong>。在庫を数えながら両手がふさがる、現場のリアルから生まれた設計です。', 'p2': '聞き取った品名はAIが在庫マスタの正式名称に自動で照合するので、言い方が多少ブレても大丈夫。記録と同時にスプレッドシートへ反映され、転記ミスも起きません。', 'p3': '書いて、数えて、また書いて——月末の棚卸が「話すだけ」に変わります。あとからの集計作業もゼロ。', 'bg': '#0a0c10'}]
ST_LINE = "現在はクライアント店舗向けにモニター提供中。一般提供は準備中です。"
def _phone(a, ind):
    return (f'{ind}<div class="mx-auto mb-6 w-full max-w-[250px]">\n'
            f'{ind}    <div class="rounded-[2rem] bg-[#161616] p-2 shadow-2xl ring-1 ring-white/15">\n'
            f'{ind}        <div class="rounded-[1.6rem] overflow-hidden" style="background:{a["bg"]}">\n'
            f'{ind}            <div class="h-7 relative"><div class="absolute top-1.5 left-1/2 -translate-x-1/2 w-16 h-4 bg-black rounded-full"></div></div>\n'
            f'{ind}            <div class="aspect-[1/2] overflow-hidden"><img src="images/{a["img"]}" alt="{a["alt"]}" class="w-full h-full object-cover object-top" loading="lazy" width="600" height="{a["h"]}"></div>\n'
            f'{ind}        </div>\n{ind}    </div>\n{ind}</div>\n')
def _app_card(a):
    i = "                "
    return (f'\n{i}<div class="bg-fukuya-dark text-white p-7 flex flex-col relative">\n'
            f'{i}    <div class="absolute top-6 right-6"><span class="label-tag text-fukuya-orange tracking-[0.15em]">モニター提供中</span></div>\n'
            f'{i}    <div class="label-tag tracking-[0.15em] mb-2" style="color:#c8a97e">ORIGINAL APP</div>\n'
            f'{i}    <h3 class="text-lg font-bold mb-5">自社アプリ「{a["n"]}」</h3>\n'
            + _phone(a, i + "    ") +
            f'{i}    <p class="text-sm text-gray-300 font-light leading-relaxed mb-4">{a["p1"]}</p>\n'
            f'{i}    <p class="text-xs text-gray-400 font-light leading-relaxed mb-4">{a["p2"]}</p>\n'
            f'{i}    <p class="text-xs text-gray-400 font-light leading-relaxed mb-4">{a["p3"]}</p>\n'
            f'{i}    <p class="mt-auto text-[11px] text-gray-500">{ST_LINE}</p>\n'
            f'{i}</div>')
app_cards_html = "".join(_app_card(a) for a in APP_CARDS)

PAGES.append({
    "file": "app.html", "short": "アプリ開発", "label": "APP DEVELOPMENT",
    "title": "飲食店向けアプリ開発（オーダーメイド）初期¥300,000〜｜自社アプリ3本の開発実績 | Fukuya Food & SNS Consulting",
    "og_title": "飲食店向けアプリ開発（オーダーメイド）初期¥300,000〜 | Fukuya",
    "description": "飲食店の現場を20年知る開発者による、予約管理・在庫管理・顧客台帳などのオーダーメイドアプリ開発。初期300,000円〜（税抜・個別見積）＋月額運用・保守15,000円〜。自社アプリ「スマ仕入」「スマ売上」「スマ棚」を実店舗で運用中。全国オンライン対応。",
    "h1": "飲食店向けの<span style=\"color:#9a8060\">オーダーメイドアプリ開発</span><br>現場を知る開発者が、お店に本当に合うアプリを",
    "lead": "予約管理・在庫管理・顧客台帳・シフト管理など、お店の「困りごと」に合わせて一から設計。最新AIを駆使した開発体制により、一般的な受託開発（小規模でも50万円〜が相場）より大幅に低コストです。自社アプリ3本を実際の店舗で運用しながら磨いている、現場出身の開発です。",
    "area_line": "全国からご依頼可能（オンライン対応）",
    "pain_title": "お店の業務で、こんなお悩みはありませんか？",
    "pains": [("📝", "紙とExcelの手作業が終わらない", "納品書の転記、棚卸のメモ、売上の集計。営業が終わってからの事務作業に毎日追われている。"),
              ("🧩", "既製品のアプリが、うちの店に合わない", "機能が多すぎて使いこなせない、逆に肝心な機能がない。現場の流れに合わせて作られていない。"),
              ("💸", "開発会社に頼むと高すぎる", "小さな業務アプリでも見積もりは50万円〜。飲食店の規模感には現実的でない。")],
    "pain_close_main": "「現場を知る開発者 × AI開発体制 × 実店舗での運用実績」で解決します。",
    "features_title": "オーダーメイド開発でできること",
    "features_lead": "「こんなことできる？」の段階からご相談ください。内容・規模により個別にお見積りします。",
    "features": [("開発例", ["予約管理・顧客台帳", "在庫管理・棚卸", "納品書・売上伝票のAI読み取りと集計", "シフト管理", "既存のスプレッドシート運用との連携"]),
                 ("Fukuyaの開発体制", ["飲食店の現場を20年知る開発者が直接担当", "最新AIを駆使した開発で低コスト・短納期", "自社アプリ3本を実店舗で運用しながら改善中", "オンライン対応で全国からご依頼可能", "月額での運用・保守にも対応"])],
    "features_extra": f'''
            <div class="mt-12">
                <div class="text-center mb-8">
                    <h3 class="text-xl md:text-2xl font-bold text-fukuya-dark mb-2">開発実績：自社アプリ3本</h3>
                    <p class="text-sm text-gray-500 font-light max-w-xl mx-auto">すべてこの体制で開発し、実際の店舗で毎日使われながら磨かれています。「作って終わり」の受託開発とは違う、現場出身の開発です。</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-5">{app_cards_html}
                </div>
                <div class="mt-10 max-w-2xl mx-auto">
                    <p class="text-sm text-gray-600 font-light leading-relaxed text-center mb-5">このアプリ3本を、プログラミング未経験の状態からClaude Codeで開発した42日間の記録を、noteで連載しています。うまくいった話ではなく、止まった記録です。</p>
                    <a href="https://note.com/long_clover8311/n/n98779ff97912" target="_blank" rel="noopener" class="block bg-fukuya-warm border border-gray-200 p-5 hover:shadow-md hover:-translate-y-0.5 transition-all group">
                        <div class="flex items-center gap-4">
                            <div class="flex-shrink-0 w-10 h-10 bg-fukuya-dark flex items-center justify-center"><svg class="w-4 h-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 013 3L7 19l-4 1 1-4L16.5 3.5z"/></svg></div>
                            <div class="flex-grow min-w-0"><p class="label-tag text-fukuya-mid tracking-[0.15em] mb-1">NOTE 連載 — 第0話</p><p class="text-sm font-bold text-fukuya-dark leading-snug">「それ、うちはいらないです」——非エンジニアの私が、自作アプリを3本持って店に行った日</p></div>
                            <div class="flex-shrink-0 text-gray-300 group-hover:text-fukuya-orange transition"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg></div>
                        </div>
                    </a>
                </div>
            </div>''',
    "pricing_title": "料金と、一般的な受託開発相場との比較",
    "pricing_lead": "内容・規模により個別にお見積りします。まずは「やりたいこと」をお聞かせください。",
    "compares": [
        compare("オーダーメイド開発", "小規模な業務アプリでも、一般的な受託開発では50万円〜が相場です。",
                [("受託開発会社（小規模アプリ）", "50万〜300万円", ""), ("月額の運用・保守", "開発費の10〜20%／年が目安", "")],
                {"rows_label": "受託開発の一般的な価格帯", "badge": "小規模受託の相場（50万円〜）を下回る価格", "price_label": "初期開発費", "price": "¥300,000〜", "unit": "（税抜・個別見積）",
                 "items": ["月額運用・保守 ¥15,000〜（税抜）", "現場を知る開発者が直接担当", "最新AI活用で低コスト・短納期", "全国オンライン対応"], "cta": "相談・お見積り"}),
    ],
    "steps": [("無料相談", "「こんなことできる？」の段階からどうぞ。フォームまたはメールで、困っている業務を教えてください。"),
              ("要件の整理", "現場の流れを伺い、本当に必要な機能だけに絞ります。現場出身だからこそ、机上の空論にはなりません。"),
              ("お見積り・開発", "内容と規模に応じてお見積り。ご納得いただいてから開発を開始し、実際の業務で試しながら仕上げます。"),
              ("運用・保守", "公開後は月額での運用・保守に対応。使いながら出てくる改善要望にも継続的にお応えします。")],
    "faq": [("アプリ開発もお願いできますか？", "はい。予約管理・在庫管理・顧客台帳など、お店の業務に合わせたオーダーメイドのアプリ開発を承っています。初期開発費300,000円〜（税抜・内容により個別見積）、月額運用・保守15,000円〜（税抜）です。オンライン対応のため全国からご依頼いただけます。"),
            ("自社アプリ（スマ仕入・スマ売上・スマ棚）は使えますか？", "現在はSNSコンサルティングのクライアント店舗向けにモニター提供中で、一般提供は準備中です。「使ってみたい」というご相談は歓迎しますので、お問い合わせフォームからご連絡ください。"),
            ("まだ何を作りたいか固まっていなくても相談できますか？", "もちろんです。「毎日の事務作業が大変」「この帳票をなんとかしたい」といった困りごとの段階からご相談ください。現場の流れを伺いながら、必要な機能を一緒に整理します。"),
            ("遠方でも依頼できますか？", "はい。アプリ開発はオンラインでのやり取りで完結できますので、全国からご依頼いただけます。")],
    "cta_title": "「うちの店に合うアプリ」を、一緒につくりましょう。",
    "service_ld": service_ld("飲食店向けオーダーメイドアプリ開発",
                             "飲食店の現場を知る開発者による、予約管理・在庫管理・顧客台帳などのオーダーメイドアプリ開発。自社アプリ「スマ仕入」「スマ売上」「スマ棚」を実店舗で運用中。",
                             BASE + "/app.html", [("オーダーメイドアプリ開発（初期開発費、個別見積）", "300000"), ("月額運用・保守", "15000")], ["日本"]),
})

# ---------- メニュー作成
PAGES.append({
    "file": "menu.html", "short": "メニュー作成", "label": "MENU DESIGN",
    "title": "飲食店のメニュー表作成・デザイン（撮影込み）¥35,000【東京・都内近郊】| Fukuya Food & SNS Consulting",
    "og_title": "飲食店のメニュー表作成・デザイン（撮影込み）¥35,000 | Fukuya",
    "description": "飲食店のメニュー表を、料理の撮影込みで35,000円（税抜）。飲食の現場とデザインの現場、両方を知る元・デザイナーが直接制作する、集客に直結するメニュー表。撮影込みで相場の約半額。対応エリアは東京都内・神奈川・埼玉・千葉。",
    "h1": "飲食店の<span style=\"color:#9a8060\">メニュー作成</span>（撮影込み）<br>元・デザイナーが直接手掛ける、集客に直結するメニュー表",
    "lead": "料理の撮影からデザイン制作まで、まとめて35,000円（税抜）。飲食の現場とデザインの現場、両方を知っているからこそ、「見た目が良い」だけでなく「注文につながる」メニュー表をつくります。デザイン＋撮影を別々に外注した場合の相場（7万円前後〜）の約半額です。",
    "area_line": "対応エリア：" + AREA + "（撮影を伴うため）",
    "pain_title": "お店のメニュー表で、こんなお悩みはありませんか？",
    "pains": [("📷", "写真が美味しそうに撮れない", "スマホで撮った写真では、看板メニューの魅力が伝わらない。プロに頼むと撮影だけで数万円。"),
              ("📄", "自作のメニューで、価格の説得力が出ない", "Wordや無料ツールで作ったメニュー表では、こだわりや価格の価値が伝わらず、安い方が選ばれてしまう。"),
              ("💸", "デザイン外注は「撮影別料金」で高くつく", "デザイン会社に頼むと5万〜15万円、しかも撮影は別。結局あきらめて、そのまま使い続けている。")],
    "pain_close_main": "「撮影込み × 元・デザイナーが直接制作 × 相場の約半額」で解決します。",
    "features_title": "メニュー作成に含まれるもの",
    "features_lead": "撮影とデザインをひとりで完結できるから、追加料金なしでこの価格に。",
    "features": [("¥35,000（税抜）に含まれるもの", ["店舗での料理・商品撮影", "メニューのデザイン制作", "元・デザイナーが直接担当", "飲食の現場目線での構成・見せ方のご提案"])],
    "pricing_title": "料金と、一般的な相場との比較",
    "pricing_lead": "「撮影は別料金」が通例の相場に対し、撮影込みでこの価格です。",
    "compares": [
        compare("メニュー作成（撮影込み）", "元・デザイナーが直接手掛ける、集客に直結するメニュー表。",
                [("制作会社に依頼", "5万〜15万円", ""), ("フリーランス・クラウドソーシング", "3万〜7.7万円", "※撮影は別料金が通例")],
                {"rows_label": "メニュー制作の一般的な価格帯", "badge": "撮影込みで相場の約半額", "price_label": "制作費", "price": "¥35,000", "unit": "（税抜）",
                 "items": ["店舗での料理・商品撮影", "メニューのデザイン制作", "元・デザイナーが直接担当"], "cta": "相談・お見積り"}),
    ],
    "steps": [STEPS_COMMON_1, ("ヒアリング", "看板メニュー・客単価・お店の雰囲気を伺い、メニュー表の構成と撮影する料理を決めます。"),
              ("撮影", "お店に伺って料理・商品を撮影します。営業の合間など、ご都合に合わせて日程を調整します。"),
              ("デザイン・納品", "撮影した写真でデザインを制作し、ご確認いただきながら仕上げます。")],
    "faq": [("メニュー作成の料金はいくらですか？", "撮影込みで35,000円（税抜）です。店舗での料理・商品撮影とメニューのデザイン制作が含まれ、元・デザイナーが直接担当します。"),
            ("対応エリアを教えてください。", "撮影を伴うため、対応エリアは東京都内・神奈川・埼玉・千葉です（一部地域は要相談）。"),
            ("印刷もお願いできますか？", "まずはご相談ください。印刷方法や部数によって最適な方法が異なりますので、お見積りの際に合わせてご案内します。"),
            ("SNS運用と一緒に頼むこともできますか？", "はい。撮影した料理写真はInstagramの投稿素材としても活用できますので、SNS運用プランとあわせてのご依頼も歓迎です。")],
    "cta_title": "「注文につながるメニュー表」を、一緒につくりましょう。",
    "service_ld": service_ld("飲食店向けメニュー表作成・デザイン（撮影込み）",
                             "飲食店のメニュー表を料理の撮影込みで制作。元・デザイナーが直接担当。",
                             BASE + "/menu.html", [("メニュー作成（撮影込み）", "35000")], AREA4),
})

for p in PAGES:
    out = build(p)
    with open(f"{OUT}\\{p['file']}", "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    print(p["file"], len(out), "bytes")

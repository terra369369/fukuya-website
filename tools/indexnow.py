# -*- coding: utf-8 -*-
"""IndexNow で Bing 等に更新を即時通知する。
使い方: python tools/indexnow.py            (sitemap.xml の全URLを送信)
        python tools/indexnow.py URL [URL...] (指定URLのみ)
キーは公開前提の値(リポジトリ直下の 4fe751fce0de587b18eda21afcf6b62d.txt で所有確認される)。
本番に反映された後に実行すること。"""
import json, re, sys, urllib.request, pathlib

HOST = "fukuya-fs.com"
KEY = "4fe751fce0de587b18eda21afcf6b62d"
ROOT = pathlib.Path(__file__).resolve().parent.parent

def main():
    urls = sys.argv[1:] or re.findall(r"<loc>([^<]+)</loc>", (ROOT / "sitemap.xml").read_text(encoding="utf-8"))
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls}).encode("utf-8")
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        print(r.status, len(urls), "urls submitted")

if __name__ == "__main__":
    main()

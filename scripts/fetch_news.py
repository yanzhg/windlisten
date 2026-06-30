import feedparser
import datetime
import os

# 新闻源
RSS_SOURCES = [
    ("36氪", "https://36kr.com/feed"),
    ("InfoQ", "https://www.infoq.cn/feed"),
    ("新浪科技", "https://tech.sina.com.cn/rss.xml"),
    ("钛媒体", "https://www.tmtpost.com/feed"),
]

# 输出目录
OUT_DIR = "docs/posts"
os.makedirs(OUT_DIR, exist_ok=True)

# 只抓 24 小时内新闻
now = datetime.datetime.now(datetime.timezone.utc)
cutoff = now - datetime.timedelta(hours=24)

news_list = []

for name, url in RSS_SOURCES:
    try:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            try:
                published = datetime.datetime(*entry.published_parsed[:6], tzinfo=datetime.timezone.utc)
                if published < cutoff:
                    continue
                news_list.append({
                    "title": entry.title,
                    "link": entry.link,
                    "summary": entry.get("summary", "暂无简介"),
                    "source": name,
                    "time": published.strftime("%Y-%m-%d %H:%M")
                })
            except Exception:
                continue
    except Exception:
        continue

# 生成今日新闻
if news_list:
    date_str = now.strftime("%Y-%m-%d")
    filename = f"{date_str}_tech_news.md"
    filepath = os.path.join(OUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"""---
title: {date_str} 科技新闻汇总
date: {date_str}
---

""")
        f.write(f"# {date_str} 科技新闻汇总\n\n")
        f.write(f"📅 自动采集于：{now.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        for news in news_list:
            f.write(f"## {news['title']}\n")
            f.write(f"- 来源：{news['source']}\n")
            f.write(f"- 时间：{news['time']}\n")
            f.write(f"- 链接：[{news['link']}]({news['link']})\n\n")
            f.write(f"{news['summary']}\n\n")
            f.write("---\n\n")
    print(f"✅ 生成新闻：{filepath}")
else:
    print("ℹ️ 今日无新新闻")
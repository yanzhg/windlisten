import feedparser
import datetime
import os

# 新闻源列表
RSS_SOURCES = [
    ("36氪", "https://36kr.com/feed"),
    ("InfoQ", "https://www.infoq.cn/feed"),
    ("新浪科技", "https://tech.sina.com.cn/rss.xml"),
    ("钛媒体", "https://www.tmtpost.com/feed"),
]

# 输出文件夹
OUT_DIR = "docs/posts"
os.makedirs(OUT_DIR, exist_ok=True)

# 24小时时间过滤
now = datetime.datetime.now(datetime.timezone.utc)
cutoff = now - datetime.timedelta(hours=24)

news_list = []

# 遍历所有RSS抓取新闻
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

# 判断是否有新闻，统一缩进层级
if news_list:
    date_str = now.strftime("%Y-%m-%d")
    filename = f"{date_str}_tech_news.md"
    filepath = os.path.join(OUT_DIR, filename)

    # 全部写入逻辑缩进在if内部
    with open(filepath, "w", encoding="utf-8") as f:
        content_head = f"""---
title: {date_str} 科技新闻汇总
date: {date_str}
---

# {date_str} 科技新闻汇总
📅 自动采集于：{now.strftime('%Y-%m-%d %H:%M:%S')}

---
"""
        f.write(content_head)
        for news in news_list:
            block = f"""## {news['title']}
- 来源：{news['source']}
- 时间：{news['time']}
- 链接：[{news['link']}]({news['link']})

{news['summary']}

---
"""
            f.write(block)
    print(f"✅ 生成新闻文件：{filepath}")
else:
    print("ℹ️ 过去24小时无新新闻")
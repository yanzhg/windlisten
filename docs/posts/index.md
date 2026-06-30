# WindListen 科技新闻

# 每日科技新闻汇总
每日自动抓取全网科技资讯，实时更新
由 GitHub Actions + MkDocs + Cloudflare 驱动

📌 新闻源：36氪、InfoQ、新浪科技、钛媒体  
⏰ 更新时间：每天上午 10 点

左侧导航「今日新闻」下拉可直接点击对应日期新闻；也可使用顶部搜索框检索日期。

# 每日科技新闻汇总
由 GitHub Actions + MkDocs + Cloudflare 全自动驱动，每日自动采集科技资讯

📌 新闻源：36氪、InfoQ、新浪科技、钛媒体
⏰ 更新：每日定时自动抓取

## 全部日期新闻（点击直达，最新置顶）
{% set news = [] %}
{% for page in pages %}
{% if page.url.startswith("posts/") and page.url != "posts/" %}
{% set _ = news.append(page) %}
{% endif %}
{% endfor %}
{% set news_sort = news | sort(attribute="title", reverse=True) %}

<ul style="font-size:17px; line-height:2.3;">
{% for item in news_sort %}
<li>📅 <a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>

## 快速检索
顶部搜索框输入日期（2026-06-30）也可快速打开新闻。
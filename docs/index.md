# WindListen 科技新闻

# 每日科技新闻汇总
每日自动抓取全网科技资讯，实时更新
由 GitHub Actions + MkDocs + Cloudflare 驱动

📌 新闻源：36氪、InfoQ、新浪科技、钛媒体  
⏰ 更新时间：每天上午 10 点



下面是所有新闻链接，按日期倒序排列：

{% set all_news = [] %}
{% for file in pages %}
  {% if file.url.startswith("posts/") and file.url != "posts/" %}
    {% set _ = all_news.append(file) %}
  {% endif %}
{% endfor %}

{% set sorted_news = all_news | sort(attribute="title", reverse=true) %}

<ul>
{% for item in sorted_news %}
<li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>
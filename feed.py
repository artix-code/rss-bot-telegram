import feedparser
import config

def get_news(url):
    news_link = []
    feed = feedparser.parse(url)
    entry = feed.entries
    
    for l in entry:
        news_link.append(l.link)

    return news_link
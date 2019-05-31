import feedparser

def parse(url):
    #proxy
    return feedparser.parse(url)

#origin of data, obtains a subset of attributes
def get_source(parsed):
    feed = parsed['feed']
    return{
        'link': feed['link'],
        'title':feed['title'],
        'subtitle': feed['subtitle'],
        'summary': feed['summary'],
    }
#returns a list of articles
def get_articles(parsed):
    articles = []
    entries = parsed['entries']
    for entry in entries:
        articles.append({
            'id': entry['id'],
            'link': entry['link'],
            'title': entry['title'],
            'summary': entry['summary'],
            'published': entry['published_parsed'],

        })
    return articles
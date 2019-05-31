from django.contrib.syndication.views import Feed
from django.urls import reverse
# from policebeat.models import NewsItem

class LatestEntriesFeed(Feed):
    title = "NBA News"
    link = "http://www.nba.com/rss/nba_rss.xml"
    description = "Updates on changes and additions to police beat central."

    # def items(self):
    #     return objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        print( item.title)

    def item_description(self, item):
        return item.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('news-item', args=[item.pk])
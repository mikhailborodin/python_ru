from django import template
from articles.models import Article, News
register = template.Library()


@register.inclusion_tag('blocks/article_main.html')
def articles(count=None):
    return {
        'articles': Article.objects.all()[:count],
        'news': News.objects.all()[:3]
    }




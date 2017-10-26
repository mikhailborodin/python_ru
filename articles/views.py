from django.views.generic import DetailView
from articles.models import Article


class ArticleView(DetailView):
    model = Article
    template = 'article_detail.html'

from django.conf.urls import url
from .models import Article, News
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^articles/$', ListView.as_view(model=Article)),
    url(r'^articles/(?P<pk>\d+)/', DetailView.as_view(model=Article)),
    url(r'^news/(?P<slug>[-\w\d]+)/', DetailView.as_view(model=News)),
    url(r'^news/$', DetailView.as_view(model=News)),
]

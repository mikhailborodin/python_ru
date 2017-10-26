from django.contrib import admin

from articles.models import Article, News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'large')

admin.site.register(Article)
admin.site.register(News, NewsAdmin)

from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from ckeditor.fields import RichTextField
from pytils.translit import slugify


class Article(TimeStampedModel):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True, max_length=255)
    preview = models.CharField(max_length=255)
    text = RichTextField()
    large = models.BooleanField(default=False)
    img = models.ImageField(upload_to='news/')
    url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('-created', '-pk')

    def get_absolute_url(self):
        if self.url:
            return self.url
        else:
            return '/articles/%s/' % self.slug

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()


class News(TimeStampedModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True, max_length=255)
    preview = models.CharField(max_length=255)
    text = RichTextField()
    large = models.BooleanField(default=False)
    img = models.ImageField(upload_to='news/')
    url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ('-created', '-pk')

    def get_absolute_url(self):
        if self.url:
            return self.url
        else:
            return '/news/%s/' % self.slug

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super(News, self).save()

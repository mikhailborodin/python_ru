from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название секции')
    template_name = models.CharField(max_length=50, default='sections/section.html')
    enabled = models.BooleanField(blank=True, verbose_name='Секция активна?')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Секция главной страницы на главной'
        verbose_name_plural = 'Секции главной страницы на главной'
        ordering = ('order',)


class Member(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя участника')
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Place(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название события')
    description = models.TextField()
    date = models.DateTimeField()
    place = models.ForeignKey(Place)
    members = models.ManyToManyField(Member)

    def __str__(self):
        return self.title

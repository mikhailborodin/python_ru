from django.db import models


class MenuItem(models.Model):

    title = models.CharField(max_length=512, blank=False)
    card_category = models.ForeignKey('cards_api.CardCategory',
                                      null=True, blank=True)
    url = models.URLField(null=True, blank=True)

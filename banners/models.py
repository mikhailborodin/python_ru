from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField


class Banner(models.Model):
    BANNER_CHOICES = Choices(
        ('banner_top_desktop', 'banner_top_desktop'),
        ('banner_top_tablet', 'banner_top_tablet'),
        ('banner_top_mobile', 'banner_top_mobile'),
    )

    slug = StatusField(choices_name='BANNER_CHOICES')
    image = models.ImageField(blank=False, upload_to='banner_images')

    def __str__(self):
        return '{}'.format(self.slug)

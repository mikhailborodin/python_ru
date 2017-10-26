from django.forms import ModelForm
from subscribed_people.models import SubscribedPerson


class SubscribeForm(ModelForm):
    class Meta:
        model = SubscribedPerson
        fields = ['email']

from django import template
from main.models import Section, Event
from datetime import datetime
register = template.Library()


@register.inclusion_tag('blocks/section.html')
def sections():
    return {'sections': Section.objects.filter(enabled=True)}


@register.inclusion_tag('blocks/events_main.html')
def events(count):
    return {'events': Event.objects.filter(date__gte=datetime.today())[:count]}


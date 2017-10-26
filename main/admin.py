from django.contrib import admin
from .models import Section, Event, Place


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    date_hierarchy = 'date'

admin.site.register(Section, SectionAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Place)

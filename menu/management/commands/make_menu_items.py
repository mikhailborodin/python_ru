from django.core.management.base import BaseCommand, CommandError
from menu import factories


class Command(BaseCommand):
    help = 'Creates test menu items for development'

    menu_items_count = 5

    def handle(self, *args, **options):
        for _ in range(self.menu_items_count):
            factories.MenuFactory.create()

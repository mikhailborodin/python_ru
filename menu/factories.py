import factory
from factory.fuzzy import FuzzyChoice
from cards_api.models import CardCategory


class MenuFactory(factory.DjangoModelFactory):
    title = factory.Iterator(['Новости', 'События',
                              'Записи', 'Блог', 'Вакансии'])
    card_category = FuzzyChoice(CardCategory.objects.all())
    url = factory.Faker('uri')

    class Meta:
        model = 'menu.MenuItem'

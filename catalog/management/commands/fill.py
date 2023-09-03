from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()

        category_list = [
            {'name': 'Электроника', 'description': 'Технические устройства и электроника'},
            {'name': 'Одежда', 'description': 'Одежда и аксессуары'},
            {'name': 'Спорт', 'description': 'Спортивные товары и снаряжение'},
            {'name': 'Книги', 'description': 'Книги и литература'},
        ]

        for category_item in category_list:
            category = Category(**category_item)
            category.save()

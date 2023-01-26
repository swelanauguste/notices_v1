from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Category

CATEGORY_LIST = ["training and education", "vacancies", "closures", 'public notice']


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in CATEGORY_LIST:
            category = _.lower()
            Category.objects.get_or_create(category=category,)
            self.stdout.write(self.style.SUCCESS(f"{category}"))
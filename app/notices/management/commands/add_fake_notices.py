from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Author, Notice, Category, NoticeStatus


# yr_cls_count = YearClass.objects.count()
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(135):
            status = NoticeStatus.objects.get(pk=randint(1, 2))
            category = Category.objects.get(pk=randint(1, Category.objects.count()))
            title = fake.sentence(nb_words=5)
            content = fake.sentence(nb_words=13)
            author = Author.objects.get(pk=randint(1, Author.objects.count()))
            Notice.objects.get_or_create(
                status=status,
                category=category,
                title=title,
                content=content,
                author=author
            )
            self.stdout.write(self.style.SUCCESS(f"{title}"))

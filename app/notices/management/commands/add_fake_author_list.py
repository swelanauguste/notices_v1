from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Author


# yr_cls_count = YearClass.objects.count()
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(20):
            first_name = fake.first_name()
            last_name = fake.last_name()
            post = fake.profile()["job"]
            department = f"{fake.company()} {fake.company_suffix()}"
            address1 = fake.city()
            tel = fake.phone_number()
            Author.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                post=post,
                department=department,
                address1=address1,
                tel=tel,
            )
            self.stdout.write(self.style.SUCCESS(f"{last_name}, {first_name}"))

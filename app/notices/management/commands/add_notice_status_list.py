from django.core.management.base import BaseCommand
from faker import Faker

from ...models import NoticeStatus

STATUS_LIST = ['drafted', 'published']


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in STATUS_LIST:
            status = _.lower()
            NoticeStatus.objects.get_or_create(status=status,)
            self.stdout.write(self.style.SUCCESS(f"{status}"))
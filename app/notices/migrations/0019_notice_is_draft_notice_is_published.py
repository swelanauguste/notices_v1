# Generated by Django 4.1.5 on 2023-01-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notices", "0018_category_slug_alter_category_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="notice",
            name="is_draft",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="notice",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
    ]
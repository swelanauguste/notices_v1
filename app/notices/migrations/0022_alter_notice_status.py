# Generated by Django 4.1.5 on 2023-01-22 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("notices", "0021_alter_noticestatus_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notice",
            name="status",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="notices.noticestatus",
            ),
        ),
    ]

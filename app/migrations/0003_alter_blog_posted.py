# Generated by Django 4.1.7 on 2023-04-13 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("app", "0002_blog_author_alter_blog_posted")]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="posted",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(
                    2023, 4, 13, 15, 12, 29, 642754, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Опубликована",
            ),
        )
    ]

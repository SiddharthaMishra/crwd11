# Generated by Django 3.0.5 on 2020-04-09 10:12

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='json',
            field=jsonfield.fields.JSONField(default={'reviews': [], 'tags': {}}),
        ),
    ]

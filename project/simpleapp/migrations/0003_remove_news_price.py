# Generated by Django 4.2.2 on 2023-06-29 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0002_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='price',
        ),
    ]

# Generated by Django 2.2 on 2019-05-30 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsapp', '0002_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='name',
            new_name='title',
        ),
    ]

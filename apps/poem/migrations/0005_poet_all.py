# Generated by Django 2.0.4 on 2019-05-24 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0004_auto_20190524_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='poet',
            name='all',
            field=models.IntegerField(default=0, help_text='数量', verbose_name='数量'),
        ),
    ]

# Generated by Django 2.0.4 on 2019-05-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, help_text='添加时间', null=True, verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='poet',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, help_text='添加时间', null=True, verbose_name='添加时间'),
        ),
    ]

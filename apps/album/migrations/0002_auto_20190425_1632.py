# Generated by Django 2.0.4 on 2019-04-25 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumphoto',
            name='album',
            field=models.ForeignKey(help_text='图集', on_delete=django.db.models.deletion.DO_NOTHING, to='album.AlbumInfo', verbose_name='图集'),
        ),
        migrations.AlterField(
            model_name='albumphoto',
            name='picture',
            field=models.ForeignKey(help_text='图片', on_delete=django.db.models.deletion.DO_NOTHING, to='material.MaterialPicture', verbose_name='图片'),
        ),
    ]
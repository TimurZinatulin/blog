# Generated by Django 3.2.5 on 2021-09-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dadova', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_featured',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
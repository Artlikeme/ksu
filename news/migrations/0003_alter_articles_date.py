# Generated by Django 4.0.5 on 2022-06-27 17:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_articles_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
    ]

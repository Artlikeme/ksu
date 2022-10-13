# Generated by Django 4.0.5 on 2022-10-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titlepage', '0002_cat_item_dropbox'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities_dropbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dropbox', models.CharField(choices=[('1', 'Таганрог')], default=1, max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Cat_item_dropbox',
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]

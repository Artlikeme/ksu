# Generated by Django 4.0.5 on 2022-06-26 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='mapcode',
            new_name='item_mapcode',
        ),
    ]

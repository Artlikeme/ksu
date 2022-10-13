# Generated by Django 4.0.5 on 2022-10-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0013_item_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openinghours',
            options={'ordering': ('weekday',)},
        ),
        migrations.AlterUniqueTogether(
            name='openinghours',
            unique_together={('weekday',)},
        ),
        migrations.AddField(
            model_name='openinghours',
            name='hours',
            field=models.CharField(default='00:00/24:59', max_length=12),
        ),
        migrations.RemoveField(
            model_name='openinghours',
            name='from_hour',
        ),
        migrations.RemoveField(
            model_name='openinghours',
            name='to_hour',
        ),
    ]

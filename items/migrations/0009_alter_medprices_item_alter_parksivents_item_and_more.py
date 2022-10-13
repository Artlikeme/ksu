# Generated by Django 4.0.5 on 2022-09-20 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_parksivents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medprices',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item', verbose_name='MedPrices'),
        ),
        migrations.AlterField(
            model_name='parksivents',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item', verbose_name='Parks_Ivents'),
        ),
        migrations.CreateModel(
            name='Kindsgardens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField()),
                ('number_of_seats', models.IntegerField()),
                ('ammounts_group', models.IntegerField()),
                ('ammounts_group_teather', models.IntegerField()),
                ('prices_month', models.IntegerField()),
                ('ammont_holidays', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item', verbose_name='Kinds_gardens')),
            ],
        ),
    ]

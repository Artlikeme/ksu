# Generated by Django 4.0.5 on 2022-09-19 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_specialdays_closed_foodbasket'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedPrices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priem', models.IntegerField()),
                ('covid', models.IntegerField()),
                ('lab_analiz', models.IntegerField()),
                ('days_analiz', models.IntegerField()),
                ('mrt', models.IntegerField()),
                ('days_mrt', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item', verbose_name='food_basked')),
            ],
        ),
    ]

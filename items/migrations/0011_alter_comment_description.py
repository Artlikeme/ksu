# Generated by Django 4.0.5 on 2022-09-20 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_universityrate_schollrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

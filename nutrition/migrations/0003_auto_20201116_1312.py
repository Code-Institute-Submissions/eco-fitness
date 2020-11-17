# Generated by Django 3.1.2 on 2020-11-16 13:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0002_auto_20201113_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrition',
            name='Grams',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
    ]
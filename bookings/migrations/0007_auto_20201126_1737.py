# Generated by Django 3.1.2 on 2020-11-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_auto_20201126_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='length',
            field=models.CharField(max_length=20),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20201113_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='name',
            field=models.CharField(max_length=254, null=True),
        ),
    ]

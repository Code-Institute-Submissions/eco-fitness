# Generated by Django 3.1.2 on 2020-11-13 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='number',
            new_name='amount',
        ),
    ]

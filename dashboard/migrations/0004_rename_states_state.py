# Generated by Django 4.1.2 on 2023-06-07 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_states_city'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='States',
            new_name='State',
        ),
    ]

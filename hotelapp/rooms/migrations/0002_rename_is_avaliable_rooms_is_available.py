# Generated by Django 5.1.6 on 2025-03-17 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rooms',
            old_name='is_avaliable',
            new_name='is_available',
        ),
    ]

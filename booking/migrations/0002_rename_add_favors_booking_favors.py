# Generated by Django 5.0.3 on 2024-03-22 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='add_favors',
            new_name='favors',
        ),
    ]

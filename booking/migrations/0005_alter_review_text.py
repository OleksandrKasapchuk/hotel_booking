# Generated by Django 5.0.3 on 2024-03-19 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_remove_room_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
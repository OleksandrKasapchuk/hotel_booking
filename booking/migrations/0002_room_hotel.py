# Generated by Django 5.0.2 on 2024-03-10 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='booking.hotel'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-30 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0004_auto_20210830_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='text',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

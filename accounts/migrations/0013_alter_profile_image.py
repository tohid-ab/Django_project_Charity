# Generated by Django 3.2.6 on 2021-09-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='image/profile.jpg', upload_to='image/profile/', verbose_name='انتخاب عکس'),
        ),
    ]

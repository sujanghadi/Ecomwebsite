# Generated by Django 3.0.2 on 2020-02-14 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appecom', '0006_auto_20200213_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Dp',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

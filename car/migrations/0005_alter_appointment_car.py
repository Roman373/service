# Generated by Django 3.2.9 on 2021-12-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_auto_20211222_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='car',
            field=models.CharField(max_length=11, verbose_name='Телефон'),
        ),
    ]

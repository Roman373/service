# Generated by Django 3.2.9 on 2021-11-17 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='lastname',
            new_name='name_lastname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AlterField(
            model_name='car',
            name='body_number',
            field=models.CharField(max_length=12, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_color',
            field=models.CharField(max_length=40, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.CharField(max_length=30, verbose_name='Модель автомобиля'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_number',
            field=models.CharField(max_length=14, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(max_length=6, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='car',
            name='register_sign',
            field=models.CharField(max_length=8, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='car',
            name='vin',
            field=models.CharField(max_length=17, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='car',
            name='year_issue',
            field=models.IntegerField(max_length=4, verbose_name=''),
        ),
    ]
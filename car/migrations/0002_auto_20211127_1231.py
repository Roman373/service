# Generated by Django 3.2.9 on 2021-11-27 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spare',
            name='suppliers',
        ),
        migrations.AddField(
            model_name='spare',
            name='supplier',
            field=models.ManyToManyField(to='car.Supplier', verbose_name='Поставщик'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='service',
            field=models.ManyToManyField(to='car.Service', verbose_name='Обращение'),
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='car.position', verbose_name='Должность'),
        ),
    ]
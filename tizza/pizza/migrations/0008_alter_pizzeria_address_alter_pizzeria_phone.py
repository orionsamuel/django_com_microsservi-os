# Generated by Django 4.0.1 on 2022-01-07 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0007_alter_pizza_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzeria',
            name='address',
            field=models.CharField(default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='pizzeria',
            name='phone',
            field=models.CharField(default='', max_length=40),
        ),
    ]

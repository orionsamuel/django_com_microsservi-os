# Generated by Django 4.0.1 on 2022-01-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0008_alter_pizzeria_address_alter_pizzeria_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzeria',
            name='address',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='pizzeria',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
    ]
# Generated by Django 4.0.1 on 2022-01-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0009_alter_pizzeria_address_alter_pizzeria_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='description',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='thumbnail_url',
            field=models.URLField(blank=True, default=''),
        ),
    ]

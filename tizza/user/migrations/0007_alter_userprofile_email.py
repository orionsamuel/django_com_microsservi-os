# Generated by Django 4.0.1 on 2022-01-12 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, unique=True, verbose_name='E-mail'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-10 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0013_rename_ser_dislikes_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dislikes',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='like',
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-13 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twshows',
            old_name='descrptions',
            new_name='descrption',
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-21 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0021_auto_20211021_1702'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
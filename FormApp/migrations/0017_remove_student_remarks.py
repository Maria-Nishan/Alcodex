# Generated by Django 3.2.7 on 2021-10-21 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0016_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='remarks',
        ),
    ]

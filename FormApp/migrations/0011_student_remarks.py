# Generated by Django 3.2.7 on 2021-10-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0010_auto_20211021_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='remarks',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

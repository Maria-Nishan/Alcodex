# Generated by Django 3.2.7 on 2021-10-20 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0005_auto_20211020_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='location_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

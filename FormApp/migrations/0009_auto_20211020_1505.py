# Generated by Django 3.2.7 on 2021-10-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0008_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='location_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='student_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='group_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
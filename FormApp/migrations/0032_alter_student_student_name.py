# Generated by Django 3.2.7 on 2021-10-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0031_auto_20211021_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

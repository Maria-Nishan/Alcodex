# Generated by Django 3.2.7 on 2021-10-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0003_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=30, null=True)),
                ('student_name', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]

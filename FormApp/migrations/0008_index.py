# Generated by Django 3.2.7 on 2021-10-20 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0007_rename_group_name_student_groupname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FormApp.group')),
            ],
        ),
    ]
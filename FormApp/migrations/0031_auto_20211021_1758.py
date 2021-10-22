# Generated by Django 3.2.7 on 2021-10-21 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0030_rename_groupname_student_group_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='group_name',
        ),
        migrations.AddField(
            model_name='group',
            name='group_id',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='location_id',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='groupname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FormApp.group'),
        ),
    ]

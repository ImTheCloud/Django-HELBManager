# Generated by Django 4.1.3 on 2022-12-20 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_rename_subtaskbobn1_post_tasks_subtasks_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-22 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_rename_tasks_subtasks_status_post_tasks_subtasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='contributor',
        ),
        migrations.AddField(
            model_name='post',
            name='contributor',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-22 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_rename_tasks_subtasks_post_tasks_subtasks_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tasks_subtasks_status',
            new_name='tasks_subtasks',
        ),
    ]

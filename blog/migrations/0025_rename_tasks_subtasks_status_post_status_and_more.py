# Generated by Django 4.1.3 on 2022-12-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_alter_post_tasks_subtasks_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tasks_subtasks_status',
            new_name='status',
        ),
        migrations.AddField(
            model_name='post',
            name='tasks_subtasks',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
    ]

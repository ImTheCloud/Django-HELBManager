# Generated by Django 4.1.3 on 2022-12-08 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_taskalice'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtaskBobN2',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='taskBobN2',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-08 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_subtaskbobn2_post_taskbobn2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtaskCesar',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='taskBobN3',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='taskCesarN1',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='taskCesarN2',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='password',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
    ]

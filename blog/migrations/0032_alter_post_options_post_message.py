# Generated by Django 4.1.3 on 2023-01-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['contributor']},
        ),
        migrations.AddField(
            model_name='post',
            name='message',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
    ]

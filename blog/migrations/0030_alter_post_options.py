# Generated by Django 4.1.3 on 2022-12-30 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_alter_post_contributor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['contributor']},
        ),
    ]

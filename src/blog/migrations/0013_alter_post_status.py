# Generated by Django 4.1.3 on 2022-12-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('TODO', 'TODO')], default='TODO', max_length=20, null=True),
        ),
    ]

# Generated by Django 4.0.1 on 2022-04-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SERVER1', '0009_alter_blog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(default='', max_length=200),
        ),
    ]

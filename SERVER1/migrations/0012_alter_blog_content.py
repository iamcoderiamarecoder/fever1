# Generated by Django 4.0.1 on 2022-04-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SERVER1', '0011_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(default=''),
        ),
    ]

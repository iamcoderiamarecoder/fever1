# Generated by Django 4.0.1 on 2022-04-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SERVER1', '0007_alter_blog_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
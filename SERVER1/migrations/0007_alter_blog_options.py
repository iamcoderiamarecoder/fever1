# Generated by Django 4.0.1 on 2022-04-20 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SERVER1', '0006_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-date']},
        ),
    ]

# Generated by Django 4.2 on 2023-06-30 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_likepost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
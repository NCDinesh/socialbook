# Generated by Django 4.2 on 2023-07-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_post_delete_post1'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to='post_images'),
        ),
    ]

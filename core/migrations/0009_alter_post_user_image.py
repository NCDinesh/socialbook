# Generated by Django 4.2 on 2023-06-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_post_post_image_alter_post_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_image',
            field=models.ImageField(default='blank.png', upload_to='newuser_images'),
        ),
    ]

# Generated by Django 4.2 on 2023-07-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_post_delete_mispost'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowerCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]

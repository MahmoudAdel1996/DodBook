# Generated by Django 2.1.1 on 2018-09-10 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todo_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_image'),
        ),
    ]

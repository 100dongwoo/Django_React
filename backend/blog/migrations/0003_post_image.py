# Generated by Django 3.2.12 on 2022-02-13 08:46

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default.jpg', upload_to=blog.models.upload_to, verbose_name='Image'),
        ),
    ]
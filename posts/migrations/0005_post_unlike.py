# Generated by Django 2.0.6 on 2018-06-25 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='unlike',
            field=models.IntegerField(default=0, verbose_name='Unlike'),
        ),
    ]
# Generated by Django 2.0.6 on 2018-07-01 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20180629_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Rating'),
        ),
    ]

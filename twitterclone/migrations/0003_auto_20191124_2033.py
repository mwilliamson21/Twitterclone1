# Generated by Django 2.2.7 on 2019-11-24 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0002_auto_20191124_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitteruser',
            name='followed_by',
        ),
        migrations.RemoveField(
            model_name='twitteruser',
            name='following',
        ),
    ]

# Generated by Django 3.1.5 on 2021-05-10 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizmodel',
            name='secs',
        ),
    ]

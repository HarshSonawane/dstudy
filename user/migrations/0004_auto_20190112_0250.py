# Generated by Django 2.1.5 on 2019-01-11 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_currentcourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentcourse',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='fullname',
        ),
        migrations.DeleteModel(
            name='CurrentCourse',
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-21 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0003_auto_20190121_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='college',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='name',
            new_name='title',
        ),
    ]

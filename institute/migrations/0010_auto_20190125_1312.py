# Generated by Django 2.1.5 on 2019-01-25 07:42

from django.db import migrations, models
import institute.models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0009_auto_20190125_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='logo',
            field=models.ImageField(blank=True, default='logo.png', null=True, upload_to=institute.models.upload_logo_path),
        ),
    ]

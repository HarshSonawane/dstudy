# Generated by Django 2.1.5 on 2019-01-23 19:43

from django.db import migrations, models
import educourse.models
import educourse.validators


class Migration(migrations.Migration):

    dependencies = [
        ('educourse', '0012_auto_20190124_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculam',
            name='file',
            field=models.FileField(upload_to=educourse.models.upload_file_path, validators=[educourse.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='modelanswerpaper',
            name='file',
            field=models.FileField(blank=True, upload_to=educourse.models.upload_file_path, validators=[educourse.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='quetionpaper',
            name='file',
            field=models.FileField(blank=True, upload_to=educourse.models.upload_file_path, validators=[educourse.validators.validate_file_extension]),
        ),
    ]
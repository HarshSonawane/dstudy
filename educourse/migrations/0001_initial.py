# Generated by Django 2.1.5 on 2019-01-21 11:54

from django.db import migrations, models
import educourse.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EduCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('course', models.CharField(max_length=5)),
                ('level', models.CharField(blank=True, choices=[('Under Graduate', 'Under Graduate'), ('Diploma ', 'Diploma')], default='Not Selected', max_length=255)),
                ('duration', models.CharField(blank=True, choices=[('2  Year', '2  Year'), ('3  Year ', '3  Year')], default='Not Selected', max_length=255)),
                ('scheme', models.CharField(blank=True, choices=[('I scheme', 'I scheme'), ('G scheme', 'G scheme')], default='Not Selected', max_length=255)),
                ('curriculam', models.FileField(blank=True, upload_to=educourse.models.upload_file_path)),
            ],
        ),
    ]

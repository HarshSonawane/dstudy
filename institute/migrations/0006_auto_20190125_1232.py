# Generated by Django 2.1.5 on 2019-01-25 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0005_college_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='contact1',
            field=models.BigIntegerField(default='9421487587'),
        ),
        migrations.AddField(
            model_name='college',
            name='email',
            field=models.EmailField(default='ddsi.dstudy@gmail.com', max_length=254),
        ),
    ]

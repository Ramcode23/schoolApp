# Generated by Django 3.2.4 on 2021-08-01 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/courses'),
        ),
    ]

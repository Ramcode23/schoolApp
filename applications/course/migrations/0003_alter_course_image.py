# Generated by Django 3.2.4 on 2021-09-03 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, default='images/courses/no-image.png', null=True, upload_to='images/courses'),
        ),
    ]
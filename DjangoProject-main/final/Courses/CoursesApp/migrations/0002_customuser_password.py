# Generated by Django 4.2.6 on 2023-10-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoursesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Password',
            field=models.CharField(default=123, max_length=64),
            preserve_default=False,
        ),
    ]

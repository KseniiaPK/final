# Generated by Django 4.2.6 on 2023-10-26 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoursesApp', '0002_customuser_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Techer',
            new_name='Teacher',
        ),
    ]

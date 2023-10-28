# Generated by Django 4.2.6 on 2023-10-26 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, unique=True)),
                ('Info', models.CharField(max_length=200)),
                ('Price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=30, unique=True)),
                ('Name', models.CharField(max_length=60)),
                ('Surname', models.CharField(max_length=60)),
                ('Photo', models.ImageField(blank=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='CoursesApp.customuser')),
                ('Bio', models.CharField(max_length=200)),
            ],
            bases=('CoursesApp.customuser',),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CoursesApp.course')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CoursesApp.customuser')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='Subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CoursesApp.subject'),
        ),
        migrations.AddField(
            model_name='course',
            name='Techer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CoursesApp.teacher'),
        ),
    ]

from django.db import models

# Create your models here.
class CustomUser(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    photo = models.ImageField(upload_to="media/", blank=True)

class Teacher(CustomUser):
    bio = models.CharField(max_length=200)


class Subject(models.Model):
    name = models.CharField(max_length=60, unique=True)


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    info = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

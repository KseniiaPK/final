from django.contrib import admin
from .models import CustomUser, Teacher, Course, Subject, Enrollment

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Enrollment)
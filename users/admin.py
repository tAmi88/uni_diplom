from django.contrib import admin
from .models.models import *
# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(TeacherType)
admin.site.register(StudentProfile)

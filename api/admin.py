from django.contrib import admin
from .models import  ClassName, Student, Teacher

@admin.register(ClassName)
class ClassNameAdmin(admin.ModelAdmin):
    list_display = ['id', 'className']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacherName', 'className']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']

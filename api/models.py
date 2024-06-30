from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class ClassName(models.Model):
    className = models.CharField(max_length=100)

    def __str__(self):
        return self.className

class Teacher(models.Model):
    teacherName = models.CharField(max_length=100)
    className = models.ForeignKey(
        ClassName,
        on_delete=models.CASCADE,
        related_name='teachers'
    )

    def __str__(self):
        return self.teacherName

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    className = models.ForeignKey(
        ClassName,
        on_delete=models.CASCADE,
        related_name='students',
        null=True
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='students',
        null=True
    )

    def __str__(self):
        return self.name

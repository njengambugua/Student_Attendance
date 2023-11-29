from django.db import models


class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=16, null=True, blank=True)


def __str__(self):
    return self.firstname


class Course(models.Model):
    coursename = models.CharField(max_length=20)


class StudentCourses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    signed_in = models.DateTimeField()
    signed_out = models.DateTimeField()

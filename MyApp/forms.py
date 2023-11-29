from django import forms
from .models import Student, Course, StudentCourses, Attendance


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'username', 'password']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class StudentCoursesForm(forms.ModelForm):
    class Meta:
        model = StudentCourses
        fields = "__all__"


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Student, Course, StudentCourses, Attendance
from django.utils import timezone


def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        my_user = User.objects.create_user(username, password)
        my_user.save()
        query = Student(firstname=firstname, lastname=lastname, username=username, password=password)
        query.save()
        return redirect('dashboard')
    return render(request, 'sign_up.html')


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact-us.html')


def handle_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = Student.objects.get(username=username, password=password)

        if user:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['firstname'] = user.firstname

            return redirect('dashboard')

    return render(request, 'login.html')


def dashboard(request):
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    firstname = request.session.get('firstname')

    return render(request, 'dashboard.html', {'user_id': user_id, 'username': username, 'firstname': firstname})


def add_course(request):
    if request.method == 'POST':
        course_id = request.POST.get('course')
        student_id = request.session.get('user_id')
        query = StudentCourses(student_id=student_id, course_id=course_id)
        query.save()
        return redirect('dashboard')

    data = Course.objects.all()
    return render(request, 'courses.html', {'courses': data})


def handle_logout(request):
    logout(request)
    return redirect('register')


def update_data(request, id):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')

        edit = Student.objects.get(id=id)
        edit.firstname = firstname
        edit.lastname = lastname
        edit.username = username
        edit.password = password
        edit.save()
        return redirect('dashboard')
    else:
        data = Student.objects.get(id=id)
        return render(request, 'edit.html', {'data': data})


def mark_attendance(request):
    if request.method == 'POST':
        course_id = request.POST.get('course')
        student_id = request.session.get('user_id')
        signed_in = timezone.now()
        signed_out = timezone.now()
        query = Attendance(student_id=student_id, course_id=course_id, signed_in=signed_in, signed_out=signed_out)
        query.save()
        return redirect('dashboard')
    user_id = request.session.get('user_id')
    student_course_data = StudentCourses.objects.filter(student_id=user_id).select_related('student', 'course').all()
    return render(request, 'attendance.html', {'data': student_course_data})


def view_attendance(request):
    user_id = request.session.get('user_id')
    student_course_data = Attendance.objects.filter(student_id=user_id).select_related('student', 'course').all()
    return render(request, 'view_attend.html', {'data': student_course_data})

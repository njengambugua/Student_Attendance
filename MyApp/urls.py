from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.handle_login, name='login'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.handle_logout, name='logout'),
    path('edit/<id>', views.update_data, name='edit'),
    path('courses/', views.add_course, name='courses'),
    path('attendance/', views.mark_attendance, name='attendance'),
    path('view/', views.view_attendance, name='view')
]

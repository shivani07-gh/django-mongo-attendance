from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-student/', views.add_student, name='add_student'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('view-attendance/', views.view_attendance, name='view_attendance'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.mongo_login, name='login'),
    path('logout/', views.mongo_logout, name='logout'),
]

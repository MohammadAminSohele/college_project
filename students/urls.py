from django.urls import path

from . import views

urlpatterns = [
    path('info', views.show_user_info),
    path('course_offerings', views.show_user_course_offerings),
    path('grades', views.show_user_grade),
    path('course', views.show_course),
]
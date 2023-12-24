from django.contrib import admin

from .models import  status,gender,Major,Student,Instructors,degree,Courses,Course_Offerings,Grades,Enrollment,teacher_Offering

# Register your models here.

admin.site.register(status)
admin.site.register(gender)
admin.site.register(Major)
admin.site.register(degree)
admin.site.register(Instructors)
admin.site.register(Student)
admin.site.register(Courses)
admin.site.register(Course_Offerings)
admin.site.register(Grades)
admin.site.register(Enrollment)
admin.site.register(teacher_Offering)
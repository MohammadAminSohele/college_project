from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class status(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class gender(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Major(models.Model):
    name=models.CharField(max_length=30)


    def __str__(self):
        return self.name

class degree(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Student_Number=models.CharField(max_length=15)
    NatCode=models.CharField(max_length=10)
    BirthDate=models.DateField()
    Telephon=models.CharField(max_length=11)
    Mobile=models.CharField(max_length=11)
    Majors=models.ForeignKey(Major,on_delete=models.CASCADE)
    gender=models.ForeignKey(gender,on_delete=models.CASCADE)
    Address=models.CharField(max_length=50)
    DateOfEntering=models.DateField()
    Status=models.ForeignKey(status,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Instructors(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Instructors_Number=models.CharField(max_length=15)
    NatCode=models.CharField(max_length=10)
    BirthDate=models.DateField()
    Telephon=models.CharField(max_length=11)
    Mobile=models.CharField(max_length=11)
    Majors=models.ForeignKey(Major,on_delete=models.CASCADE)
    gender=models.ForeignKey(gender,on_delete=models.CASCADE)
    Address=models.CharField(max_length=50)
    DateOfemployeement=models.DateField()
    Status=models.ForeignKey(status,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# class Semesters(models.Model):
#     name=models.CharField(max_length=20)
#     date_start=models.DateField()
#     date_end=models.DateField()

#     def __str__(self):
#         return self.name

class Courses(models.Model):
    # semester=models.ForeignKey(Semesters,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50)
    unit=models.IntegerField()
    Major=models.ManyToManyField(Major)
    Instructors=models.ForeignKey(Instructors,on_delete=models.CASCADE,null=True)
    time_start=models.DateField()
    time_end=models.DateField()

    def __str__(self):
        return self.name



class Course_Offerings(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    # semester=models.ManyToManyField(Semesters)
    instructors=models.ForeignKey(Instructors,on_delete=models.CASCADE)
    class_Entity=models.IntegerField()
    date_start=models.DateField()
    date_end=models.DateField()

    def __str__(self):
        return self.course.name

class Grades(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    grade=models.IntegerField()
    register_date=models.DateField()

    def __str__(self):
        return self.user.username


class Enrollment(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE) 
    # semester=models.ForeignKey(Semesters,on_delete=models.CASCADE)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)

    def __str__(self):
        return self.course.name


class teacher_Offering(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    teacher=models.ForeignKey(Instructors,on_delete=models.CASCADE)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.teacher.user.username
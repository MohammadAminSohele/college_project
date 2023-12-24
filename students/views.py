from django.shortcuts import render
from django.http import HttpResponseServerError
from django.http import Http404

from students.models import Student,Course_Offerings,Grades,Instructors,Courses,teacher_Offering
from .forms import StudentForm,TeacherForm

# Create your views here.
""" student info """
def show_user_info(request):
    user=request.user
    if user.groups.filter(name='students').exists():
        student=Student.objects.filter(user=request.user).first()
        if student is None:
            raise Http404('دانشجو مورد نظر یافت نشد')
        form=StudentForm(request.POST or None,initial={'NatCode':student.NatCode,'Telephon':student.Telephon,'Mobile':student.Mobile,'Address':student.Address,})
        if form.is_valid():
            NatCode=form.cleaned_data.get('NatCode')
            Telephon=form.cleaned_data.get('Telephon')
            Mobile=form.cleaned_data.get('Mobile')
            Address=form.cleaned_data.get('Address')
            student.NatCode=NatCode
            student.Telephon=Telephon
            student.Mobile=Mobile
            student.Address=Address
            student.save()
    else:
        return HttpResponseServerError("Error: User type not recognized.")
    context={
    'student_info':student,
    'form':form
    }
    return render(request,'user_info.html',context)
""" teacher info """
def show_teacher_info(request):
    user=request.user
    if user.groups.filter(name='teacher').exists():
        Instructors_info=Instructors.objects.filter(user=request.user).first()
        if Instructors_info is None:
            raise Http404('استاد مورد نظر یافت نشد')
        form=TeacherForm(request.POST or None,initial={'NatCode':Instructors_info.NatCode,'Telephon':Instructors_info.Telephon,'Mobile':Instructors_info.Mobile,'Address':Instructors_info.Address,})
        if form.is_valid():
            NatCode=form.cleaned_data.get('NatCode')
            Telephon=form.cleaned_data.get('Telephon')
            Mobile=form.cleaned_data.get('Mobile')
            Address=form.cleaned_data.get('Address')
            Instructors_info.NatCode=NatCode
            Instructors_info.Telephon=Telephon
            Instructors_info.Mobile=Mobile
            Instructors_info.Address=Address
            Instructors_info.save()
    else:
        return HttpResponseServerError("Error: User type not recognized.")
    context={
        'Instructors_info':Instructors_info,
        'form':form
    }
    return render(request,'teacher_info.html',context)

""" course offerings """
def show_user_course_offerings(request):
    user=request.user
    if user.groups.filter(name='students').exists():
        course_offerings=Course_Offerings.objects.filter(user=request.user).all()
    else:
        return HttpResponseServerError("Error: User type not recognized.")
    return render(request,'show_user_course_offerings.html',{'course_offerings':course_offerings})    
""" user grade """
def show_user_grade(request):
    user=request.user
    if user.groups.filter(name='students').exists():
        grades=Grades.objects.filter(user=request.user).all()
    else:
        return HttpResponseServerError("Error: User type not recognized.")
    return render(request,'show_user_grade.html',{'grades':grades})

""" show course of term """
def show_course(request):
    user=request.user
    if user.groups.filter(name='students').exists():
        course=Courses.objects.filter(user).all()
    else:
        return HttpResponseServerError("Error: User type not recognized.")
    return render(request,'show_course.html',{'course':course})


""" show teacher cours offerings """

def show_teacher_course_offering(request):
    user=request.user
    if user.groups.filter(name='teacher').exists():
        teacher_offer=teacher_Offering.objects.filter(user=request.user).all()
    else:
        return HttpResponseServerError("Error: User type not recognized.")
    context={
        'teacher_offer':teacher_offer
    }
    return render(request,'show_teacher_course_offerings.html',context)
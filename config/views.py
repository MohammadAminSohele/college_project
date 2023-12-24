from django.shortcuts import render
from django.contrib.auth.models import User

def show_user_profile(request):
    return render(request,'user_profile.html',{})
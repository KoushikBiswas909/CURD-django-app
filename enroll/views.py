from django.shortcuts import render, HttpResponseRedirect

from enroll.models import User
from .forms import StudentRegistration
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here. Templets are render through views

# This function will add new Item and Show all Items
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data["name"]
            em = fm.cleaned_data["email"]
            pw = fm.cleaned_data["password"]
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, "enroll/addandshow.html", {"form": fm, "stu": stud})


# This fuction will Update or Edit
def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, "enroll/updatestudent.html", {"form": fm})


# This fuction wll delete
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")


# User Register
def register(request):
    form = UserCreationForm
    if request.method == "POST":
        regForm = UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request, "User has been registered.")
        else:
            messages.warning(request, "Enter details again")
    return render(request, "registration/register.html", {"form": form})


# https://www.geeksforgeeks.org/django-sign-up-and-login-with-confirmation-email-python/            [check today]

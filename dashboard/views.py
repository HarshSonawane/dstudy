from django.shortcuts import render, redirect, reverse
from django.conf import settings


def index(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "dashboard/index.html", {})

def profile(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "dashboard/maintainance.html", {})

def change_password(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "dashboard/maintainance.html", {})

def edit_profile(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "dashboard/maintainance.html", {})

def notifications(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "dashboard/maintainance.html", {})

def courses(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "dashboard/maintainance.html", {})

def exams(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "dashboard/maintainance.html", {})

def college_notes(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "dashboard/maintainance.html", {})

def progress(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "dashboard/maintainance.html", {})

def attendance(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "dashboard/maintainance.html", {})

def dstudy_notes(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "dashboard/maintainance.html", {})

def student_notes(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "dashboard/maintainance.html", {})






from django.shortcuts import render, redirect, reverse
from django.conf import settings


def index(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "user/index.html", {})

def profile(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "user/profile.html", {})

def change_password(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "user/change_password.html", {})

def edit_profile(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "user/edit_profile.html", args)

def notifications(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "user/notifications.html", {})

def courses(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "user/courses.html", {})

def exams(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "user/exams.html", {})

def college_notes(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "user/college_notes.html", {})

def progress(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "user/progress.html", {})

def attendance(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "user/attendance.html", {})

def dstudy_notes(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "user/dstudy_notes.html", {})

def student_notes(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "user/student_notes.html", {})






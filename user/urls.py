from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from .views import index, profile, change_password, edit_profile, notifications, courses, college_notes, exams, progress, attendance, dstudy_notes, student_notes

urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change_password/', change_password, name='change_password'),
    path('notifications/', notifications, name='notifications'),
    path('courses/', courses, name='courses'),
    path('college_notes/', college_notes, name='college_notes'),
    path('exams/', exams, name='exams'),
    path('progress/', progress, name='progress'),
    path('attendance/', attendance, name='attendance'),
    path('dstudy_notes/', dstudy_notes, name='dstudy_notes'),
    path('student_notes/', student_notes, name='student_notes'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

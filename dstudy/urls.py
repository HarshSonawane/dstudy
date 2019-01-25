from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin




from .views import index

from .views import index, CollegeListView, CollegeDetailSlugView, UniversityListView, UniversityDetailSlugView, SubjectListView, QuetionPaperListView, ModelAnswerPaperListView, CurriculamListView, EduCourseListView, help, contact, enquiry, about, services, careers, seminars, workshops, terms, privacy

urlpatterns = [
    path('', index, name='main_index'),
    path('help', help, name='help'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('careers', careers, name='careers'),

    path('seminars', seminars, name='seminars'),
    path('workshops', workshops, name='workshops'),
    path('terms', terms, name='terms'),
    path('privacy', privacy, name='privacy'),

    path('contact', contact, name='contact'),
    path('enquiry', enquiry, name='enquiry'),



    path('colleges/', CollegeListView.as_view(), name='colleges'),
    path('universities/', UniversityListView.as_view(), name='universities'),
    path('colleges/<slug>/', CollegeDetailSlugView.as_view()),
    path('universities/<slug>/', UniversityDetailSlugView.as_view()),

    path('subjects/', SubjectListView.as_view(), name='subjects'),
    path('courses/', EduCourseListView.as_view(), name='academic_courses'),
    path('quetionpapers/', QuetionPaperListView.as_view(), name='quetionpapers'),
    path('modelanswerpapers/', ModelAnswerPaperListView.as_view(), name='modelanswerpapers'),
    path('curriculms/', CurriculamListView.as_view(), name='curriculms'),

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    #path('user/', include('user.urls')),
    path('dashboard', include('dashboard.urls'), name='dashboard'),
] 

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#url(r'^login/', LoginView.as_view(), name="index_login"),
#url(r'^signup/', SignupView.as_view(), name="index_signup"),
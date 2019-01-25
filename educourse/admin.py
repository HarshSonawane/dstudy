from django.contrib import admin
from .models import EduCourse, Subject, QuetionPaper, ModelAnswerPaper, Curriculam


class EduCourseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = EduCourse

admin.site.register(EduCourse, EduCourseAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Subject

admin.site.register(Subject, SubjectAdmin)

class QuetionPaperAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = QuetionPaper

admin.site.register(QuetionPaper, QuetionPaperAdmin)

class ModelAnswerPaperAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = QuetionPaper

admin.site.register(ModelAnswerPaper, ModelAnswerPaperAdmin)

class CurriculamAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Curriculam

admin.site.register(Curriculam, CurriculamAdmin)
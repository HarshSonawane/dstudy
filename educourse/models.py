import random
import os
import datetime
from django.db import models
from django.db.models.signals import pre_save, post_save
from .validators import validate_file_extension

from institute.models import University


from dstudy.utils import unique_slug_generator


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_file_path(instance, filename):
    new_filename = random.randint(1, 3231546414654785)
    name, ext =get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "pdfs/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class EduCourseManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class EduCourse(models.Model):
    level_choices    = (("Under Graduate","Under Graduate"),("Diploma ","Diploma"))
    duration_choices    = (("2  Year","2  Year"),("3  Year ","3  Year"))
    title             = models.CharField(max_length=500)
    slug                = models.SlugField(blank=True, unique=True)
    course             = models.CharField(max_length=5)
    level            = models.CharField(choices=level_choices,max_length=255, default='Not Selected', null=False, blank=True)
    duration            = models.CharField(choices=duration_choices,max_length=255, default='Not Selected', null=False, blank=True)
    university          = models.ForeignKey(University, on_delete=models.CASCADE)
    curriculam          =   models.FileField(upload_to=upload_file_path, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    objects = EduCourseManager()

    def __str__(self):
        return self.title

def educourse_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(educourse_pre_save_receiver, sender=EduCourse)


class SubjectManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class Subject(models.Model):
    study_year_choices  = (("First Year(1st)","First Year(1st)"),("Second Year(2nd)","Second Year(2nd)"),("Third Year(3rd)","Third Year(3rd)"))
    title               = models.CharField(max_length=500)
    slug                = models.SlugField(blank=True, unique=True)
    code                = models.CharField(max_length=5)
    study_year          = models.CharField(choices=study_year_choices,max_length=255, default='Not Selected', null=False, blank=False)
    course              = models.ForeignKey(EduCourse, on_delete=models.CASCADE)
    syllabus            = models.FileField(upload_to=upload_file_path, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)


    objects = SubjectManager()

    def __str__(self):
        return self.title

def subject_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(subject_pre_save_receiver, sender=Subject)

class QuetionPaperManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class QuetionPaper(models.Model):
    exam_time_choices   = (("Summer","Summer"),("Winter","Winter"))
    scheme_choices      = (("E","E"),("G","G"),("I","I"),("M","M"))
    title               = models.CharField(max_length=500)
    slug                = models.SlugField(blank=True, unique=True)
    code                = models.CharField(max_length=10)
    exam_year           = models.IntegerField()
    exam_time           = models.CharField(choices=exam_time_choices,max_length=255, default='Not Selected', null=False, blank=False)
    subject             = models.ForeignKey(Subject, on_delete=models.CASCADE)
    scheme              = models.CharField(choices=scheme_choices,max_length=255, default='Not Selected', null=False, blank=False)
    file                = models.FileField(upload_to=upload_file_path, blank=False, validators=[validate_file_extension])
    max_marks           = models.IntegerField(default=100, blank=False, null=None)
    min_marks           = models.IntegerField(default=40, blank=False, null=None)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)


    objects = QuetionPaperManager()

    def __str__(self):
        return self.title

def quetionpaper_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(quetionpaper_pre_save_receiver, sender=QuetionPaper)


class ModelAnswerPaperManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class ModelAnswerPaper(models.Model):
    exam_time_choices   = (("Summer","Summer"),("Winter","Winter"))
    scheme_choices      = (("E","E"),("G","G"),("I","I"),("M","M"))
    title               = models.CharField(max_length=500)
    slug                = models.SlugField(blank=True, unique=True)
    code                = models.CharField(max_length=10)
    exam_year           = models.IntegerField()
    exam_time           = models.CharField(choices=exam_time_choices,max_length=255, default='Not Selected', null=False, blank=False)
    subject             = models.ForeignKey(Subject, on_delete=models.CASCADE)
    scheme              = models.CharField(choices=scheme_choices,max_length=255, default='Not Selected', null=False, blank=False)
    file                = models.FileField(upload_to=upload_file_path, blank=False, validators=[validate_file_extension])
    max_marks           = models.IntegerField(default=100, blank=False, null=None)
    min_marks           = models.IntegerField(default=40, blank=False, null=None)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)


    objects = ModelAnswerPaperManager()

    def __str__(self):
        return self.title

def modelanswerpaper_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(modelanswerpaper_pre_save_receiver, sender=ModelAnswerPaper)


class CurriculamManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class Curriculam(models.Model):
    scheme_choices      = (("E","E"),("G","G"),("I","I"),("M","M"))
    title               = models.CharField(max_length=500)
    slug                = models.SlugField(blank=True, unique=True)
    subject             = models.ForeignKey(Subject, on_delete=models.CASCADE)
    scheme              = models.CharField(choices=scheme_choices,max_length=255, default='Not Selected', null=False, blank=False)
    file                = models.FileField(upload_to=upload_file_path, blank=False, validators=[validate_file_extension])
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)


    objects = CurriculamManager()

    def __str__(self):
        return self.title

def curriculam_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(curriculam_pre_save_receiver, sender=Curriculam)


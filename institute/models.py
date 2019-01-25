import random
import os
from django.db import models
from django.db.models.signals import pre_save, post_save
from dstudy.utils import unique_slug_generator

# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_logo_path(instance, filename):
    new_filename = random.randint(1, 3231546414654785)
    name, ext =get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "logos/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class UniversityManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class University(models.Model):
    state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    title    = models.CharField(max_length=500)
    slug    = models.SlugField(blank=True, unique=True)
    logo    = models.ImageField(upload_to=upload_logo_path, null=True, blank=True)
    address = models.CharField(max_length=500)
    state   = models.CharField(choices=state_choices,max_length=255, default='Maharashtra', null=False, blank=True)
    district = models.CharField(max_length=100)
    city    = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    type    = models.CharField(max_length=250)
    website = models.URLField()
    phone = models.BigIntegerField(default='9421487587')
    fax = models.BigIntegerField(default='0000000000')
    email    = models.EmailField(default='ddsi.dstudy@gmail.com')
    rank    = models.CharField(max_length=50)

    objects = UniversityManager()

    def __str__(self):
        return self.title

def university_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(university_pre_save_receiver, sender=University)

class CollegeManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None



class College(models.Model):
    state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    title    = models.CharField(max_length=500)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    slug    = models.SlugField(blank=True, unique=True)
    logo    = models.ImageField(upload_to=upload_logo_path, null=True, blank=True, default='logo.png')
    address = models.CharField(max_length=500)
    state   = models.CharField(choices=state_choices,max_length=255, default='Maharashtra', null=False, blank=True)
    district = models.CharField(max_length=100)
    city    = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    website = models.URLField(default='dstudy.ddsweb.in')
    contact1 = models.BigIntegerField(default='9421487587')
    contact2 = models.BigIntegerField(default='9421487587')
    email    = models.EmailField(default='ddsi.dstudy@gmail.com')
    rank    = models.CharField(max_length=50)

    objects = CollegeManager()

    def __str__(self):
        return self.title

def college_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(college_pre_save_receiver, sender=College)
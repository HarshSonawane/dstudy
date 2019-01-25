from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    STUDENT = 1
    TEACHER = 2
    HOD = 3
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (HOD , 'HOD'),
    )
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER , 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/%y/%m/%d/', default='img/uploads/user.png')
    mobile = models.CharField(max_length=15, null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


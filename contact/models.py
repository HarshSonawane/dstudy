from django.db import models

# Create your models here.

class ContactManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class Contact(models.Model):
    #type_choices        = (("Reporting Problem","Reporting Problem"),("Feedback","Feedback"),("Not Specific","Not Specific"))
    name                = models.CharField(max_length=500)
    email               = models.EmailField()
    phone               = models.BigIntegerField()
    subject             = models.CharField(max_length=500)
    type                = models.CharField(max_length=100)
    message             = models.TextField()
    #type                = models.CharField(choices=type_choices, max_length=255, default='Not Selected', null=False, blank=False)
    created_at          = models.DateTimeField(auto_now_add=True)
    user_id             = models.IntegerField(blank=True)


    objects = ContactManager()

    def __str__(self):
        return self.name


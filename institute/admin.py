from django.contrib import admin
from .models import College, University

# Register your models here.

class CollegeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = College

admin.site.register(College, CollegeAdmin)

class UniversityAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = University

admin.site.register(University, UniversityAdmin)
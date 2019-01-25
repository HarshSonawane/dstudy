from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'phone', 'created_at']
    class Meta:
        model = Contact

admin.site.register(Contact, ContactAdmin)
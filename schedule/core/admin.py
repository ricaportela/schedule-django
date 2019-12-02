from django.contrib import admin
from .models import Contact, PhoneNumberContact


admin.site.register(Contact)
admin.site.register(PhoneNumberContact)
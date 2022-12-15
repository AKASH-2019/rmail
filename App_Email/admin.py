

from django.contrib import admin
from .models import Email, EmailCategory

# Register your models here.
admin.site.register(Email)
admin.site.register(EmailCategory)
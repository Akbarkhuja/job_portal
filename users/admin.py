from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *


User = get_user_model()

class GeneralAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_applicant", "is_recruiter", "is_admin")

admin.site.register(User, GeneralAdmin)
admin.site.register(Applicant)
admin.site.register(Recruiter)
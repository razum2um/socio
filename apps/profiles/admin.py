__author__ = 'nimnull'
from django.contrib import admin
from models import UserProfile

class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'sex', 'birth_date',)

admin.site.register(UserProfile, ProfileAdmin)
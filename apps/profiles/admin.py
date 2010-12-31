__author__ = 'nimnull'
from django.contrib import admin
from models import UserProfile

class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'avatar', 'sex', 'birth_date', 'show_bd', 'summary')

admin.site.register(UserProfile, ProfileAdmin)
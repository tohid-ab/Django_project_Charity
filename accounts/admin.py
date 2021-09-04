from django.contrib import admin
from .models import *
# Register your models here.


class ProfileUser(admin.ModelAdmin):
    list_display = ('image_tag', 'user')
    search_fields = ('user',)


admin.site.register(Profile, ProfileUser)
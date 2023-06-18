from django.contrib import admin
from.models import Profile 
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserAdmin(UserAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['password','date_joined','last_login']
        else:
            return []
        
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Profile)
from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'room']


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
#
# from users.models import UserProfile
#
#
# class UserProfileInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False
#     verbose_name_plural = 'user profile'
#
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (UserProfileInline, )
#
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

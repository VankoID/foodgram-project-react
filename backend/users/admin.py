from django.contrib import admin

from .models import Subscribe, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    list_filter = ('username', 'email')


admin.site.register(User, UserAdmin)
admin.site.register(Subscribe)

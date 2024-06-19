from django.contrib import admin
from .models import MyUser, Email

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_admin', 'is_active')
    search_fields = ('email',)
    readonly_fields = ('id',)

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'created_at')
    search_fields = ('subject', 'body')
    readonly_fields = ('id', 'created_at')

from django.contrib import admin
from .models import User, Step

# Register your models here.

@admin.register(User)
class UserSessionAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_session', 'message','timestamp',)

@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ('current_state',)

# @admin.register(Log)
# class LogAdmin(admin.ModelAdmin):
#     list_display = ('user_log', 'message', 'timestamp')
    

from django.contrib import admin
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Teacher, TeacherAdmin)

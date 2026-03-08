
# Register your models here.

from django.contrib import admin
from .models import Student, Department

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_number', 'age', 'department']
    list_filter = ['department', 'age']
    search_fields = ['name', 'roll_number']
    ordering = ['name']

admin.site.register(Student, StudentAdmin)
admin.site.register(Department)
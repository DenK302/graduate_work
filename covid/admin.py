from django.contrib import admin
from .models import Employer

# Register your models here.


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'department', 'position', 'wantmake')


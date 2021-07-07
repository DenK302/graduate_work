from django.contrib import admin
from .models import Research, Student, Teacher

# Register your models here.
# admin.site.register(Research)
admin.site.register(Teacher)


# admin.site.register(Work)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'category', 'date_start', 'date_end')


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('topic', 'student', 'teacher')

# admin.site.register(Student, StudentAdmin)

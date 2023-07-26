from django.contrib import admin

from StudentApp.models import Course, City, Student

# Register your models here.
admin.site.register(Course)
admin.site.register(City)
admin.site.register(Student)

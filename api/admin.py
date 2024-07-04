from django.contrib import admin
from .models import University, College, Department, Course, Student

# Register your models here

tables = ["University", "College", "Department", "Course", "Student"]
for table in tables:
    admin.site.register(table)

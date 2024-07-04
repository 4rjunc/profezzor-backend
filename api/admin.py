from django.contrib import admin
from .models import University, College, Department, Course, Student

# List of models to register
models = [University, College, Department, Course, Student]

for model in models:
    admin.site.register(model)

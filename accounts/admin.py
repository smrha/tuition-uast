from django.contrib import admin
from .models import Lesson
from import_export.admin import ImportExportModelAdmin

@admin.register(Lesson)
class LessonAdmin(ImportExportModelAdmin):
    pass
from django.contrib import admin
from .models import UserProfile, Lesson
from import_export.admin import ImportExportModelAdmin

# admin.site.register(UserProfile)
# admin.site.register(Lesson)
@admin.register(UserProfile)
class UserProfileAdmin(ImportExportModelAdmin):
    pass

@admin.register(Lesson)
class LessonAdmin(ImportExportModelAdmin):
    pass
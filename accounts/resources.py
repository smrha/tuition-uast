from .models import Lesson
from import_export import resources

class LessonResource(resources.ModelResource):
    
    class Meta:
        model = Lesson
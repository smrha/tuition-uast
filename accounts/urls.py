from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('teachers/', views.teachers_list, name='teachers_list'),
    path('teachers/<int:pk>', views.teacher_detail, name='teacher_detail'),
    path('teachers/<int:pk>/edit', views.teacher_edit, name='teacher_edit'),
    path('teachers/<int:pk>/add', views.lesson_add, name='lesson_add'),
]
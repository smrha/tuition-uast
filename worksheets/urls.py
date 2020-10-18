from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='worksheet_index'),
    path('project/add/', views.project_add, name='project_add'),
    path('project/list/', views.project_list, name='project_list'),
    path('project/show/<int:pk>/', views.project_show, name='project_show'),
]
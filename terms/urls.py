from django.urls import path
from . import views

urlpatterns = [
    path('', views.terms_index, name='terms_index'),
    path('add', views.term_add, name='term_add'),
]
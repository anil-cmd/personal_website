from django.urls import path

from . import views

urlpatterns = [
    path('', views.projects, name='works'),
    path('resume/', views.resume, name='resume')
]

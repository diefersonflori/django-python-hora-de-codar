from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path('h', views.helloworld),
    path('', views.tasklist,name='task-list'),
]

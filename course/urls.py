from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.course_list, name='course_list'),
    path('<str:slug>/details/', views.details, name='details'),
    path('<str:course_slug>/<str:lesson_slug>/details/', views.lesson_detail, name='lesson_detail'),
]

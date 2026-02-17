from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test),
    path('test2',views.test2),
    path('home',views.home),
    path('about',views.about),
    path('contact',views.contact),
]
from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test),
    path('test2',views.test2),
    path('home',views.home),
    path('about',views.about),
    path('contact',views.contact),
    path('design',views.design),
    path('index', views.index),
    path('add', views.add),
    path('summ', views.summ),
    path('college',views.college),
    path('registration', views.registration),
    path('password', views.password),
    path('insert', views.insert),
    path('ins', views.ins),
    path('student1',views.student1),
    path('val', views.val),
]
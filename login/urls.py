from django.urls import path
from login import views
urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('search/', views.search),
    path('display/', views.display)

]
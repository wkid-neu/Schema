from django.urls import path
from MapSchema import views

urlpatterns = [
    path('display/', views.map_index),
    path('enter/',views.enter),
    path('form/',views.form)
]

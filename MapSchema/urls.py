from django.urls import path
from MapSchema import views

urlpatterns = [
    path('display/<type>/', views.map_index),
    path('process/', views.process_form),
    path('get_points/',views.get_points)
]

from django.urls import path
from MapSchema import views

urlpatterns = [
    path('display/<type>/', views.map_index),
    path('process/', views.process_form),
    path('get_points/', views.get_all_points),
    path('delete_point/', views.delete_point),
    path('edit_users/', views.edit_users),
    path('edit_process/', views.edit_process),
    path('update/', views.update)

]

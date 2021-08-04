from django.urls import path
from createobject import views

urlpatterns = [
    path('index/', views.check),
    path('search/', views.search),
    path('creating/<entityname>/', views.creating),
    path('generating/', views.generating),
    path('looking/<entity_id>/', views.get_the_entity),
    path('process/', views.process),
    path('obtaining/',views.obtaining),
    path('get_the_entity/',views.get_the_entity)
]

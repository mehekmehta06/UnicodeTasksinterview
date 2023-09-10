from django.urls import path
from . import views

urlpatterns = [
    #path('',views.pokemon_types),
    path('',views.pokemon_by_type),
]

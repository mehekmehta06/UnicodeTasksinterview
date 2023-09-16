from django.urls import path
from . import views

urlpatterns = [
    path('display',views.pokemon_types),
    path('select',views.pokemon_by_type),
]

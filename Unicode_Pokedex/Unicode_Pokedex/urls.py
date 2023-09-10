from django.urls import path
from django.urls import include
from pokedex_app import views

urlpatterns = [
    #path('pokedex/', include('pokedex_app.urls')),
    path('pokemon_form/',include('pokedex_app.urls')),
]

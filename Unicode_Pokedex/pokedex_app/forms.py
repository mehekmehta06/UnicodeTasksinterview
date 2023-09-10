

from django import forms

class PokemonTypeForm(forms.Form):
    type_choices = [
        ('grass', 'Grass'),
        ('fire', 'Fire'),
        ('water', 'Water'),
        
    ]

    type = forms.ChoiceField(choices=type_choices, label='Select a Pokémon Type')

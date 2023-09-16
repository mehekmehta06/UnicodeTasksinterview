

from django import forms

class PokemonTypeForm(forms.Form):
    type_choices = [
        ('grass', 'Grass'),
        ('fire', 'Fire'),
        ('water', 'Water'),
         ('normal','Normal'),
          ('fighting','Fighting'),
           ('flying','Flying'),
           ('shadow','Shadow')
        ]
        
    type = forms.ChoiceField(choices=type_choices, label='Select a Pokémon Type') 
        
        
        
    

   

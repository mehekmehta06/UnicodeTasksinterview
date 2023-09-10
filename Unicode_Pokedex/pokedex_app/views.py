"""
import requests
from django.http import JsonResponse

def pokemon_types(request):

    api_url1 = 'https://pokeapi.co/api/v2/type/'
    api_url2 = 'https://pokeapi.co/api/v2/ability'

    try:
        
        response1 = requests.get(api_url1)
        response_data1 = None

        if response1.status_code == 200:
            data1 = response1.json()
            types = [entry['name'] for entry in data1['results']]
            response_data1 = {'types': types}
        else:
            response_data1 = {'error': 'Failed to fetch data from PokeAPI'}

        
        response2 = requests.get(api_url2)
        response_data2 = None

        if response2.status_code == 200:
            data2 = response2.json()
            abilities = [entry['name'] for entry in data2['results']]
            response_data2 = {'ability': abilities}
        else:
            response_data2 = {'error': 'Failed to fetch data from the second API'}

        combined_response_data = [response_data1,response_data2]

        return JsonResponse(combined_response_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)})

"""    

import requests
from django.http import JsonResponse
from django.shortcuts import render
from .forms import PokemonTypeForm

def pokemon_by_type(request):
    if request.method == 'POST':
        form = PokemonTypeForm(request.POST)
        if form.is_valid():
            selected_type = form.cleaned_data['type']

            api_url = f'https://pokeapi.co/api/v2/type/{selected_type}'
           
            try:
                response= request.GET.get(api_url)
                if response.status_code == 200:
                    data = response.json()

                    pokemon_list = [entry['pokemon']['name'] for entry in data['pokemon']]

                    return render(request, 'pokedex_app/pokemon_list.html', {'pokemon_list': pokemon_list})
                else:
                    return render(request, 'pokedex_app/error.html', {'error_message': error_message})
                
            except Exception as e:
                error_message = str(e)
                return render(request, 'pokedex_app/error.html', {'error_message': error_message})

    else:
        form = PokemonTypeForm()

    return render(request, 'pokedex_app/type_selection.html', {'form': form})

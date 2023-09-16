
import requests
from django.http import JsonResponse
from django.shortcuts import render
from .forms import PokemonTypeForm


def pokemon_types(request):

    api_url1 = 'https://pokeapi.co/api/v2/type/'
    api_url2 = 'https://pokeapi.co/api/v2/ability'
    api_url3 = 'https://pokeapi.co/api/v2/egg-group'
    api_url4 = 'https://pokeapi.co/api/v2/nature'

    try:
        #pokemon types
        response1 = requests.get(api_url1)
        
        if response1.status_code == 200:
            data1 = response1.json()
            types = [entry['name'] for entry in data1['results']]
            response_data1 = {'types': types}
        else:
            response_data1 = {'error': 'Failed to fetch data from PokeAPI'}
        #pokemon abilities
        response2 = requests.get(api_url2)
        
        if response2.status_code == 200:
            data2 = response2.json()
            abilities = [entry['name'] for entry in data2['results']]
            response_data2 = {'ability': abilities}
        else:
            response_data2 = {'error': 'Failed to fetch data from the second API'}
        #pokemon eggGroup
        response3 = requests.get(api_url3)
       
        if response3.status_code == 200:
            data3 = response3.json()
            eggGroups = [entry['name'] for entry in data3['results']]
            response_data3 = {'EggGroup': eggGroups}
        else:
            response_data3 = {'error': 'Failed to fetch data from PokeAPI'}
        #pokemon natures
        response4 = requests.get(api_url4)
        
        if response4.status_code == 200:
            data4 = response4.json()
            natures = [entry['name'] for entry in data4['results']]
            response_data4 = {'Nature': natures}
        else:
            response_data4 = {'error': 'Failed to fetch data from PokeAPI'}
        #json response method
        #combined_response_data = [response_data1,response_data2,response_data3,response_data4]
         #return JsonResponse(combined_response_data, safe=False)
        #template method
        return render(request, 'pokedex_app/pokemon_types.html',{'types': types,'abilities': abilities,'eggGroups': eggGroups,'natures':natures})

    except Exception as e:
        #return JsonResponse({'error': str(e)})
        error_message = str(e)
        return render(request, 'pokedex_app/error.html', {'error_message': error_message})

   
def pokemon_by_type(request):
    if request.method == 'POST':
        form = PokemonTypeForm(request.POST)
        if form.is_valid():
            selected_type = form.cleaned_data['type']

            api_url = f'https://pokeapi.co/api/v2/type/{selected_type}'
           
            try:
                response= requests.get(api_url)
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

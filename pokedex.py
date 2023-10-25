import requests 
import json

ability_pokemon = []

def getPokemon():
    pokemon_name = input("Digite o nome do pokemon: ")
    
    return pokemon_name.strip()

pokemon_name = getPokemon()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

request = requests.get(url)
request_json = json.loads(request.content)

print(f"O nome do pokémon é: {request_json['name']}")
for i in range(0,2):
    ability_pokemon.append(request_json['abilities'][i]['ability']['name'])

print(f"As habilidades do pokemon são: {ability_pokemon}")
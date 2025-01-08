import requests
import json

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data for {name}. Status code: {response.status_code}")
        return None

# List of Pokémon names
get_pokemon = [
    "eevee", "vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"  
]

pokemon_dict = {}

for pokemon_name in get_pokemon:
    pokemon_info = get_pokemon_info(pokemon_name)
    if pokemon_info:
        pokemon_dict[pokemon_name] = {
            "id": pokemon_name,
            "name": pokemon_name,
            "pokedexId": pokemon_info["id"],
            "types": [t['type']['name'] for t in pokemon_info['types']],
            "image_url": ""
        }
        print(f"Processed: {pokemon_name}")

# Write to JSON file
with open('poke_data.json', 'w') as f:
    json.dump(pokemon_dict, f, indent=2)

print("JSON file created successfully.")

import requests
import json

# Base URL for the API
BASE_URL = "https://pokeapi.co/api/v2/"

# Function to retrieve Pokémon data from the API
def get_pokemon_info(name):
    url = f"{BASE_URL}pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data for {name} (Status Code: {response.status_code})")
        return None

# Function to process and save Pokémon data
def fetch_and_save_pokemon(pokemon_list, output_file):
    all_pokemon_data = []

    for name in pokemon_list:
        print(f"Fetching data for {name}...")
        data = get_pokemon_info(name)
        if data:
            # Extract relevant fields
            pokemon_info = {
                "name": data["name"],
                "id": data["id"],
                "types": [t['type']['name'] for t in data['types']],
            }
            all_pokemon_data.append(pokemon_info)

    # Save to JSON file
    with open(output_file, "w") as json_file:
        json.dump(all_pokemon_data, json_file, indent=4)
    print(f"Data saved to {output_file}")

# Read Pokémon names from a file
def read_pokemon_names_from_file(filename):
    try:
        with open(filename, "r") as file:
            pokemon_names = file.readlines()
        # Remove extra spaces and normalize case
        return [name.strip().lower() for name in pokemon_names]
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []

# File containing Pokémon names (one name per line)
input_file = "pokemon_names.txt"
output_file = "pokemon_data.json"

# Fetch Pokémon names from the file
pokemon_list = read_pokemon_names_from_file(input_file)

if pokemon_list:
    # Fetch data and save
    fetch_and_save_pokemon(pokemon_list, output_file)
else:
    print("No Pokémon names found in the file.")

# A blueprint is a way to organize and structure a Flask application into reusable components
from flask import Blueprint, render_template, request, jsonify
import json
import requests
from website.services import DBcosmos
# from website.Azure_Services import cosmos_service

views = Blueprint('views', __name__)

Azure_Function_URL = "http://127.0.0.1:7071/api/poke"

@views.route('/')  # These define the routes, e.g. http://127.0.0.1:5000/ Returns "Home"
def home():
    return render_template("home.html")

@views.route('/search', methods=['GET', 'POST'])  # These define the routes, e.g. http://
def search():
    
    if request.method == 'POST':
        poke_name = request.form["name"]
        response = requests.get(f"{Azure_Function_URL}/{poke_name}")
        pokemon_data = response.json()
        return render_template("poke_result.html", poke = pokemon_data)
    else:
        return "Error: Pokémon not found"
''' 
if request.method == 'POST': 
    ptype = request.form['poke_type']
    response = request.get(Azure_Function_URL + ptype)

if request.method == 'POST':
    pokedexId = request.form['pokedex_id']
    response = request.get(Azure_Function_URL + pokedexId)
'''
        

       
        
     





'''
    # Get user input from query parameters
    name = request.args.get('name')
    ptype = request.args.get('ptype')
    pokedexId = request.args.get('pokedexId')

    # Build a query dictionary based on user input
    query = {}
    
    if name: 
        query['name'] = name.lower()
    if ptype:
        query['ptype'] = ptype.lower()
    if pokedexId: 
        query['pokedexId'] = int(pokedexId)
        
    # Fetch data from Cosmos DB using a service layer function
    pokemon_data = DBcosmos.get_pokemon_by_query(query)
    
    # Check if data was found
    if not pokemon_data:
        return jsonify({"error": "No Pokémon found matching your criteria"}),404
    else:   # Return a rendered template with the data
        return render_template("poke_result.html", poke = pokemon_data)
'''


# A blueprint is a way to organize and structure a Flask application into reusable components
from flask import Blueprint, render_template, request, jsonify
from website.services import DBcosmos
# from website.Azure_Services import cosmos_service

views = Blueprint('views', __name__)


@views.route('/')  # These define the routes, e.g. http://127.0.0.1:5000/ Returns "Home"
def home():
    return render_template("home.html")

@views.route('/search', methods=['GET']) 
def search():
    # Get user input from query parameters
    name = request.args.get('name')
    ptype = request.args.get('ptype')
    pokedex_id = request.args.get('pokedex_id')

    # Build a query dictionary based on user input
    query = {}
    
    if name: 
        query['name'] = name.lower()
    if ptype:
        query['ptype'] = ptype.lower()
    if pokedex_id: 
        query['pokedex_id'] = int(pokedex_id)
        
    # Fetch data from Cosmos DB using a service layer function
    pokemon_data = DBcosmos.get_pokemon_by_query(query)
    
    # Check if data was found
    if not pokemon_data:
        return jsonify({"error": "No Pokémon found matching your criteria"}),404
    else:   # Return a rendered template with the data
        return render_template("poke_result.html", poke = pokemon_data)
    
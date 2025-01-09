# A blueprint is a way to organize and structure a Flask application into reusable components
from flask import Blueprint, render_template, request, jsonify
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
    
    # Check if data was found

    # Return a rendered template with the data
    render_template("poke_result.html")

'''
@views.route('/results') # Dont need this, this is just to make sure it works. The "def search():" function will return "poke_result.html" 
def poke_result():
    return render_template("poke_result.html")
'''
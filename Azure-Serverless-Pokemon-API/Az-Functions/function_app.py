import azure.functions as func
import json


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="poke/{name}", methods=["GET"])
def GetPoke(req: func.HttpRequest) -> func.HttpResponse:
    
    poke_name = req.route_params.get('name')
   # poke_type = req.params.get('ptype')
  #  poke_id = req.params.get('pokedex_id')
    
    if not poke_name:
        return func.HttpResponse(
            "Please pass a name on the path",
            status_code=400
        )
 
    pokemon_info = {
        "name": 'eevee',
        "ptype": 'normal',
        "pokedex_id": 123
    }

    if poke_name:
        return func.HttpResponse(json.dumps(pokemon_info), mimetype="application/json", status_code=200)  

# Function to get the User input from 'views.py | def search' . e.g. from website.views import search


# Based on the input build a query to retrieve data from Cosmos DB | e.g. if name = 'Eevee' then query = {'name': 'eevee'}

## Return the data as a JSON response |

    
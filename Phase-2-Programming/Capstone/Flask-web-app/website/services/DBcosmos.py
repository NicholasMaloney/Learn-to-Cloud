# Logic for querying/storing Pokémon data in Cosmos DB.
from azure.cosmos import exceptions, CosmosClient, PartitionKey
from .secrets import secrets

client = CosmosClient(secrets["cosDB_Client_Auth"], credential = secrets["cosDB_Client_Cred"]) # Make a .secrets file to store these 

database = client.get_database_client("poke-db-id")
container = database.get_container_client("poke-ct-id")


def get_pokemon_by_query(query):
    SQL_query_items = "SELECT * FROM c WHERE 1=1 "
    params = []
    
    if 'name' in query:
        SQL_query_items += "AND c.name = @name"
        params.append({"name":"@name", "value":query['name']})
    
    if 'type' in query:
        SQL_query_items = "AND c.type = @type"
        params.append({"type":"@type", "value":query['type']})
    
    if 'pokedex_id' in query: 
        SQL_query_items = "AND c.pokedex_id = @pokedex_id"
        params.append({"pokedex_id": "@pokedex_id", "value":query['pokedex_id']})
    
    # Execute the query
    results = container.query_items(
        query=SQL_query_items,
        parameters=params,
        enable_cross_partition_query=True
    )
    return list(results)

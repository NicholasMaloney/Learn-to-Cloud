# Logic for uploading/retrieving Pokémon images in Blob Storage.
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from website.services import secrets

# Authenticat to Azure and access the Blob storage account. 
connection_string = secrets.Blob_cnct_str # Make a .secrets file to store these 
service = BlobServiceClient.from_connection_string(conn_str=connection_string) 
# Configure the Azure provider
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0.2"
    }
  }
}

#---------------------------------------------------------------#

# Configure Azure provider
provider "azurerm" {
  features {}
  subscription_id = "Enter-your-ID-here"
}

#create a resource group  / store all related resources for the project 
resource "azurerm_resource_group" "rg" {
  name     = "phase2-capstone"
  location = "australiaeast"
}

#---------------------------------------------------------------#

# create a cosmos db / holds movie data 
  # Cosmos DB Account
resource "azurerm_cosmosdb_account" "dba" {
  name = "cosmos-db-account"
  location = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  offer_type = "Standard"
  kind = "GlobalDocumentDB"

  consistency_policy {
    consistency_level = "Session"

  }

  geo_location {
    location = azurerm_resource_group.rg.location
    failover_priority = 0
  }

}
    # Cosmos DB SQL Database 
resource "azurerm_cosmosdb_sql_database" "db" {
  name                = "cosmos-sql-db"
  resource_group_name = azurerm_resource_group.rg.name
  account_name        = azurerm_cosmosdb_account.dba.name 
  
}
      # Cosmos DB Containers 
resource "azurerm_cosmosdb_sql_container" "dbc" {
  name = "cosmosdb-sql-container"
  resource_group_name = azurerm_resource_group.rg.name
  account_name = azurerm_cosmosdb_account.dba.name
  database_name = azurerm_cosmosdb_sql_database.db.name
  partition_key_paths = "/id" # You can this of this like a Primary key, its not the exact same 
  throughput = 400
}

          # Cosmos DB Items 

#---------------------------------------------------------------#

# create blog storage / hold pictures of movie cover art 
resource "azurerm_storage_account" "sa" {
  name                     = "phase2_storage_acct"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind = "BlobStorage"
}

resource "azurerm_storage_container" "sc" {
  name                  = "movieimages"
  storage_account_name   = azurerm_storage_account.sa.name
  container_access_type = "private"
}

resource "azurerm_storage_blob" "sb" {
  name                   = "phase2_movie_image_storage"
  storage_account_name   = azurerm_storage_account.sa.name
  storage_container_name = azurerm_storage_container.sc.name
  type                   = "Block"
  source                 = "some-local-file.zip"
}

#---------------------------------------------------------------#
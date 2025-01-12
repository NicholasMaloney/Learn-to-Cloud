# Phase 2: Programming
- In this phase, I'm learning Python programming with a focus on cloud technologies. I'll start by refreshing the basics like variables, functions, and data types, and gradually move to more advanced topics.
- Initially, my project aimed to develop a serverless movies API as requested in Phase 2 of the Learn to Cloud project. However, as I progressed, I decided to pivot and apply the same concept to create a Pokémon API. The current implementation is locally hosted and leverages Azure cloud services. I manually set up Cosmos DB NoSQL for efficient data storage and Blob storage for managing images. To interact with these services, I utilized Azure SDKs for Python, enabling seamless database queries. The API itself is built using Flask, a lightweight and flexible Python web framework.

# Pokémon API Web App

This project is a web application that allows users to search for Pokémon by name, type, or Pokédex ID and retrieve detailed data, including associated images. This project is built using Python, Flask, Azure Cosmos DB, and Azure Blob Storage.
- [Run The Web App](https://github.com/NicholasMaloney/Learn-to-Cloud/blob/b08a4bf091f6d51d61ef549f8cf85482e3fd2a3a/Phase-2-Programming/Capstone/Flask-web-app/main.py)
- [Flask Routes](https://github.com/NicholasMaloney/Learn-to-Cloud/blob/b08a4bf091f6d51d61ef549f8cf85482e3fd2a3a/Phase-2-Programming/Capstone/Flask-web-app/website/views.py)
- [HTML Tempaltes](https://github.com/NicholasMaloney/Learn-to-Cloud/tree/b08a4bf091f6d51d61ef549f8cf85482e3fd2a3a/Phase-2-Programming/Capstone/Flask-web-app/website/templates)
- [Query CosmosDB](https://github.com/NicholasMaloney/Learn-to-Cloud/blob/b08a4bf091f6d51d61ef549f8cf85482e3fd2a3a/Phase-2-Programming/Capstone/Flask-web-app/website/services/DBcosmos.py)


## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Architecture](#project-architecture)
- [Detailed Flow](#detailed-flow)
- [Key Components](#key-components)
	- [Frontend](#frontend)
	- [Backend](#backend)
	- [Database](#database)
	- [Data Handling](#data-handling)
- [Challenges Overcome](#challenges-overcome)


## Features
- Search Pokémon by:
  - Name (case-insensitive)
  - Type (e.g., "Fire", "Water")
  - Pokédex ID
- Retrieve detailed Pokémon data, including:
  - Name
  - Type(s)
  - Pokédex ID
  - Image URL
- Display Pokémon images fetched from Azure Blob Storage.
- Direct Cosmos DB integration using the Python SDK for data retrieval.


## Technologies Used
- **Frontend:** HTML, CSS
- **Backend:** Python, Flask
- **Database:** Azure Cosmos DB (NoSQL)
- **Storage:** Azure Blob Storage (for Pokémon images)
- **Integration:** Python SDK for Cosmos DB and Blob Storage

### Environment Setup 
- Installed the following Azure SDKs for python 
    - azure-mgmt-resource
    - azure-cosmos
    - azure-storage-blob
    - azure-identity
- Configured the following resources 
    - Resource group 
    - Cosmos DB account 
        - Cosmos DB SQL dataase 
        - Cosmos DB container 
    - Storage account 
        - Storage container 
        - Blob storage 


## Project Architecture
- User Request -> Flask Web App -> Cosmos DB & Blob Storage (via Python SDK) -> Response with Data & Image

### Detailed Flow
1. Users interact via the front-end web app.
2. Flask handles user input and routes requests to appropriate endpoints.
3. The Python SDK queries Cosmos DB for Pokémon data and fetches images from Blob Storage.
4. The web app renders data and displays the appropriate Pokémon image.


## Key Components

### Frontend
- `base.html`: Base template with common structure
- `home.html`: Homepage with search form
- `poke_result.html`: Displays search results

### Backend
- `main.py`: Entry point of the application
- `views.py`: Contains route handlers and business logic
- `DBcosmos.py`: Handles interactions with Cosmos DB

### Database
- Stores Pokémon data in a structured format
- Allows for efficient querying based on various parameters

### Data Handling
- Proper error handling for invalid inputs or no search results
- Efficient querying using Cosmos DB's SQL API


## Challenges Overcome
- Implemented case-insensitive search for Pokémon names
- Resolved issues with querying array fields (Pokémon types) in Cosmos DB
- Handled type conversion for Pokédex ID to ensure proper integer comparison

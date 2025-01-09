## Directory Structure
Flask-pokemon-app/
    website/
        static/                # For CSS, JavaScript, images, etc.
        templates/             # HTML templates for rendering (if needed).
        services/              # Azure service integrations (e.g., Cosmos DB, Blob Storage).
            __init__.py        # Make this a package.
            cosmos_service.py  # Logic for querying/storing Pokémon data in Cosmos DB.
            blob_service.py    # Logic for uploading/retrieving Pokémon images in Blob Storage.
        __init__.py            # Initializes the Flask app and extensions.
        auth.py                # Authentication logic (if any).
        models.py              # Database models for Pokémon data (optional, for SQLAlchemy or ORM).
        views.py               # API route handlers for the web app.
    azure_functions/           # Directory for Azure Function scripts (optional if managing locally).
        pokemon_api.py         # Azure Function for Pokémon API logic.
    main.py                    # Entry point for running the Flask app.
    config.py                  # Configuration settings for the app (e.g., Azure keys, Flask config).
    requirements.txt           # Python dependencies for your project.
    README.md                  # Project overview and setup instructions.

### Notes
- To run the web app run main.py
- All webpages that users can navigate too are defined in views.py 
- '__init__.py' stores the routes and views and initilises Flask
- The tutorial I am following to learn uses Bootstrap as a CSS framework which allows for styling 
- Make a search bar on home.html, where users can search for pokemon based on 
    - name 
    - type 
    - pokedex ID

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

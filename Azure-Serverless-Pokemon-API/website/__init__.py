# Initializes the Flask app and extensions.
from flask import Flask 

def create_app(): 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app 
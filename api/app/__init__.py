from flask import Flask, request, jsonify
from flask_cors import CORS
from config import config
from flask_language import Language, current_language
# from flask_mongoalchemy import MongoAlchemy
from pymongo import MongoClient

lang = Language()
uri = "mongodb://mongodb:27017"
client = MongoClient(uri)
db = client.dschang_db
# db2 = client.sante_bd
# db3 = client.logment_bd




# db = MongoAlchemy()
def create_app(environment):
   # flask initialisation
    app = Flask(
        __name__, static_folder='./static', template_folder='./templates')
    # Init flask configurations.
    app.config.from_object(config[environment])
    config[environment].init_app(app)
    # Enabling the cross origin using the cors.
    CORS(app,resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

    #Flask Language initialisation
    with app.app_context():
        lang.init_app(app)

    #Database initialisation
    # with app.app_context():
    #     db.init_app(app)

    # testing
    # user = {
    #     'name': 'kenne',
    #     'email': 'kenneboston1@gmail.com',
    #     'password': 'kenne'
    # }

    # db.users.insert_one(user)

    @lang.allowed_languages
    def get_allowed_languages():
        return ['en', 'fr']

    @lang.default_language
    def get_default_language():
        return 'en'


    # Route de base
    from .public import public_blueprint
    app.register_blueprint(public_blueprint)


    # Importing and registring namespaces
    from .api_logement.v1 import logement
    from .api_auth.v1 import auth
    from .api_sante.v1 import sante
    app.register_blueprint(auth)
    app.register_blueprint(sante)
    app.register_blueprint(logement)



    # @app.route("/")
    # def hello():
    #     return "Hello World!"

    # Return app
    return app

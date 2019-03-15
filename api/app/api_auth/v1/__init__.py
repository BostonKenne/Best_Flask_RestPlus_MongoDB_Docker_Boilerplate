from flask import (Blueprint)
from flask_restplus import Api, apidoc
from app import CORS


# Blueprint initialisation
auth = Blueprint('auth', __name__, url_prefix='/api/auth')

# Init Cors on blueprint
CORS(auth)

# Authorization dictionary
authorizations = {
    'apikey': {
        'in': 'header',
        'type': 'apiKey',
        'name': 'x-access-token',
    }
}


description = ''' API AUTHENTIFICATION ET GESTION DES UTILISATEURS  '''
# Init api.
api = Api(
    auth, title='USER MANAGMENT API',
    authorizations=authorizations, description=description,
    version='1.0', doc='/authentication/', default='authentication',
    default_label='authentication namespace.')

# Importing the namespaces.

from .namespaces.namespace_language import lang_api
from .namespaces.namespace_authentication import auth_api
from .namespaces.namespace_user import user_api
api.add_namespace(lang_api)
api.add_namespace(auth_api)
api.add_namespace(user_api)

@api.documentation
def swagger_ui():
    return apidoc.ui_for(api)



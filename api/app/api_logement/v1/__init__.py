from flask import (Blueprint)
from flask_restplus import Api, apidoc
from app import CORS


# Blueprint initialisation
logement = Blueprint('logement', __name__, url_prefix='/api/v1')

# Init Cors on blueprint
CORS(logement)

# Authorization dictionary
authorizations = {
    'apikey': {
        'in': 'header',
        'type': 'apiKey',
        'name': 'x-access-token',
    }
}


description = '''
This is <b>FIND HOUSING IN DSCHANG'S</b> REST API. All request in regards to the application can be found here,
in general most of the methods require you being as an active user to be able to access.
'''
# Init api.
api = Api(
    logement, title='FIND HOUSING API',
    authorizations=authorizations, description=description,
    version='1.0', doc='/logement/', default='authentication',
    default_label='authentication namespace.')

# Importing the namespaces.

# from .namespaces.globals.namespace_migration import migration_api
# from .namespaces.globals.namespace_authentication import authentication_api
# from .namespaces.globals.namespace_user import user_api
# from .namespaces.globals.namespace_communication import communication_api
# from .namespaces.globals.namespace_customer import customer_api
# from .namespaces.globals.namespace_supplier import supplier_api

@api.documentation
def swagger_ui():
    return apidoc.ui_for(api)

# api.add_namespace(migration_api)
# api.add_namespace(authentication_api)
# api.add_namespace(user_api)
# api.add_namespace(communication_api)
# api.add_namespace(customer_api)
# api.add_namespace(supplier_api)
# Registering namespaces to the api.

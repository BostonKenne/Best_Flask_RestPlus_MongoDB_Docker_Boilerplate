from flask import (Blueprint)
from flask_restplus import Api, apidoc
from app import CORS


# Blueprint initialisation
sante = Blueprint('sante', __name__, url_prefix='/api')

# Init Cors on blueprint
CORS(sante)

# Authorization dictionary
authorizations = {
    'apikey': {
        'in': 'header',
        'type': 'apiKey',
        'name': 'x-access-token',
    }
}


description = ''' API SANTÉ -dschang Connecté '''
# Init api.
api = Api(
    sante, title='API SANTÉ',
    authorizations=authorizations, description=description,
    version='1.0', doc='/sante/', default='authentication',
    default_label='authentication namespace.')

@api.documentation
def swagger_ui():
    return apidoc.ui_for(api)
# Lib imports
from flask import Blueprint
from .views.index import indexViews

# Init blueprint
public_blueprint = Blueprint('public_blueprint', __name__, url_prefix='/')


# Register views to blueprint
indexViews.register(public_blueprint)

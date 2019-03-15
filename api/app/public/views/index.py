# Libs and App imports
from flask_classy import FlaskView, route
from flask import render_template


# Object for global views
class indexViews(FlaskView):
    # Base route path.
    route_base = '/'

    @route("/")
    def home_page(self):
        return render_template('index.html')

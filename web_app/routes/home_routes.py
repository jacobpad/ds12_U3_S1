# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

# Make the rout
@home_routes.route("/") # HOME PAGE

# Define a function
def hello():
    print("VISITED THE HOME PAGE") # A log for the server (terminal)
    return "Hello World!"

# A second page
@home_routes.route("/about")

# Make a function that goes with the route "about"
def about():
    print("VISITED THE ABOUT PAGE") # A log for the server (terminal)
    return "About me"
    # return render_template('about.html')

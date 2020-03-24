 # web_app/__init__.py

##  RUN THIS CODE IN MAC WITH  ##
##  FLASK_APP=web_app flask run  ##

from flask import Flask, render_template

from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
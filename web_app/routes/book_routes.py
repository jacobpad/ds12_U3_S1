# web_app/routes/book_routes.py

from flask import Blueprint, jsonify

book_routes = Blueprint("book_routes", __name__)

# Make the rout & Define a function
@book_routes.route("/books.json") # HOME PAGE
def books():
    print("VISITED THE BOOKS PAGE") # A log for the server (terminal)
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
        {"id": 4, "title": "Book 4"},
        {"id": 5, "title": "Book 5"},
        {"id": 6, "title": "Book 6"},
    ]
    return jsonify(books)
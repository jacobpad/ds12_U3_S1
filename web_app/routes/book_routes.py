# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, render_template, request

book_routes = Blueprint("book_routes", __name__)

# Make the rout & Define a function
@book_routes.route("/books.json") # BOOKS.JSON PAGE
def list_books():
    print("VISITED THE BOOKS.JSON PAGE") # A log for the server (terminal)
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
        {"id": 4, "title": "Book 4"},
        {"id": 5, "title": "Book 5"},
        {"id": 6, "title": "Book 6"},
    ]
    return jsonify(books)

# Make the rout & Define a function
@book_routes.route("/books") # BOOKS PAGE
def books():
    print("VISITED THE BOOKS.JSON PAGE") # A log for the server (terminal)
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
        {"id": 4, "title": "Book 4"},
        {"id": 5, "title": "Book 5"},
        {"id": 6, "title": "Book 6"},
    ]
    return render_template("books.html", books=books) # Pass the books var to the page

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    return jsonify({
        "message": "BOOK CREATED OK (TODO)",
        "book": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")

# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, render_template, request, redirect

from web_app.models import db, Book #, parse_records

book_routes = Blueprint("book_routes", __name__)

# Make the rout & Define a function
@book_routes.route("/books.json") # BOOKS.JSON PAGE
def list_books():
    print("VISITED THE BOOKS.JSON PAGE") # A log for the server (terminal)
    # books = [
    #     {"id": 1, "title": "Book 1"},
    #     {"id": 2, "title": "Book 2"},
    #     {"id": 3, "title": "Book 3"},
    #     {"id": 4, "title": "Book 4"},
    #     {"id": 5, "title": "Book 5"},
    #     {"id": 6, "title": "Book 6"},
    # ]
    book_records = Book.query.all()
    return jsonify(book_records)

# Make the rout & Define a function
@book_routes.route("/books") # BOOKS PAGE
def books():
    print("VISITED THE BOOKS.JSON PAGE") # A log for the server (terminal)
    # books = [
        # {"id": 1, "title": "Book 1"},
        # {"id": 2, "title": "Book 2"},
        # {"id": 3, "title": "Book 3"},
        # {"id": 4, "title": "Book 4"},
        # {"id": 5, "title": "Book 5"},
        # {"id": 6, "title": "Book 6"},
    # ]
    book_records = Book.query.all()
    print(book_records)

    return render_template("books.html", books=book_records) # Pass the books var to the page

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))
    # # todo: store in database
    # return jsonify({
    #     "message": "BOOK CREATED OK (TODO)",
    #     "book": dict(request.form)
    # })
    new_book = Book(title=request.form["title"], author_id=request.form["author_name"])
    print(new_book)
    db.session.add(new_book)
    db.session.commit()

    #flash(f"Book '{new_book.title}' created successfully!", "success")
    return redirect(f"/books")
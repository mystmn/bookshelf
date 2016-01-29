from flask import Blueprint, render_template, current_app, request
from bookshelf.data.models import Book

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template("index.htm")


@main.route('books/')
def display_books():
    books = [book for book in Book.query.all()]

    return render_template("books.htm", books=books)


@main.route('books/<id>', methods=['GET', 'POST'])
def id_books(id):
    if request.method == 'GET':
        data = Book.query.filter_by(id=id).first()

        return render_template("book.html", data=data)
    elif request.method == "POST":
        books = [book for book in Book.query.all()]
    else:
        pass

    return render_template("books.htm", books=books)

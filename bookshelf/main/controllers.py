from flask import Blueprint, render_template, current_app, request, redirect, url_for
import random
from bookshelf.data.models import Book, db

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template("index.htm")


@main.route('books/')
def display_books():
    books = [book for book in Book.query.all()]

    return render_template("books.htm", books=books)


@main.route('books/<int:get_id>', methods=['GET', 'POST'])
def id_books(get_id):
    rand = hex(random.getrandbits(16))
    rand2 = hex(random.getrandbits(16))
    data = Book.query.filter_by(id=get_id).first()

    if request.method == "POST":
        data.title = request.form['title']
        db.session.commit()
        return redirect(url_for('.display_books'))

    elif request.method == 'GET':
        return render_template("book.html", data=data, rand=rand, rand2=rand2)

    else:
        return redirect('http://www.runnable.com', 301)
#    return render_template("books.htm", data=data)

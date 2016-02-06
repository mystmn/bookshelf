from flask import Blueprint, render_template, current_app, request, redirect, url_for
from bookshelf.data.models import Book, db
import random

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template("index.htm")


@main.route('books/', methods=['GET', 'POST'])
def display_books():
    if request.method == "POST":
        book_id = request.form['id']

        if request.form['delete'] == "true":
            Book.query.filter_by(id=book_id).delete()
            db.session.commit()
        else:
            pass
        return redirect(url_for(".display_books"))

    else:
        books = [book for book in Book.query.all()]
        return render_template("books.htm", books=books)


@main.route('books/<int:get_id>', methods=['GET', 'POST'])
def id_books(get_id):
    rand = hex(random.getrandbits(16))
    rand2 = hex(random.getrandbits(16))
    rand3 = hex(random.getrandbits(16))
    rand4 = hex(random.getrandbits(16))
    data = Book.query.filter_by(id=get_id).first()

    if request.method == "POST":
        data.title = request.form['title']
        data.rating = request.form['rank']
        data.description = request.form['desc']
        db.session.commit()
        return redirect(url_for('.display_books'))

    elif request.method == 'GET':
        return render_template("book.html", data=data, rand=rand, rand2=rand2, rand3=rand3, rand4=rand4)

    else:
        return redirect('http://www.runnable.com', 301)

# return render_template("books.htm", data=data)

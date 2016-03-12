from flask import Blueprint, render_template, request, redirect, url_for
from bookshelf.data.models import Book, db
import random

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template("index.htm")


@main.route('router/', methods=['GET', 'POST'])
def router(req=None):

    if request.method == "POST":

        if request.form['code'] == "1":  # Create item
            bN = request.form['book_name']
            bA = request.form['book_author']
            req = bN + "," + bA
            me = Book(bN, "0", "", bA)
            db.session.add(me)
            db.session.commit()

        elif request.form['code'] == "2":  # Delete item
            book_id = request.form['id']
            Book.query.filter_by(id=book_id).delete()
            db.session.commit()

        return redirect(url_for('.display_books'))
    else:
        req = "GET"

    return render_template("router.html", req=req)


@main.route('books/')
def display_books():
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

from bookshelf import app
from bookshelf.data.models import db, Book

def create_books(db):
    book1 = Book('Epic of the Forgotten', 5, 'Id recommend the book any day')

    db.session.add(book1)
    db.session.commit()

with app.app_context():
    db.drop_all()
    db.create_all()

    create_books(db)


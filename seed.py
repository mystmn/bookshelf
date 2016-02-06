from bookshelf import app
from bookshelf.data.models import db, Book

def create_books(db):
# id, title, rating, description, and producer
    book1 = Book('When Breath Becomes Air', 6, 'Well done', 'Paul Kalanithi')
    book2 = Book('First 100 Words', 8, 'Kinda Boring', 'Roger Priddy')
    book3 = Book('The First Team', 4, 'Would recommend', 'John Ball')
    book4 = Book('Black', 8, 'AA++', 'Ted Dekker')
    book5 = Book('Red', 8, 'Amazing', 'Ted Dekker')
    book6 = Book('White', 8, 'Blessing', 'Ted Dekker')
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.add(book4)
    db.session.add(book5)
    db.session.add(book6)
    db.session.commit()

with app.app_context():
#    db.drop_all()
    db.create_all()
    create_books(db)


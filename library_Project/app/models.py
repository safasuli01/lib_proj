from flask_sqlalchemy import   SQLAlchemy
from flask import url_for

db = SQLAlchemy()


class Book(db.Model):
    __tablename__ = 'books'
    id= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(100), nullable=False)
    c_photo= db.Column(db.String(100), nullable=False)
    p_no= db.Column(db.Integer)
    description= db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f'{self.title}'

    @property
    def image_url(self):
        return url_for('static', filename=f'images/{self.c_photo}')  # assuming the images are stored in a 'books/images' folder in static directory.  If not, adjust this accordingly.  Also, make sure to update the filename to match the actual filename stored in the database.   If the filename is stored in a different column, you'll need to modify this accordingly.   If the filename is stored

    @property
    def show_url(self):
        return url_for('books.show_book', id=self.id)

    @property
    def edit_url(self):
        return url_for('books.edit_book', id=self.id)

    @property
    def delete_url(self):
        return url_for('books.delete_book', id=self.id)
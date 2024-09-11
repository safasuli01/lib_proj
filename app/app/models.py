from flask_sqlalchemy import SQLAlchemy
from flask import url_for

db = SQLAlchemy()


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    c_photo = db.Column(db.String(300), nullable=False)
    p_no = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f"{self.title}"

    @property
    def image_url(self):
        return url_for(
            "static", filename=f"images/{self.c_photo}"
        )

    @property
    def show_url(self):
        return url_for("books.show", book_id=self.id)

    @property
    def edit_url(self):
        return url_for("books.edit", book_id=self.id)

    @property
    def delete_url(self):
        return url_for("books.delete", book_id=self.id)

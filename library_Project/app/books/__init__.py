from flask import Blueprint

book_blueprint = Blueprint ('books', __name__, '/books')

from app.books import views
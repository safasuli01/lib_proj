import os
from flask import Flask, render_template,redirect, request, url_for
from werkzeug.utils import secure_filename

from app.books import book_blueprint
from app.models import db, Book
from app.books.forms import BookForm

@book_blueprint.route(404)
def page_not_found(error):
    return render_template('error.html'), 404

@book_blueprint.route('/', endpoint='landpage', method=['GET'])
def landpage():
    books = Book.query.all()
    return render_template('books/landpage.html', books=books)

@book_blueprint.route('/create', endpoint='create', methods=['GET', 'POST'])
def create_book():
    form = BookForm()
    if form.validate_on_submit():
        c_photo = request.files['c_photo']
        image_name=secure_filename(c_photo.filename)
        c_photo.save(os.path.join('static/images/', image_name))
        book = Book(
            title=form.title.data,
            c_photo=image_name,
            p_no=form.p_no.data,
            description=form.description.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('show'))
    return render_template('books/create.html', form=form)

@book_blueprint.route('/<int:book_id>', endpoint='show', methods=['GET'])
def show_book(id):
    book = Book.query.get_or_404(id)
    return render_template('books/show.html', book=book)


@book_blueprint.route('/<int:book_id>/edit', endpoint='edit', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get_or_404(id)
    form = BookForm(obj=book)
    if form.validate_on_submit():
        book.title=form.title.data
        book.c_photo=form.c_photo.data
        book.p_no=form.p_no.data
        book.description=form.description.data
        if request.files['c_photo']:
            c_photo = request.files['c_photo']
            image_name=secure_filename(c_photo.filename)
            c_photo.save(os.path.join('static/images/', image_name))
            book.c_photo=image_name
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('books/edit.html', form=form, book=book)

@book_blueprint.route('/<int:book_id>/delete', endpoint='delete', methods=['POST'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))
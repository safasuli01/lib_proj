from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired, Length


class BookForm(FlaskForm):
    title = StringField("title", validators=[DataRequired(), Length(2, 200)])
    c_photo = FileField("Cover Photo", validators=[DataRequired()])
    p_no = IntegerField("Page Number")
    description = StringField("Description", validators=[DataRequired()])
    submit = SubmitField("Submit")

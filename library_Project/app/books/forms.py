from wtforms import StringField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm

class BookForm(FlaskForm):
    id = IntegerField('id')
    title = StringField('title', validators =[DataRequired(), Length(2,20)])
    c_photo = FileField('c_photo', validators =[DataRequired()])
    p_no = IntegerField('p_no')
    description = StringField('description', validators =[DataRequired])


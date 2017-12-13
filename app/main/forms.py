from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired


class CareerForm(FlaskForm):
	image = FileField('Career Image')
	name = StringField('Title', validators=[DataRequired(), Length(1, 64)])
	overview = TextAreaField('Overview', validators=[DataRequired()])

class CategoryForm(FlaskForm):
	name = StringField('Title', validators=[DataRequired(), Length(1, 64)])
	overview = TextAreaField('Overview', validators=[DataRequired()])
	submit = SubmitField('Create')

class CommentForm(FlaskForm):
	content = StringField('Add Comment', validators=[DataRequired()])
	submit = SubmitField('Add Comment')


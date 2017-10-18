from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User, Career, Category, Comment

class CareerForm(FlaskForm):
	name = StringField('Title', validators=[DataRequired(), Length(1, 64)])
	overview = TextAreaField('Overview', validators=[DataRequired()])
	submit = SubmitField('Create')

class CategoryForm(FlaskForm):
	name = StringField('Title', validators=[DataRequired(), Length(1, 64)])
	overview = TextAreaField('Overview', validators=[DataRequired()])
	submit = SubmitField('Create')

class CommentForm(FlaskForm):
	content = StringField('Add Comment', validators=[DataRequired()])
	submit = SubmitField('Comment')


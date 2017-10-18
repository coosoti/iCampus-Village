from . import main
from flask import Flask, render_template, redirect, url_for
from .forms import CareerForm, CategoryForm, CommentForm
from ..models import Category, Career, Permission, User, Comment
from flask_login import current_user
from app import db

@main.route('/')
@main.route('/category/<int:id>')
def home(id=None):
    categories = Category.query.all()
    careers = Career.query.all()
    category = Category.query.filter_by(id=id).first()
    if category:
       careers = category.careers
    return render_template('index.html', category=category, careers=careers, categories=categories)

@main.route('/career/<int:id>', methods=['GET', 'POST'])
def career_detail(id):
    form = CommentForm()
    career = Career.query.filter_by(id=id).first()
    comments = career.comments

    if form.validate_on_submit():
        new_comment =Comment(content=form.content.data,
                   owner=current_user.username)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('career_detail'))                 
    return render_template('career_detail.html', career=career, comments=comments, form=form)    

@main.route('/about')
def about():
    return render_template('about.html')

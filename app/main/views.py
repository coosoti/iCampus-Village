from . import main
from flask import Flask, render_template, redirect, url_for
from .forms import CareerForm, CategoryForm
from ..models import Category, Career, Permission, User
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

# @main.route('/category/<int:id>')
# def career_list_by_category(id):
#     category = Category.query.filter_by(id=id).first()
#     if category:
#         data = category.careers
#     return render_template('index.html', data=data, category=category)    

@main.route('/about')
def about():
    return render_template('about.html')

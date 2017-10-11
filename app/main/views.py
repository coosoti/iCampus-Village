from . import main
from flask import Flask, render_template, redirect, url_for
from .forms import CareerForm, CategoryForm
from ..models import Category, Career, Permission, User
from flask_login import current_user
from app import db

@main.route('/')
def home():
    careers = Career.query.all()
    return render_template('index.html', careers=careers)

# @main.route('/create_category', methods=['GET', 'POST'])
# def create_category():
#     form = CategoryForm()
#     if form.validate_on_submit():
#         category = Category(name=form.name.data,
#                             overview = form.overview.data)
#         db.session.add(category)
#         print(category)
#         return redirect(url_for('.home'))
#     return render_template('home.html', form=form)                        

# @main.route('/create_career', methods=['GET', 'POST'])
# def create_career():
#     form = CareerForm()
#     if form.validate_on_submit():
#         career = Career(name=form.name.data,
#                             overview = form.overview.data)
#         db.session.add(career)
#         print(career)
#         return redirect(url_for('.home'))
#     return render_template('home.html', form=form)

@main.route('/about')
def about():
    return render_template('about.html')

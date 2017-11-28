from . import main
from flask import Flask, render_template, redirect, url_for, flash
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

# CRUD functionalities for categories models
@main.route('/cms/', methods=['GET', 'POST'])
def cms():
    categories = Category.query.all()
    return render_template('cms.html', categories=categories)

# Retrieve each categy on CMS  
@main.route('/cms/cat/<int:id>')
def ret_cat(id):
    category = Category.query.filter_by(id=id).first()
    return render_template('cms_cat_detail.html', category=category)

# Create Category in CMS
@main.route('/cms/create_cat', methods=['GET', 'POST'])
def create_category():
    form = CategoryForm()
    if current_user.can(Permission.WRITE) and form.validate_on_submit():
        # print(current_user.username)
        new_category = Category(name=form.name.data, overview=form.overview.data)
        db.session.add(new_category)
        return redirect(url_for('main.cms'))
    print(current_user.role.permissions)    
    return render_template('create_cat.html', form=form)     

# Edit Category CMS
@main.route('/cms/edit_cat/<int:id>', methods=['GET', 'POST'])
def edit_cat(id):
    category = Category.query.get_or_404(id)
    if not current_user.can(Permission.WRITE):
        abort(403)
    form = CategoryForm()
    if form.validate_on_submit():
        category.name = form.name.data
        category.overview = form.overview.data
        db.session.add(category)
        flash('The category has been updated')
        return redirect(url_for('main.cms'))
    form.name.data = category.name
    form.overview.data = category.overview
    return render_template('edit_cat.html', form=form, category=category)    

# Delete Category in CMS
@main.route('/cms/<int:id>/delete', methods=['GET', 'POST'])
def delete_cat(id):
    category = Category.query.get_or_404(id)
    if not current_user.can(Permission.WRITE):
        abort(403)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('main.cms'))


# Create Career in CMS
@main.route('/cms/create_career', methods=['GET', 'POST'])
def create_career():
    form = CareerForm()
    if current_user.can(Permission.WRITE) and form.validate_on_submit():
        # print(current_user.username)
        new_career = Career(name=form.name.data, overview=form.overview.data)
        db.session.add(new_career)
        return redirect(url_for('main.all_careers'))
    print(current_user.role.permissions)    
    return render_template('create_career.html', form=form)     


# Retrieve all careers in CMS
@main.route('/cms/all-careers/')  
def all_careers():
    careers = Career.query.all()
    return render_template('cms_all_careers.html', careers=careers)

# Retrieve one career for editing or updating
@main.route('/cms/careers/<int:id>')
def ret_career(id):
    career = Career.query.filter_by(id=id).first()
    return render_template('cms_career_detail.html', career=career)

# Edit Career in CMS
@main.route('/cms/edit_career/<int:id>', methods=['GET', 'POST'])
def edit_career(id):
    career = Career.query.get_or_404(id)
    if not current_user.can(Permission.WRITE):
        abort(403)
    form = CareerForm()
    if form.validate_on_submit():
        career.name = form.name.data
        career.overview = form.overview.data
        db.session.add(career)
        flash('The career has been updated')
        return redirect(url_for('main.all_careers'))
    form.name.data = career.name
    form.overview.data = career.overview
    return render_template('edit_career.html', form=form, career=career)

# Delete Category in CMS
@main.route('/cms/career/<int:id>/delete', methods=['GET', 'POST'])
def delete_career(id):
    career = Career.query.get_or_404(id)
    if not current_user.can(Permission.WRITE):
        abort(403)
    db.session.delete(career)
    db.session.commit()
    return redirect(url_for('main.all_careers'))

@main.route('/career/<int:id>', methods=['GET', 'POST'])
def career_detail(id):
    form = CommentForm()
    career = Career.query.filter_by(id=id).first()
    comments = career.comments

    if form.validate_on_submit():
        new_comment =Comment(content=form.content.data,
                             career=career,
                             owner=current_user._get_current_object())
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.career_detail', id=career.id))                 
    return render_template('career_detail.html', career=career, comments=comments, form=form)    

@main.route('/about')
def about():
    return render_template('about.html')

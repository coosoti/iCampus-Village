from . import main
from flask import Flask, render_template

@main.route('/')
def home():
	return render_template('home.html')

@main.route('/about')
def about():
	return render_template('about.html')

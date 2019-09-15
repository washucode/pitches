from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required

@main.route('/')
def index():
    render_template('index.html')

@main.route('/interview')
def interview():
    render_template('interview.html')

@main.route('/promotion')
def promotion():
    render_template('promotion.html')

@main.route('/product')
def product():
    render_template('product.html')
@main.route('/pickup')
def pickup():
    render_template('pickup.html')






from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/interview')
def interview():
    return render_template('interview.html')

@main.route('/promotion')
def promotion():
    return render_template('promotion.html')

@main.route('/product')
def product():
    return render_template('product.html')
@main.route('/pickup')
def pickup():
    return render_template('pickup.html')






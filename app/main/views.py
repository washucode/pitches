from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required

@main.index('/')
def index():
    render_template('index.html')

@main.interview('/interview')
def interview():
    render_template('interview.html')

@main.promotion('/promotion')
def promotion():
    render_template('promotion.html')

@main.product('/product')
def product():
    render_template('product.html')
@main.pickup('/pickup')
def pickup():
    render_template('pickup.html')






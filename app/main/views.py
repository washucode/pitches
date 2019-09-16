from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required

@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
 
    general = Pitch.query.all()
    product = Pitch.query.filter_by(category = 'Product Pitch').all()
    pickup = Pitch.query.filter_by(category = 'Pickup Lines').all()
    interview= Pitch.query.filter_by(category = 'Interview Pitch').all()
    promotion = Pitch.query.filter_by(category = 'Promotion Pitch').all()
    return render_template('index.html',general=general,product=product,pickup=pickup,interview=interview,promotion=promotion)

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






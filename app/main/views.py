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

@main.route('/new_pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = Pitch_Form()    

    if pitch_form.validate_on_submit():
        pitch = Pitch(title = pitch_form.title.data, category = pitch_form.category.data, content = pitch_form.pitch_content.data, author = pitch_form.author.data)

        pitch.save_pitch()
        
        return redirect(url_for('main.index'))
    
    return render_template('new_pitch.html', form = form)  









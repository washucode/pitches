from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required
from ..models import User,Pitch
from .forms import Pitch_Form, Update_Profile
from .. import db,photos

@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
 
    
    
    return render_template('index.html')
@main.route('/all_pitches')
def all_pitches():
    general = Pitch.query.all()
    return render_template('all_pitches.html',general=general)


@main.route('/interview')
def interview():
    interview= Pitch.query.filter_by(category = 'Interview Pitch').all()
    return render_template('interview.html',interview=interview)

@main.route('/promotion')
def promotion():
    promotion = Pitch.query.filter_by(category = 'Promotion Pitch').all()
    return render_template('promotion.html',promotion=promotion)

@main.route('/product')
def product():
    product = Pitch.query.filter_by(category = 'Product Pitch').all()
    return render_template('product.html',product=product)
@main.route('/pickup')
def pickup():
    pickup = Pitch.query.filter_by(category = 'Pickup Lines').all()
    return render_template('pickup.html', pickup=pickup)

@main.route('/new_pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = Pitch_Form()    

    if form.validate_on_submit():
        pitch = Pitch(title = form.title.data, category =form.category.data, content = form.content.data, author = form.author.data)

        pitch.save_pitch()
        
        return redirect(url_for('main.all_pitches'))
    
    return render_template('new_pitch.html', pitch_form = form)  

@main.route('/<username>')
@login_required
def profile(username):
    pitch = Pitch.query.filter_by(user_id= current_user.id).all()
    user = User.query.filter_by(username = username).first()
    if user == None:
        abort(404)
    
    return render_template('profile.html', user = user)
    
@main.route('/<username>/update/pic', methods = ['POST'])
@login_required
def update_profile_pic(username):
    user = User.query.filter_by(username = username).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_img = path
        db.session.commit()

    return redirect(url_for('main.profile', username = username))

@main.route('/user/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = Update_Profile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',username=user.username))

    return render_template('update_profile.html',form =form)

@main.route('/comments/<int:pitch_id>/comment',methods=['POST','GET'])
@login_required
def comment(pitch_id):

    form = CommentsForm()    
    current_pitch = Pitch.query.filter_by(id = pitch_id).first()
    if form.validate_on_submit():
        comment = Comment(comment = form.comment.data,user = current_user,pitch = current_pitch)
        db.session.add(new_comment)
        db.session.commit()
        
        
        return redirect(url_for('main.all_pitches'))
    
    return render_template('comments.html', comment_form = form)  
  
   
   






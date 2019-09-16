from flask import render_template,redirect,url_for,flash,request
from . import auth
from flask_login import login_user,logout_user,login_required
from .forms import LoginForm,SignUpForm
from ..models import User,Pitch

@auth.route('/signup',methods=['GET','POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user =  User(email = form.email.data, username = form.username.data,password = form.password.data)
        
        user.save_user()

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('sign_up.html',signup_form = form)


@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        else:
            flash('Invalid username or Password')


    return render_template('login.html',login_form = form)

@auth.route('/logout')
@login_required
def signout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for("main.index"))

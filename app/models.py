from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key= True)
    username = db.Column(db.String(255),nullable=False, unique=True)
    email = db.Column(db.String(20), nullable =False,unique=True)
    bio = db.Column(db.String(255))
    profile_img = db.Column(db.String(20),nullable =False,default='default.jpg')
    password = db.Column(db.String(60),nullable = False)
    pitches = db.relationship('Pitch', backref = 'user', lazy = 'dynamic')
    comments = db.relationship('Comment', backref = 'user', lazy = 'dynamic')

    def save_user(self):
        db.session.add(self)
        db.session.commit()
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read the password atrribute')
    
    @password.setter
    def password(self, password):
        password_hash = generate_password_hash(password)
        self.password = password_hash


    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(20))
    pitch_content = db.Column(db.String)
    category = db.Column(db.String(20))
    author = db.Column(db.String(20))
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)        
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')
    def save_comment(self):
        db.session.add(self)
        db.session.commit()


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)    
    body = db.Column(db.String)          
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
        
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


    
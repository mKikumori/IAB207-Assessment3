from datetime import datetime
from flask_login import UserMixin
from . import db

class MusicShow(db.Model):
    __tablename__ = 'music_shows'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    description = db.Column(db.String(250))
    image = db.Column(db.String(400))
    genre = db.Column(db.String(20))

    comments = db.relationship('Comment', backref='musicShow')

    def __repr__(self):
        return f"Name: {self.name}"
    
    
class User(db.Model):
    __tablename__ = 'users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	# password should never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long, depending on your hashing algorithm
    password_hash = db.Column(db.String(255), nullable=False)
    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')
    
    # string print method
    def __repr__(self):
        return f"Name: {self.name}"
    

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    # add the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    music_show_id = db.Column(db.Integer, db.ForeignKey('music_shows.id'))

    # string print method
    def __repr__(self):
        return f"Comment: {self.text}"

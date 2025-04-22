from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
from faker import Faker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
fake = Faker()

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    join_date = db.Column(db.DateTime, nullable=False)
    bio = db.Column(db.Text, default="No bio provided.")
    reputation = db.Column(db.String(20), default="Neutral")
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    posts = db.relationship('Post', backref='category', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String(20), nullable=False)  # buyer or seller
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

# Routes
@app.route('/')
def index():
    posts = Post.query.order_by(Post.date.desc()).limit(10).all()
    members = User.query.order_by(User.join_date.desc()).limit(10).all()
    return render_template('index.html', posts=posts, members=members)

@app.route('/marketplace')
def marketplace():
    buyer_posts = Post.query.filter_by(type='buyer').order_by(Post.date.desc()).limit(10).all()
    seller_posts = Post.query.filter_by(type='seller').order_by(Post.date.desc()).limit(10).all()
    return render_template('marketplace.html', buyer_posts=buyer_posts, seller_posts=seller_posts)

@app.route('/marketplace/buyers')
def buyers():
    posts = Post.query.filter_by(type='buyer').order_by(Post.date.desc()).all()
    return render_template('buyers.html', posts=posts)

@app.route('/marketplace/sellers')
def sellers():
    posts = Post.query.filter_by(type='seller').order_by(Post.date.desc()).all()
    return render_template('sellers.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)
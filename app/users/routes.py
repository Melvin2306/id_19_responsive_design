from flask import Blueprint, redirect, render_template, url_for, request, current_app
from .models import User, Company
from app.users.services.create_user import create_user
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from app.users.services.create_user import create_user
from app.users.models import User


blueprint = Blueprint('users', __name__)

### root ### 
@blueprint.route('/<user_id>')
@login_required
def user(user_id):
    return render_template('/users/user.html', user_id=user_id)


### signup ###
@blueprint.get('/signup')
def get_signup():
    return render_template("users/signup.html")

@blueprint.post('/signup')
def post_signup():
    try:
        if User.query.filter_by(user_email=request.form.get('email')).first():
            raise Exception ('Email already taken.')
        elif request.form.get('password') != request.form.get('password_confirmation'):
            raise Exception('Passwords do not match.')
        
        user = create_user(request.form)
        login_user(user)
        return redirect(url_for('users.user', user_id=user.id))
    
    except Exception as error_message:
        error = error_message or 'An error occurred while creating a user. Please make sure to enter valid data.'
        return render_template('users/signup.html', error=error)

@blueprint.route('/sign-up')
@blueprint.route('/anmeldung')
@blueprint.route('/registration')
def redirect_signup():
    return redirect(url_for('users.get_signup'))



### login ###
@blueprint.get('/login')
def get_login():
    return render_template("users/login.html")

@blueprint.post('/login')
def post_login():
    try:
        user = User.query.filter_by(user_email=request.form.get('email')).first()
        if not user:
            raise Exception('Email address not found.')
        elif check_password_hash(request.form.get('password'), user.password):
            raise Exception('Incorrect Password.')
        
        login_user(user)
        return redirect(url_for('users.user', user_id=user.id))
    
    except Exception as error_message:
        error = error_message or 'An error occurred while logging in. Please verify your email and password.'
        return render_template('users/login.html', error=error)


### logout ###
@blueprint.get('/logout')
def get_logout():
    logout_user()
    return redirect(url_for('users.get_login'))
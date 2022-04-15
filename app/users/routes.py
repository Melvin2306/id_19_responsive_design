from flask import Blueprint, redirect, render_template, url_for, request, current_app
from .models import User, Company
from app.users.services.create_user import create_user
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

blueprint = Blueprint('users', __name__)

### root ### 
@blueprint.route('/<user_id>')
def user(user_id):
    return render_template('/users/user.html', user_id=user_id)

@blueprint.get('/login')
def get_login():
    return render_template("users/login.html")

@blueprint.post('/login')
def post_login():
    try:
        user = User.query.filter_by(email=request.form.get('email')).first()
        if not user:
            raise Exception('Email address not found.')
        elif check_password_hash(request.form.get('password'), user.password):
            raise Exception('Incorrect Password.')
        
        login_user(user)
        return redirect(url_for('simple_pages.about'))
    
    except Exception as error_message:
        error = error_message or 'An error occurred while logging in. Please verify your email and password.'
        return render_template('users/login.html', error=error)

@blueprint.route('/signup')
def get_signup():
    return render_template('/users/signup.html')
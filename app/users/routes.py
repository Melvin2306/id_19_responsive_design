from flask import Blueprint, redirect, render_template, url_for, request, current_app

blueprint = Blueprint('simple_pages', __name__)

### root ### 
@blueprint.route('/<user_id>')
def user(user_id):
    return render_template('/users/user.html', user_id=user_id)


from flask import Blueprint, redirect, render_template, url_for, request, current_app

blueprint = Blueprint('simple_pages', __name__)

### root ### 
@blueprint.route('/')
def root():
    return render_template('simple_pages/root.html')

@blueprint.route('/home')
@blueprint.route('/start')
@blueprint.route('/landingpage')
@blueprint.route('/landing')
def redirect_root():
    return redirect(url_for(root))



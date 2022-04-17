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

###linking pages and redirecting###
#about
@blueprint.route('/about')
def about():
    return render_template('simple_pages/about.html')

@blueprint.route('/about-me')
@blueprint.route('/about-page')
@blueprint.route('/info')
@blueprint.route('/information')
def redirect_about():
    return redirect(url_for(about))

#imprint
@blueprint.route('/imprint')
def imprint():
    return render_template('simple_pages/imprint.html')

@blueprint.route('/impressum')
@blueprint.route('/legal')
@blueprint.route('/legal-info')
def redirect_imprint():
    return redirect(url_for(imprint))


#FAQ
@blueprint.route('/faq')
def faq():
    return render_template('simple_pages/faq.html')

@blueprint.route('/f-a-q')
@blueprint.route('/frequentlyaskedquestions')
@blueprint.route('/frequently-asked-questions')
def redirect_faq():
    return redirect(url_for(faq))

@blueprint.route('/how_it_works')
def how_it_works():
    return render_template('simple_pages/how_it_works.html')


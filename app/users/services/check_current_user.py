from flask_login import login_user, logout_user, current_user, login_required

def check_current_user(user):

    if user.id == current_user.id:
        return True
    else:
        return False

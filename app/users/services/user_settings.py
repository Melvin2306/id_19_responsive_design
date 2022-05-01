from app.users.models import User

def user_settings(form_data, user):

    if form_data.get('user_email'):
        user.user_email=form_data.get('user_email').lower()

    if form_data.get('first_name'):
        user.first_name=form_data.get('first_name').capitalize()

    if form_data.get('last_name'):
        user.last_name=form_data.get('last_name').capitalize()

    if form_data.get('street_name'):
        user.street_name=form_data.get('street_name').capitalize()

    if form_data.get('zip_code'):
        user.zip_code=form_data.get('zip_code')

    if form_data.get('town'):
        user.town=form_data.get('town').capitalize()

    if form_data.get('country'):
        user.country=form_data.get('country').capitalize()

    user.save()
    
    return user
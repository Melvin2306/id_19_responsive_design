from app.users.models import User

def user_settings(form_data, user):

    if form_data.get('user_email'):
        user.email=form_data.get('user_name')

    if form_data.get('user_first_name'):
        user.first_name=form_data.get('user_first_name')

    if form_data.get('user_last_name'):
        user.last_name=form_data.get('user_last_name')

    if form_data.get('user_street_name'):
        user.street_name=form_data.get('user_street_name')

    if form_data.get('user_phone_number'):
        user.zip_code=form_data.get('user_phone_number')

    if form_data.get('user_town'):
        user.town=form_data.get('user_town')

    if form_data.get('user_country'):
        user.country=form_data.get('user_country')

    user.save()
    
    return user
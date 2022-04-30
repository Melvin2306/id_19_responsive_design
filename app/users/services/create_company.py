from app.users.models import User, Company

def create_company(user_id):
    # create new company
    new_company = Company(
        user_id = user_id
    )
    new_company.save()
    
    return new_company
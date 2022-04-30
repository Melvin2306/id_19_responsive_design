from app.users.models import User, Company
from werkzeug.security import generate_password_hash, check_password_hash

def create_company(user_id):
    # Create new User 
    new_company = Company(
        user_id = user_id
    )
    new_company.save()
    
    return new_company
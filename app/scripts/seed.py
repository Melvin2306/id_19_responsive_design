from unicodedata import category
from app.app import create_app
from app.users.models import Company, User
from app.extensions.database import db

app = create_app()
app.app_context().push()

all_users_dict = {
    "Email": "melvin.rinkleff@gmx.de", 
    "First Name": "Melvin", 
    "Last Name": "Rinkleff",
    "Street": "Alfred-Jung-Straße", 
    "ZIP": 310715,
    "Town": "Berlin",
    "Country": "Germany",
}

all_accounts_dict = {
    "Sparkasse Hannover": {
        "Account": "Sparkasse Hannover", 
        "Category": "Banking", 
        "Contact Email": "info@sparkasse-hannover.de",
        "Contact Phone Number": 051130007070, 
        "Description": "primary banking account", 
        }
    "N26 Bank": {
        "Account": "N26", 
        "Category": "Banking", 
        "Contact Email": "support@n26.com",
        "Contact Phone Number": 030364286880, 
        "Description": "Second banking account", 
        }
    "Katapult Magazin": {
        "Account": "Katapult", 
        "Category": "Magazines", 
        "Contact Email": "redaktion@katapult-magazin.de",
        "Contact Phone Number": 017656998944, 
        "Description": "Yearly subscription magazines account", 
        }
}

for slug, user in all_users_dict.items():
    new_user = User(
        slug=slug,
        user_email=user["Email"], 
        first_name=user["First Name"], 
        last_name=user["Last Name"], 
        street_name=user["Street"], 
        zip_code=user["ZIP"],
        town=user["Town"],
        country=user["Country"],
        )
    db.session.add(new_user)

for slug, company in all_accounts_dict.items():
    new_company = Company(
        slug=slug,
        name=company["Account"], 
        category=company["Category"], 
        company_email=company["Contact Email"], 
        phone_number=company["Contact Phone Number"], 
        description=company["Description"],
        )
    db.session.add(new_company)

db.session.commit()

from unicodedata import category
from app.app import create_app
from app.users.models import Company, User
from app.extensions.database import db

app = create_app()
app.app_context().push()

initial_user_dict = {
    "Email": "melvin.rinkleff@gmx.de",
    "Password": 12345678,
    "First Name": "Melvin", 
    "Last Name": "Rinkleff",
    "Street": "Alfred-Jung-Straße", 
    "ZIP": "310715",
    "Town": "Berlin",
    "Country": "Germany",
    }


all_accounts_dict = {
    "Sparkasse Hannover": {
        "Account": "Sparkasse Hannover", 
        "Category": "Banking", 
        "Contact Email": "info@sparkasse-hannover.de",
        "Contact Phone Number": "051130007070", 
        "Description": "primary banking account", 
        },
    "N26 Bank": {
        "Account": "N26", 
        "Category": "Banking", 
        "Contact Email": "support@n26.com",
        "Contact Phone Number": "030364286880", 
        "Description": "Second banking account", 
        },
    "Katapult Magazin": {
        "Account": "Katapult", 
        "Category": "Magazines", 
        "Contact Email": "redaktion@katapult-magazin.de",
        "Contact Phone Number": "017656998944", 
        "Description": "Yearly subscription magazines account", 
        }
}

new_user = User(
    user_email=initial_user_dict["Email"], 
    password=initial_user_dict["Password"],
    first_name=initial_user_dict["First Name"], 
    last_name=initial_user_dict["Last Name"], 
    street_name=initial_user_dict["Street"], 
    zip_code=initial_user_dict["ZIP"],
    town=initial_user_dict["Town"],
    country=initial_user_dict["Country"],
    )
new_user.save()


for company_name, company in all_accounts_dict.items():
    new_company = Company(
        user_id=User.query.filter_by(user_email="melvin.rinkleff@gmx.de").first().id,
        name=company["Account"], 
        category=company["Category"], 
        company_email=company["Contact Email"], 
        phone_number=company["Contact Phone Number"], 
        description=company["Description"],
        )
    db.session.add(new_company)

db.session.commit()

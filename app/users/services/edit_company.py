from app.users.models import Company

def edit_company(form_data, company):
    # edit company
    if form_data.get('company_name'):
        company.name=form_data.get('company_name')

    if form_data.get('company_category'):
        company.category=form_data.get('company_category')

    if form_data.get('company_company_email'):
        company.company_email=form_data.get('company_company_email')

    if form_data.get('company_phone_number'):
        company.phone_number=form_data.get('company_phone_number')

    if form_data.get('company_description'):
        company.description=form_data.get('company_description')

    company.save()
    
    return company
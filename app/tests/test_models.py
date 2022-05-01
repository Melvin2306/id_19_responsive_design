from app.extensions.database import db
from app.users.models import Company

def test_company_update(client):
    # updates company name to Sparkasse
    test_company = Company(
        name = "N26",
        category = "Finance",
        company_email = "info@n26.de",
        phone_number = "018343974",
        description = "Test test"
        )

    db.session.add(test_company)
    db.session.commit()

    test_company.name = "Sparkasse"
    test_company.save()

    updated_company = Company.query.filter_by(category="Finance").first()
    assert updated_company.name == "Sparkasse"

def test_company_delete(client):
    # deletes company
    test_company = Company (
        name = "N26",
        category = "Finance",
        company_email = "info@n26.de",
        phone_number = "018343974",
        description = "Test test"
        )
    db.session.add(test_company)
    db.session.commit()

    test_company.delete()

    deleted_company = Company.query.filter_by(name="N26").first()
    assert deleted_company is None
from app.extensions.database import db, CRUDMixin
from flask_login import UserMixin
import uuid

class User(db.Model, CRUDMixin, UserMixin):
    id = db.Column('id', db.String(999), default=lambda: str(uuid.uuid4()), primary_key=True)
    user_email = db.Column(db.String(40), index = True, unique = True)
    password = db.Column(db.String(999))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    street_name = db.Column(db.String(40))
    zip_code = db.Column(db.Numeric(8, 0))
    town = db.Column(db.String(20))
    country = db.Column(db.String(20))
    companies = db.relationship('Company', backref='user', lazy=True)

class Company(db.Model, CRUDMixin):
    id = db.Column('id', db.String(999), default=lambda: str(uuid.uuid4()), primary_key=True)
    user_id = db.Column(db.Text, db.ForeignKey('user.id'))
    name = db.Column(db.String(30))
    category = db.Column(db.String(20))
    company_email = db.Column(db.String(40))
    phone_number = db.Column(db.String(20))
    description = db.Column(db.String(100))
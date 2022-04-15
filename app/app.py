from flask import Flask, redirect, url_for, render_template, send_file
from app.extensions.database import db, migrate
from . import simple_pages, users

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    register_extensions(app)
    register_blueprints(app)
    return app

# Blueprints
def register_blueprints(app: Flask):
    app.register_blueprint(simple_pages.routes.blueprint)
    app.register_blueprint(users.routes.blueprint)
# Extensions
def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)


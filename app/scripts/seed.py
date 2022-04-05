from app.app import create_app
#Anpassen ->    from app.jobs.models import Job
from app.extensions.database import db

app = create_app()
app.app_context().push()

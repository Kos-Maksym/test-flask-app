from learn_python import db, app

app.app_context().push()
db.create_all()
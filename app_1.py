from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/appdb'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(80), unique=True)
    post_text = db.Column(db.String(255))

    def __init__(self, title, post_text):
        self.title = title
        self.post_text = post_text


@app.route('/')
def index():
    return "Hello World"


if __name__ == "__main__":
    manager.run()
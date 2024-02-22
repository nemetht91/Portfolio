from flask import Flask, render_template, redirect, url_for, request, flash, abort
from os import environ, path
import sqlalchemy.exc
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc


LANGUAGE_LOGO_PATH = "static/img/logos/"

app = Flask(__name__)
app.secret_key = environ.get("SECRET_KEY")
app.config['SESSION_TYPE'] = 'filesystem'

##CONNECT TO DB
DATABASE_SCHEME = environ.get("DATABASE_SCHEME")
DATABASE_USER = environ.get("DATABASE_USER")
DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD")
DATABASE_HOST = environ.get("DATABASE_HOST")
DATABASE_PORT = environ.get("DATABASE_PORT")
DATABASE_NAME = environ.get("DATABASE_NAME")

database_string = f"{DATABASE_SCHEME}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}" \
                  f"/{DATABASE_NAME}"


engine = sqlalchemy.create_engine(database_string, pool_pre_ping=True, pool_size=10, max_overflow=20, pool_recycle=300,
                                  connect_args={
                                      "keepalives": 1,
                                      "keepalives_idle": 30,
                                      "keepalives_interval": 10,
                                      "keepalives_count": 5,
                                       "sslmode": "disable"
                                  }
                                  )

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_DATABASE_URI'] = database_string


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text, nullable=False)
    challenges = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(500), nullable=False)
    github_url = db.Column(db.String(500), nullable=False)
    website = db.Column(db.Boolean, nullable=True)
    languages = db.Column(db.String(250), nullable=False)


with app.app_context():
    #print('sqlalchemy engine:', db.engine)
    db.create_all()
    db.session.commit()

    # close the sql pool connections so that new forks create their own connection.
    db.session.remove()
    db.engine.dispose()

@app.route('/')
def get_home():
    return render_template("index.html")


@app.route('/about')
def get_about():
    return render_template("about.html")


@app.route('/portfolio')
def get_portfolio():
    projects = get_all_projects()
    return render_template("projects.html", projects=projects)


@app.route('/project/<int:project_id>')
def get_project(project_id):
    project = Project.query.get(project_id)
    languages = get_language_logos(project.languages)
    return render_template("project.html", project=project, languages=languages)


@app.route('/contact')
def get_contact():
    return render_template("contact.html")


def get_all_projects():
    return Project.query.order_by(desc(Project.id)).all()


def get_language_logos(raw_languages: str):
    languages = raw_languages.split(", ")
    language_logos = []
    for language in languages:
        if path.isfile(f"{LANGUAGE_LOGO_PATH}{language}.png"):
            language_logos.append(f"../{LANGUAGE_LOGO_PATH}{language}.png")
    return language_logos


if __name__ == "__main__":
    app.run(debug=True)
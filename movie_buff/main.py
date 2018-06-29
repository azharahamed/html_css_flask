from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import username, password, host, port, database

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_ECHO'] = True


connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
db = SQLAlchemy(app)
db_session = db.session

class Director(db.Model):
  __tablename__ = 'directors'

  country = db.Column(db.String(120))
  first = db.Column(db.String(50))
  last = db.Column(db.String(50))
  director_id = db.Column(db.Integer, primary_key=True)

  movies = db.relationship('Movies', backref='directors')

  def __str__(self):
    return f'Directors Table: \nCountry: {self.country}\nFirst: {self.first}\nLast: {self.last}\nDirector Id: {self.director_id}\n'

class Movies(db.Model):
  __tablename__ = 'movies'
  movie_id = db.Column(db.Integer, primary_key= True)
  title = db.Column(db.String(50))
  year = db.Column(db.Integer)
  director_id = db.Column(db.Integer,db.ForeignKey('directors.director_id'))

  director = db.relationship('Director')
  viewing = db.relationship('Viewings', backref="movies")

  def __str__(self):
    return f'Movies Table: \Movie Id: {self.movie_id}\Title: {self.title}\nYear: {self.year}\nDirector Id: {self.director_id}\n'

class Viewers(db.Model):
  __tablename__ = 'viewers'

  viewer_id = db.Column(db.Integer, primary_key=True)
  first = db.Column(db.String(60))
  last = db.Column(db.String(60))
  movie_id = db.Column(db.String(60))
  viewings = db.relationship('Viewings', backref="viewers")

  def __str__(self):
    return f'Viewers Table: \Viewer Id: {self.viewer_id}\nFirst: {self.first}\nlast: {self.last}\nMovie Id: {self.movie_id}\n'

class Viewings(db.Model):
  __tablename__ = 'viewings'

  date_viewed = db.Column(db.DateTime)
  viewing_id = db.Column(db.Integer, primary_key=True)
  viewer_id = db.Column(db.Integer, db.ForeignKey('viewers.viewer_id'))
  movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))

  movie = db.relationship('Movies')
  viewer = db.relationship('Viewers')

  def __str__(self):
    return f'Viewings Table: \nDate Viewed: {self.date_viewed}\nViewing Id: {self.viewing_id}\nviewer_id: {self.viewer_id}\nMovie Id: {self.movie_id}\n'


# director_row = Director.query.get(1)
director_query = Viewings.query.filter_by(viewing_id=1)

for viewings in director_query:
  print(viewings.movie.director.last)

app.run()


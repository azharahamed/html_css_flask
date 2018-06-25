from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too
app.config['ENV'] = 'development'

@app.route("/")
def index():
    content = f"""
      <html>
      <head></head>
      <body>
        <form action="/submit" method = "POST" id = "usrform">
          <span>I want to cross off </span><select name="movielistvalue">{getMovielistinHTML()}</select><span>from my Watchlist.</span><br>
          <input type="submit" name="Submit This" id="submit_button">
        </form>
      </body>
      </html>
    """

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"

    return content

@app.route("/submit", methods = ["POST"])
def submitpage():
  movie_name=request.form['movielistvalue']
  return cross_off(movie_name)

  
def cross_off(moviename):
  returnstring = f"""
      <html>
      <head></head>
      <body>
        <span style = "text-decoration: line-through">{moviename}</span>  has been crossed off your Watchlist.        
      </body>
      </html>
  """
  return returnstring

def getMovielistinHTML():
  movielist = ["The Shawshank Redemption", "The Godfather", "The Godfather: Part II", "The Dark Knight", "12 Angry Men"]
  rtn_str = ""
  for movie in movielist:
    rtn_str = f'{rtn_str}\n<option value="{movie}">{movie}</option>'
  
  return rtn_str;


app.run()
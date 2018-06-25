from flask import Flask, request, redirect
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too
app.config['ENV'] = "development"  

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""

# a form for adding new movies
add_form = """
    <form action="/add" method="post">
        <label>
            I want to add
            <input type="text" name="new-movie"/>
            to my watchlist.
        </label>
        <input type="submit" value="Add It"/>
    </form>
"""

current_watchlist = [ "Star Wars", "Minions", "Freaky Friday", "My Favorite Martian" ]
    # returns user's current watchlist--hard coded for now

# a form for crossing off watched movies
# (first we build a dropdown from the current watchlist items)

def getcrossoff_form():
  crossoff_options = ""
  for movie in current_watchlist:
      crossoff_options += '<option value="{0}">{0}</option>'.format(movie)

  crossoff_form = """
      <form action="/crossoff" method="post">
          <label>
              I want to cross off
              <select name="crossed-off-movie"/>
                  {0}
              </select>
              from my watchlist.
          </label>
          <input type="submit" value="Cross It Off"/>
      </form>
  """.format(crossoff_options)
   
  return crossoff_form

# a list of movies that nobody should have to watch
terrible_movies = [
    "Gigli",
    "Star Wars Episode 1: Attack of the Clones",
    "Paul Blart: Mall Cop 2",
    "Nine Lives",
    "Starship Troopers"
]

@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']

    if crossed_off_movie not in current_watchlist:
        # the user tried to cross off a movie that isn't in their list,
        # so we redirect back to the front page and tell them what went wrong
        error = "'{0}' is not in your Watchlist, so you can't cross it off!".format(crossed_off_movie)

        # redirect to homepage, and include error as a query parameter in the URL
        return redirect("/?error=" + error)

    # if we didn't redirect by now, then all is well
    crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
    confirmation = crossed_off_movie_element + " has been crossed off your Watchlist."
    content = page_header + "<p>" + confirmation + "</p>" + page_footer
    current_watchlist.remove(crossed_off_movie_element)
    return content

@app.route("/add", methods=['POST'])
def add_movie():
    new_movie = request.form['new-movie']

    # TODO 
    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    new_movie = cgi.escape(new_movie, quote=True)
    
    # TODO 
    # if the user typed nothing at all, redirect and tell them the error
    if not new_movie:
      error = "User didn't type any thing"
      return redirect("/?error=" + error)

    # TODO 
    # if the user wants to add a terrible movie, redirect and tell them not to add it b/c it sucks
    elif new_movie in terrible_movies:
      error = "This movie sucks"
      return redirect("/?error=" + error)

    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer
    current_watchlist.append(new_movie)

    return content

@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"

    # if we have an error, make a <p> to display it
    error = request.args.get("error")
    if error:
        error_esc = cgi.escape(error, quote=True)
        error_element = '<p class="error">' + error_esc + '</p>'
    else:
        error_element = ''

    # combine all the pieces to build the content of our response
    main_content = edit_header + add_form + getcrossoff_form() + error_element


    # build the response string
    content = page_header + main_content + page_footer

    return content

app.run()
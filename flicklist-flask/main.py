from flask import Flask
from random import randrange

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    tom_movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"
    content += "<h1>Tommorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + tom_movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"

    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    # TODO: randomly choose one of the movies, and return it
    lst = ["The Shawshank Redemption", "The Godfather", "The Godfather: Part II", "The Dark Knight", "12 Angry Men"]
    return lst[randrange(5)]


app.run()
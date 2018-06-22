from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['ENV'] = 'development'


@app.route('/<post_title>')
def show_post(post_title):
  return post_title

app.run(port=8008)
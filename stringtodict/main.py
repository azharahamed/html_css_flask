def dicttostring(dictionary):
  strng = ''
  for key, item in dictionary.items():
    strng += f'{key}={item}&' 
  return strng

from flask import Flask, render_template, request, redirect
from cgi import escape

app = Flask(__name__)
app.config['ENV'] = 'develeopment'
app.config['DEBUG'] = True

@app.route('/')
def index():
  if request.args:
    print(request.args)
  return render_template("login.html",display_dict=request.args)

@app.route("/submit", methods=['POST'])
def submit():
  dictionary={}
  i = 0
  prev_item = ''
  print("Multidict Values", request.form)
  form = request.form
  print(len(form))
  for item in request.form.values():
    # item = escape(item)
    print(item)
    if(i!=0 and i%2 !=0 and prev_item):
      dictionary[prev_item] = item
    prev_item = item
    i += 1
  return redirect("/?"+dicttostring(dictionary)) 

app.run()

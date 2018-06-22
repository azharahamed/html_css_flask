from flask import Flask, request
from helpers import encrypt

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too
app.config["ENV"] = 'Development' #Setting env as developent

@app.route("/")
def index():
  strng = """
              <html>
                <head>
                    <style>
                        form {
                            background-color: #eee;
                            padding: 20px;
                            margin: 0 auto;
                            width: 540px;
                            font: 16px sans-serif;
                            border-radius: 10px;
                        }
                        textarea {
                            margin: 10px 0;
                            width: 540px;
                            height: 120px;
                        }
                    </style>
                </head>
                <body>
                  <form action="/submit" method = "POST" id = "usrform">
                    <label for="rotate">Rotate By:</label>
                    <input type="text" name="rotate"><br>
                    <textarea rows="4" cols="50" name="originaltext" form="usrform">Enter text here...</textarea>
                    <input type="submit">
                </body>
              </html>
  """
  return strng

@app.route('/submit', methods=['POST'])
def submit():
  text = request.form['originaltext']
  rotate = int(request.form['rotate'])
  encrypt_text = encrypt(text,rotate)
  return_text = ''
  for char in encrypt_text:
    if(char == '\n'):
      return_text = f'{return_text}<br>'
    else:
      return_text = f'{return_text}{char}'
  strng = """
              <html>
                <head>
                    <style>
                        body {
                            background-color: #eee;
                            padding: 20px;
                            margin: 0 auto;
                            width: 540px;
                            font: 16px sans-serif;
                            border-radius: 10px;
                        }
                        textarea {
                            margin: 10px 0;
                            width: 540px;
                            height: 120px;
                        }
                    </style>
                </head>
                <body>
  """
  return_text = f'{strng}\n<h1>The encrypted text is :</h1>\n<br><p>{return_text}</p></body></html>'
  return return_text

app.run()
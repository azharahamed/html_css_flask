from flask import Flask, request, render_template, redirect

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too
app.config['ENV'] = 'development'



@app.route("/")
def index():
  errormessages = {}
  error = request.args.get("error")
  username = request.args.get("username")
  usernameerror = request.args.get("usernameerror")
  password1 = request.args.get("password1")
  password2 = request.args.get("password2")
  email = request.args.get("email")
  emailerror = request.args.get("emailerror")

  if error:
    errormessages['error'] = "Username and Password fields are mandatory"
  if usernameerror:
    errormessages['username'] = "Invalid Username"
  if password1:
    errormessages['password1'] = "Invalid Password"
  if password2:
    errormessages['password2'] = "Password mistmatch"
  if emailerror:
    errormessages['email'] = "Invalid email Id"
  print(username)
  return render_template("login.html",username=username,errormessage=errormessages,email=email)

@app.route("/register", methods=['POST'])
def validation():
  validation = True
  username = request.form['username']
  email = request.form['email']
  pw1 = request.form['password1']
  pw2 = request.form['password2']
  return_string = "/?"

  if username:
    return_string += "username="+username+"&"
  if email:
    return_string += "email="+email+"&"

  if(username and pw1 and pw2):
    if(len(username) < 3 or len(username) > 20 or (' ' in username)):
      return_string += "usernameerror="+username+"&"
      validation = False
    if(len(pw1) < 3 or len(pw1) > 20 or (' ' in pw1)):
      return_string += "password1=False&"
      validation = False
    if(pw1 != pw2):
      return_string += "password2=False&"
      validation = False
    if(email != ''):
      if(email.count('@')>1 or email.count('.')>1 or email.count('@') == 0 or email.count('.') == 0 ):
        return_string += "emailerror="+email+"&"
        validation = False
    if(validation == False):
      return redirect(return_string)
    else:
      return render_template("welcome.html",username=username)

  else:
    return redirect("/?error=Username and Password missing")
    

app.run()
from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['ENV'] = 'development'

class Vehicle:
  def __init__(self):
    self.v_type = ''
    self.model_yr = ''
    self.made = ''
    self.vin = 0 
  
  def __repr__(self):
    return f"""
    <tr>
      <th>{self.v_type}</th>
      <th>{self.model_yr}</th>
      <th>{self.made}</th>
      <th>{self.vin}</th>
    <tr>"""

vehicles = []

@app.route('/')
def index():
  return '''
  <form action="/submit" method = "POST">
    <label for="v_type">Vehicle Type :</label>
    <input type="text" name="v_type"><br>
    <label for="model_yr">Model Year :</label>
    <input type="text" name="model_yr"><br>
    <label for="made">Made :</label>
    <input type="text" name="made"><br>
    <label for="vin">VIN :</label>
    <input type="text" name="vin"><br>
    <input type="submit" value="Submit">
  </form>
  '''
@app.route('/submit',methods=['POST'])
def submit():
  vehicle = Vehicle()
  for key, value in request.form.items():
    # print(f"Key: {key} Value: {value}")
    if key == 'v_type':
      vehicle.v_type = value
    elif key == 'model_yr':
      vehicle.model_yr = value
    elif key == 'made':
      vehicle.made = value
    elif key == 'vin':
      vehicle.vin = value
  vehicles.append(vehicle)
  return f'Values Submitted thanks <a href="http://127.0.0.1:8008/">click here</a> to submit another vehicle details<br>{vehicle}'

@app.route('/display')
def display():
  strng = """
  <table> 
    <tr>
      <th>Vehicle Type</th>
      <th>Model</th>
      <th>Made</th>
      <th>VIN</th>
    <tr>  
  """
  for item in vehicles:
    strng = f'{strng}{item}'
  strng = f'{strng}<table>'
  return strng

app.run(port=8008)
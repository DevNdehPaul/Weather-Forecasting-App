from flask import Flask, render_template, request
import requests
api_key = "cee8ab5fe84041fb95754318252810"
endpoint = "http://api.weatherapi.com/v1/forecast.json"
method = "GET"
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/weather', methods = ['GET', 'POST'])
def weather():
    search = request.form.get('city')
    # Here we have our Headers
    headers = {
    "x-access-token" : api_key,
    "content_type" : "application/json"
     }
# Here we have our Parameters
    params = {
    "key" : api_key,
    "q" : search
    }
    response = requests.request( method, endpoint, params = params, headers = headers)
    data = response.json()
    town = data['location']['name']
    country = data['location']['country']
    temp = float(data['current']['temp_c'])
    temp = 273.15 + temp
    temp = round(temp,2)
    con = data['current']['condition']['text']
    hu = data['current']['humidity']
    wi = data['current']['wind_kph']
    print()
    return render_template('index.html',town = town, country = country, temp = temp, con = con, hu = hu, wi = wi)

if __name__ == "__main__":
    app.run(debug=True)


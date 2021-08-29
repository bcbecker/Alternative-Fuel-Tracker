from flask import render_template, request, Blueprint
#temporary, need to establish some other way
from config import Config
import requests
import json

main = Blueprint('main', __name__)

#these need to go to a search function, data gathered from a form
fuel_type = "E85"
location = "48382"
range_in_miles = "7"
#limit or offset? (see docs)

URL = "https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json?api_key=" + str(Config.API_KEY) + "&location=" + location + "&fuel_type=" + fuel_type + "&radius=" + range_in_miles


@main.route("/")
@main.route("/home")
def home():
    response = requests.get(URL).json()
    location_response = response['fuel_stations']
    return render_template('index.html', location_response=location_response)

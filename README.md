# Alternative-Fuel-Tracker
If you embrace alternative and renewable energy, you know it can be challenging to find gas stations sharing that mentality. Alternative Fuel Tracker is here to save the day! Offering flexible search parameters, AFT can find you a station that fits your needs, and then direct you to it.

The live demo is viewable through my portfolio.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Improvements](#improvements)


## General Information
AFT is a practical example of third-party API consumption. It is an intersection of the Google Maps API and the National Renewable Energy Lab (NREL) API: passing data retrieved about gas stations from the NREL, to Google Maps geocoding, providing both a visual representation and directions. Users can search using a wide variety of acceptable formats (Zip, City/State, Address/City/State), limit their search range, and select the type of alternative fuel they're after. This query string is formatted and a request is sent to the NREL API, which returns JSON containing information about each matching location. Using Jinja2, the results are displayed, and a marker is created on the map for each result through the Google Maps geocoder. Users can redirect to Google Maps, en route, by clicking the 'Directions' button.

My favorite thing about this project is that it solves a real-life problem in an elegant way. I, and many others in the automotive community, opt to use Ethanol-based fuels in performance-oriented vehicles, and finding stations locally that carry Ethanol can be difficult. This little app not only tracks them down and gives me directions, but it also shows the date for which that particular station was last confirmed to carry Ethanol. This small feature is crucial, because nobody wants to get to the location only to find out they stopped carrying that fuel type last year!


## Technologies Used
- Flask, a micro-framework
    - WTForms for validation
    - Jinja2 templating engine
- National Renewable Energy Lab API
- Google Maps API
- Bootstrap CSS
- JavaScript, jQuery
- Deployed with AWS Elastic Beanstalk with CodePipeline


## Features
- Search by zip, city/state, or full address
- Filter by fuel type and distance to location
- Fully interactive map displaying labeled locations
- Get directions through Google Maps redirect


## Setup
Ensure python 3.9 is installed.

Install requirements:
```bash
pip install -r requirements.txt
```

Or, access virtual environment:
```bash
pip install pipenv
pipenv shell
```

### Creating .env file
For this server to run, you must create a .env file within the package, setting the following parameters:
```bash
SECRET_KEY=
NREL_API_KEY=
GOOGLE_API_KEY=
```
Set the secret key to whatever you'd like! You will need to get API keys from both Google, and NREL (https://developer.nrel.gov).

### Running the Server
```bash
python run.py
```

### Viewing the website
Site can be found here: http://127.0.0.1:5000/
(for localhost)


## Improvements
Improvements:
- Make the map more responsive for phones

To Do:
- Configure https
- Update AWS CodePipeline to include testing

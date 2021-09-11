from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    """
    Collects parameters for querying API
    """
    fuel_type_choices = [("BD", "Biodiesel"), ("CNG", "Compressed Natural Gas"),
            ("ELEC", "Electric"), ("E85", "Ethanol (E85)"), ("HY", "Hydrogen"),
                ("LNG", "Liquefied Natural Gas"), ("LPG", "Propane")]

    distance_radius_choices = ["1", "2", "3", "4", "5", "10", "15", "20", "25", "50", "100"]

    address_city_state_zip = StringField("Search Location", validators=[DataRequired()])

    fuel_type = SelectField("Fuel Type", choices=fuel_type_choices, validate_choice=True, default="all", validators=[DataRequired()])

    distance_radius = SelectField("Distance", choices=distance_radius_choices, validate_choice=True, default="5", validators=[DataRequired()])

    submit = SubmitField("Find Stations")
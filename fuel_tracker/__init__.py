from flask import Flask
from fuel_tracker.config import ProductionConfig



def create_app(config_class=ProductionConfig):
    application = Flask(__name__)
    application.config.from_object(config_class)


    from fuel_tracker.routes import main
    application.register_blueprint(main)

    return application
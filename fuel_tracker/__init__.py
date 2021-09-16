from flask import Flask
from config import ProductionConfig



def create_app(config_class=ProductionConfig):
    application = Flask(__name__)
    application.config.from_object(ProductionConfig)


    from fuel_tracker.routes import main
    application.register_blueprint(main)

    return application
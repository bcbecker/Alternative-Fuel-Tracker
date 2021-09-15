from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import ProductionConfig


limiter = Limiter(key_func=get_remote_address,
  default_limits=["50/day"])


def create_app(config_class=ProductionConfig):
    application = Flask(__name__)
    application.config.from_object(ProductionConfig)
    limiter.init_app(application)


    from fuel_tracker.routes import main
    application.register_blueprint(main)

    return application
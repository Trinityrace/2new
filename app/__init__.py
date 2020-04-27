from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()
# # Initializing application
# app = Flask(__name__,instance_relative_config = True)

# # Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# from app import views

def create_app(config_name):
    app = Flask(__name__)

    # Creating app configurations
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    bootstrap.init_app(app)

    # Registering the BluePrint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting up config
    from .request import configure_request
    configure_request(app)

    return app
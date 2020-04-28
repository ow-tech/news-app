from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()



#Initializing application

def create_app(config_name):
    app = Flask(__name__)

        # Creating app configurations
    app.config.from_object(config_options[config_name])

    # # Setting up configuration
    # app.config.from_object(DevConfig)
    # app.config.from_pyfile('config.py')

    #Initializing Flask Extensions
    bootstrap.init_app(app)

 # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting the config
    from .request import configure_request
    configure_request(app)


    return app
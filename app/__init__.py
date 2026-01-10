from flask import Flask
from config import Config
from flask_moment import Moment
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


moment = Moment()

# configure application according to what is defined in config class

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = config_class.STATIC_FOLDER
    app.template_folder = config_class.TEMPLATE_FOLDER
    # creates the database for communication
    bootstrap.init_app(app)
    moment.init_app(app)
   
    # blue print registration
    from app.Controller.routes import routes_blueprint as routes
    app.register_blueprint(routes)

    return app
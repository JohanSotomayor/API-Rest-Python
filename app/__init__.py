from flask import Flask, g
from config import settings
from .models import db
from flask_sqlalchemy import SQLAlchemy
from .middlewares.errorhandler import ErrorHandler
from .router import RouterConfig
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from flask_cors import CORS

class AppConfig:
    def __init__(self):
        self.app = Flask(__name__)
        self.configure_app()
        self.configure_db()
        self.configure_routes()
        self.configure_error_handlers()

    def configure_app(self):
        CORS(self.app, resources={r"/api/*": {"origins": "*"}}) # Configurar CORS
        self.app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URI
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        

    def configure_db(self):

        try:
            engine = create_engine(settings.DATABASE_URI)
            with engine.connect() as connection:
                print("Conexión exitosa a la base de datos")

            db.init_app(self.app)
            with self.app.app_context():
                db.create_all()  # Crear las tablas en la base de datos

        except OperationalError as e:
            print("Error al conectar a la base de datos:", e)


    def configure_routes(self):
        RouterConfig.register_blueprints(self.app)

    def configure_error_handlers(self):
        self.app.register_error_handler(404, ErrorHandler.not_found_error)
        self.app.register_error_handler(Exception, ErrorHandler.unhandled_exception)

        
def create_app():
    return AppConfig().app
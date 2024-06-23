from flask import Blueprint, jsonify, g

class ErrorRoutes:
    def __init__(self):
        self.main = Blueprint('error', __name__, url_prefix='/api/error')
        self.Error_routes()

    def Error_routes(self):
        @self.main.route('/')
        def forceError(self):
                raise Exception("500")

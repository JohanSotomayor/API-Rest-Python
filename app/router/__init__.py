from .error import ErrorRoutes
from .products import ProductRoutes
from .clients import ClientsRoutes

class RouterConfig:

    @staticmethod
    def register_blueprints(app):
        error_routes = ErrorRoutes()
        # product_routes = ProductRoutes()
        # clients_routes = ClientsRoutes()
        app.register_blueprint(error_routes.main)
        # app.register_blueprint(product_routes.main)
        # app.register_blueprint(clients_routes.main)

        

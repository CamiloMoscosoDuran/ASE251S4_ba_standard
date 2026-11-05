from flask import Flask
from flask_cors import CORS
from app.routes.sales_routes import sales_bp
from app.routes.product_routes import products_bp
from app.config.swagger import swagger_bp
app = Flask(
    __name__,
    static_folder="../static",
    static_url_path="/static"
)


# Permitir consumo desde frontend y aplicaciones móviles
CORS(app)
app.json.ensure_ascii = False
app.json.sort_keys = False


# Registrar Blueprints
app.register_blueprint(sales_bp)
app.register_blueprint(products_bp)
app.register_blueprint(swagger_bp)
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

from flask import Blueprint, jsonify
from app.services.analytics import product_service


products_bp = Blueprint(
    "products",
    __name__
)


@products_bp.route(
    "/analytics/integrated/top-product",
    methods=["GET"]
)
def top_product_month():
    result = product_service.get_top_product_month()
    if not result:
        return jsonify({
            "message":
            "No se encontró información"
        }), 404
    return jsonify(
        result.__dict__
    )

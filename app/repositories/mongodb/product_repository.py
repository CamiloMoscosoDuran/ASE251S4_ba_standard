from app.database.mongodb import db


def get_product_by_id(product_id):
    """
    Obtiene información del producto
    mediante product_id.
    """
    product = db.products.find_one(
        {
            "product_id": product_id
        }
    )
    return product

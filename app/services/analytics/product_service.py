from app.repositories.sqlserver.sales_repository import SalesRepository
from app.repositories.mongodb import product_repository as product_repo
from app.schemas.analytics_schema import IndicatorResponse

sales_repository = SalesRepository()


def get_top_product_month():
    """
    Obtiene el producto más vendido
    integrando información de SQL Server
    y MongoDB.
    """
    # 1. Obtener ventas desde SQL Server
    sales_data = sales_repository.get_top_product()
    if not sales_data:
        return None

    # 2. Obtener información del producto desde MongoDB
    product = product_repo.get_product_by_id(
        sales_data["product_id"]
    )

    if not product:
        return None

    # 3. Integrar ambas fuentes
    data = {
        "product_id":
        sales_data["product_id"],
        "product":
        product.get("name"),
        "category":
        product.get("category"),
        "quantity":
        sales_data["quantity"]
    }

    # 4. Retornar indicador estándar
    return IndicatorResponse(
        indicator="top_product_month",
        title="Producto más vendido del mes",
        chart_type="card",
        data=data,
        sources=[
            "SQL Server",
            "MongoDB"
        ]
    )

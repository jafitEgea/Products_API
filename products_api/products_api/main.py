from fastapi import FastAPI, APIRouter, HTTPException
from model.schemas import Product, ProductCreate

app = FastAPI(title = "PRODUCTS API")

api_router = APIRouter()

products = [
    {
        "id": 1,
        "name": "Iphone 13",
        "quantity": 12,
        "description": "Nuevo celular de Apple",
        "price": 4500000,
        "category": 1 

    },
    {
        "id": 2,
        "name": "MSI GF13 thin",
        "quantity": 10,
        "description": "Laptop para gamer",
        "price": 5000000,
        "category": 2
    }
]

#products list
@api_router.get("/products/")
def products_list() -> dict:
    return products

#products by id
@api_router.get("/products/{id}/", status_code = 200, response_model = Product)
def fetch_product(*, id: int) -> any:
    result = [product for product in products if product["id"] == id]
    if not result:
        raise HTTPException(status_code = 404, detail = "Product with id " + str(id) + " not found")
    return result[0];

#products by category_id
@api_router.get("/products/category/{category_id}/", status_code = 200, response_model = Product)
def fetch_product_by_category_id(*, category_id: int) -> any:
    result = [product for product in products if product["category"] == category_id]
    if not result:
        raise HTTPException(status_code = 404, detail = "Product with category id " + str(category_id) + " not found")
    return result[0];

#create product
@api_router.post("/products/", status_code = 201, response_model = ProductCreate)
def create_product(*, product_in: ProductCreate) -> dict:
    new_entry_id = len(products) + 1
    products_entry = Product(
        id = new_entry_id,
        name = product_in.name,
        quantity =  product_in.quantity,
        description = product_in.description,
        price = product_in.price,
        category = product_in.category
    )
    products.append(products_entry.dict())
    return products_entry

app.include_router(api_router)

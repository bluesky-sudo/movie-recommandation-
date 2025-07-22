# routes/products.py

from fastapi import APIRouter, HTTPException
from models.product import serialize_product
from database import products_collection
from bson import ObjectId

router = APIRouter(prefix="/products", tags=["Products"])

# GET all products
@router.get("/")
def get_products():
    products = products_collection.find()
    return [serialize_product(p) for p in products]

# ✅ POST - Add a new product
@router.post("/")
def add_product(product: dict):
    result = products_collection.insert_one(product)
    new_product = products_collection.find_one({"_id": result.inserted_id})
    return serialize_product(new_product)

# GET a single product by ID
@router.get("/{product_id}")
def get_product(product_id: str):
    product = products_collection.find_one({"_id": ObjectId(product_id)})
    if product:
        return serialize_product(product)
    raise HTTPException(status_code=404, detail="Product not found")

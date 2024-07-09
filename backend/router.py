from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schema import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_product,
    get_products,
    delete_product,
    update_product
    )

router = APIRouter()


@router.get("/products", response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    products = get_products(db)
    return products

@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_product(product_id:int, db:Session = Depends(get_db)):
    db_product = get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="produto inexistente")
    return db_product


@router.post("/products", response_model=ProductResponse)
    
def create_product(product: ProductCreate, db:Session = Depends(get_db)):
    return create_product(product = product, db=db)


@router.delete("/products/{product_id}", response_model = ProductResponse)

def delete_product(product_id: int, db:Session = Depends(get_db)):
    product_db = delete_product(product_id=product_id, db=db)
    if product_db is None:
            raise HTTPException(status_code=404, detail="produto inexistente")
    return delete_product(product_id=product_id, db=db)

    
    @router.put("/products/{product_id}", response_model=ProductResponse)
    
    def atualizar_product(product_id: int, product:ProductUpdate, db:Session = Depends(get_db)):
        product_db = update_product(db=db, product_id=product_id, product=product)
        if product_db is None:
            raise HTTPException(status_code=404, detail="produto inexistente")
        return product_db
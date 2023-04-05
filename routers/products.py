from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(prefix="/products", 
                   tags=["products"],
                   responses={404: {"message":"No encontrado"}})

class Product(BaseModel):
    id: int
    name: str

products_list = [Product(id=0, name="Producto 1"),
                Product(id=1, name="Producto 2")]

#All products
@router.get("/")
async def products():
    return products_list

#All products Path
@router.get("/products/{id}")
async def product(id: int):
    return search_product(id)

#POST
@router.post("/product/{id}")
async def product(product: Product):
    if type(search_product(product.id)) == Product:
        raise HTTPException(status_code=404, detail="El producto ya existe")
    products_list.append(product)
    return product


#PUT
@router.put("/product/{id}")
async def product(product: Product):

    found = False
    for index, saved_product in enumerate(products_list):
        if saved_product.id == product.id:
            products_list[index] = product
            found = True

    if not found:             
        return {"error":" no se a actualizado el producto"}
    return product
    

#DELETE
@router.delete("/product/{id}")
async def product(id: int):

    found = False
    for index, saved_product in enumerate(products_list):
        if saved_product.id == id:
            del products_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el producto"}



#Funcion search id
def search_product(id: int):
    products = filter(lambda product: product.id == id, products_list)
    try:
        return list(products)[0]
    except:
        return {"error":"No se a encontrado el producto"}
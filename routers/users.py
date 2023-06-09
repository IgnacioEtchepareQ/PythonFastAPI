from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import uvicorn

#uvicorn main:app --reload
router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: {"message":"No encontrado"}})

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_list = [User(id=0, name="Ignacio", surname="Etchepare", age="30"),
             User(id=1, name="Testeo", surname="Prueba", age="15")]

#All user
@router.get("/")
async def users():
    return users_list


#Path
@router.get("/users/{id}")
async def user(id: int):
    return search_user(id)

#Query
@router.get("/userquery")
async def user(id: int):
   return search_user(id)
    
    

#POST 
@router.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    users_list.append(user)
    return user

#PUT
@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:             
        return {"error":" no se a actualizado el usuario"}
    return user


#DELETE
@router.delete("/user/{id}")
async def user(id: int):

    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}

      


#Función buscar usuario por id
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":" no se a encontrado el usuario"}
    


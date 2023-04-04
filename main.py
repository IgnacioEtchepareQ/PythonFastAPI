from fastapi import FastAPI
from routers import products, users

app = FastAPI()

@app.get("/")
async def root ():
    return "Hola!"


# Routers

app.include_router(products.router)
app.include_router(users.router)

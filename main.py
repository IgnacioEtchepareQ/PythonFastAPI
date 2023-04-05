from fastapi import FastAPI
from routers import products, users

#uvicorn main:app --reload

app = FastAPI()

@app.get("/")
async def root ():
    return "Hola!"

@app.get("/url")
async def url():
    return {"url":"https://youtube.cl"}

# Routers

app.include_router(products.router)
app.include_router(users.router)

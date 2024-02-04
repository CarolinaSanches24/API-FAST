from fastapi import FastAPI, HTTPException;
from typing import List
from uuid import UUID;
from models import User, Role;

app = FastAPI()

db: List[User] = [
    User(
        id = UUID("c9029d3e-82c2-4da8-a307-c16fdbff8e54"),
        first_name="Ana",
        last_name="Maria",
        email="ana@gmail.com",
        role=[Role.role_1]
    ),
    User(
        id = UUID("08aaa45a-c0ea-4d46-acab-d65e2aa6b78a"),
        first_name="Cintia",
        last_name="Zanoni",
        email="cintia@gmail.com",
        role=[Role.role_2]
    ),
    User(
        id = UUID("2be75629-b4c5-4aa8-9a9c-9a854858379e"),
        first_name="Joana",
        last_name="Gomes",
        email="joana@gmail.com",
        role=[Role.role_3]
    ),
    
]

@app.get("/")
async def root():
    return {"message":"Olá, Devs"}

# Lista todos os usuarios
@app.get("/api/users")
async def get_users():
    return db;

#Obter um usuario
@app.get("/api/user/{id}")
async def get_user(id:UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message":"Usuário não encontrado!"}

# cadastrar usuario
@app.post("/api/users")
async def add_user(user:User):
    """
    Adiciona um usuário na base de dados
    - **id** : UUID
    - **first_name**:string
    - **lat_name**:string
    - **email**:string
    - **role**:Role
    """
    db.append(user)
    return {"id":user.id}

# atualizar usuario
@app.put("/api/user/{id}")
async def update_user(id:UUID, user_data:User):
    for user in db:
        if user.id == id:
            user.first_name = user_data.first_name
            user.last_name = user_data.last_name
            user.email = user_data.email
            user.role = user_data.role
            return {"message": "Usuário atualizado com sucesso!"}
    raise HTTPException(
        status_code = 404,
        detail= f"Usuário com o id {id} não encontrado!"
    )

#remover usuario
@app.delete("/api/user/{id}")
async def remove_user(id:UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail= f"Usuário com o id {id} não encontrado!"
    )
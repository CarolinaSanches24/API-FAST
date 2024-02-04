from pydantic import BaseModel;
from uuid import UUID, uuid4;
from typing import Optional, List;
from enum import Enum;

class Role(str, Enum):
    role_1 = "admin";
    role_2  = "aluna";
    role_3 = "instrutora";

class User(BaseModel):
    #cria randomicamente o id
    id:Optional[UUID]= uuid4();
    #nome
    first_name:str;
    #sobrenome
    last_name:str;
    email:str;
    #perfil
    role: List[Role];
    
    
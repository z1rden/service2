from pydantic import BaseModel

class AddUser(BaseModel):
    name: str
    surname: str
    email: str
    login: str
    hash_password: str

class DeleteUser(BaseModel):
    id: int

class UpdateUser(BaseModel):
    id: int
    parameter: str
    value: str
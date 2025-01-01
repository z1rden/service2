from fastapi import FastAPI
import grpc
from .generated import users_pb2
from .generated import users_pb2_grpc
from .models import AddUser, DeleteUser, UpdateUser
import os

app = FastAPI()
recommendations_host = os.getenv("GRPC_HOST", "localhost")

@app.get("/get_users")
async def get_users():
    with grpc.insecure_channel(f'{recommendations_host}:50051') as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        response = stub.GetUsers(users_pb2.GetUsersRequest(message='Получить список пользователей'))

    return response.message

@app.post("/add_user")
async def add_user(user: AddUser):
    with grpc.insecure_channel(f'{recommendations_host}:50051') as channel:
        stub = users_pb2_grpc.UsersStub(channel)

        new_user = users_pb2.User()
        new_user.name = user.name
        new_user.surname = user.surname
        new_user.email = user.email
        new_user.login = user.login
        new_user.hash_password = user.hash_password

        response = stub.AddUser(users_pb2.AddUserRequest(message='Добавить нового пользователя',
                                                     user=new_user))

    return response.message

@app.post("/delete_user")
async def delete_user(user: DeleteUser):
    with grpc.insecure_channel(f'{recommendations_host}:50051') as channel:
        stub = users_pb2_grpc.UsersStub(channel)

        id = user.id

        response = stub.DeleteUser(users_pb2.DeleteUserRequest(message='Удалить пользователя',
                                                               id=int(id)))

    return response.message

@app.post("/update_user")
async def update_user(user: UpdateUser):
    with grpc.insecure_channel(f'{recommendations_host}:50051') as channel:
        stub = users_pb2_grpc.UsersStub(channel)

        id = user.id
        parameter = user.parameter
        value = user.value

        response = stub.UpdateUser(users_pb2.UpdateUserRequest(message='Обновить пользователя',
                                                               id=int(id),
                                                               parameter=parameter,
                                                               value=value))

    return response.message


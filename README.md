  Папка service2 описывает gateway-сервис, отвечающий за взаимодействие между клиентом(пользователем) и grpc-сервером.
  В папке service2 лежит Dockerfile, по которому создается в дальнейшем контейнер gateway внутри docker-compose.yml, находящимся в папке service1.
  В папке service2 лежит requirements.txt, описывающий используемые библиотеки, необходимые для работы данного сервиса. Эти библиотеки автоматически устанавливаются в docker'e благодаря Dockerfile.
  
  В папке blueprint находится "основа", необходимая для работы данного сервиса.
  Директория blueprint/generated содержит в себе файлы, генерируемые при запуске:
    python3 -m grpc_tools.protoc --proto_path=blueprint/proto \
            --python_out=blueprint/generated \
            --grpc_python_out=blueprint/generated \
            blueprint/proto/*.proto
    по входящему Protobuffer файлу proto/users.proto, описывающий grpc-сервис.
  Файл bleprint/__main__.py необходим для запуска gateway-сервиса. В него импортируется экземпляр fastapi под названием app. 
  Файл blueprint/client.py описывает сам gateway-сервис: создается экземляр fastapi app, прописываются его ручки get_users, add_user, delete_user, update_user (согласно описанию grpc-сервиса), а также прописывается связь для взаимодойствия с портом grpc-сервера путем :
    recommendations_host = os.getenv("GRPC_HOST", "localhost") -  это необходимо для работы внутри docker'a
    with grpc.insecure_channel(f'{recommendations_host}:50051') as channel:
  Файл blueprint/models.py описывает типы json, которые отправляются на ручки gateway.

  Для общения с gateway-сервисом использовался postman. 
  Все возможные взаимодействия с gateway-сервисом:
  1. get на http://0.0.0.0:8000/get_users
  2. post на http://0.0.0.0:8000/add_user
     body:
     {
        "name": "Artem",
        "surname": "Kulagin",
        "email": "artemkulagin@yandex.ru",
        "login": "saintkulia",
        "hash_password": "aaa"
      }
  3. post на http://0.0.0.0:8000/delete_user
     body:
     {
        "id": 1
      }
  4. post на http://0.0.0.0:8000/update_user
     body:
     {
        "id": 3,
        "parameter": "hash_password",
        "value": "sdadasdas" 
      }

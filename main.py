from fastapi import FastAPI
from routes.user import user


description = """
Backend de Prueba con FastApi conectada a MongoDB🚀🦄🧺\U0001F440\U0001F947
## Usuarios


You will be able to:

* **Create users** 
* **Read users** 
* **Delete and Update**
"""

app = FastAPI(
    title="Test Backend",
    description=description,
    summary="Prueba de Crud con MongoDB una base para FARM Stack",
    version="0.0.1",
    contact={
        "name": "4rcmdl30",
        "email": "arcmdle0@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/license/mit/",
    },
)

app.include_router(user,prefix='/users',tags=['Usuarios'])

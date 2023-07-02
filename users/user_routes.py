"""Enrutador basico de FastApi para las url de usuarios,
solo incluye el Crud basico para administrar los usuarios    """
from fastapi import APIRouter, Response
from starlette.status import (
    HTTP_204_NO_CONTENT,
    HTTP_202_ACCEPTED,
    HTTP_201_CREATED,
    HTTP_302_FOUND,
)
from bson import ObjectId
from passlib.hash import pbkdf2_sha256
from config.db import conn
from users.user_models import User
from users.user_schema import user_entity, users_entity
from utils.user_prep import prepare_user_to_save


user = APIRouter()


@user.get("/", response_model=list[User])
def get_all_users():
    users = users_entity(conn.userdb.users.find())
    return users


@user.get("/{id}", response_model=User, status_code=HTTP_302_FOUND)
def get_one_user(id):
    user_found = user_entity(conn.userdb.users.find_one({"_id": ObjectId(id)}))
    return user_found


@user.post("/", response_model=User, status_code=HTTP_201_CREATED)
def create_user(user: User):
    new_user = prepare_user_to_save(user)
    new_oid = conn.userdb.users.insert_one(new_user).inserted_id
    user_created = conn.userdb.users.find_one({"_id": new_oid})
    return user_entity(user_created)


@user.put("/{id}", response_model=User, status_code=HTTP_202_ACCEPTED)
def update_user_by_id(id: str, user: User):
    user_to_update = prepare_user_to_save(user)
    conn.userdb.users.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": user_to_update}
    )
    return user_entity(conn.userdb.users.find_one({"_id": ObjectId(id)}))


@user.delete("/{id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(id: str):
    conn.userdb.users.find_one_and_delete({"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)

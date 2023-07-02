from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT,HTTP_202_ACCEPTED,HTTP_201_CREATED,HTTP_302_FOUND
from passlib.hash import pbkdf2_sha256
from bson import ObjectId
from config.db import conn
from models.user import User
from schemas.user import user_entity,users_entity

user = APIRouter()

@user.get('/',response_model=list[User])
def get_all_users():
    users = users_entity(conn.userdb.users.find())
    # print (users) debug
    return users
    
@user.get('/{id}',response_model=User,status_code=HTTP_302_FOUND)
def get_one_user(id):
    user_found = user_entity(conn.userdb.users.find_one({'_id':ObjectId(id)}))
    # Debug print(user_found)
    return user_found
@user.post('/', response_model=User,status_code=HTTP_201_CREATED)
def create_user(user:User):
    new_user = dict(user)
    new_user['password'] = pbkdf2_sha256.hash(new_user['password'])
    del new_user['id']
    new_oid = conn.userdb.users.insert_one(new_user).inserted_id
    user_created = conn.userdb.users.find_one({'_id':new_oid})
    return user_entity(user_created)

@user.put('/{id}', response_model=User, status_code=HTTP_202_ACCEPTED)
def update_user_by_id(id:str, user:User):
    user_to_update = dict(user)
    del user_to_update['id']
    user_to_update['password']= pbkdf2_sha256.hash(user_to_update['password'])
    conn.userdb.users.find_one_and_update({'_id':ObjectId(id)},{'$set':user_to_update})
    return user_entity(conn.userdb.users.find_one({'_id':ObjectId(id)})) 

@user.delete('/{id}', status_code=HTTP_204_NO_CONTENT)
def delete_user(id:str):
    conn.userdb.users.find_one_and_delete({'_id':ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
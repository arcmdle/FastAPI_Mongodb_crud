def user_entity(item) -> dict:
    return{
        'id':str(item['_id']),
        'full_name':item['full_name'],
        'email':item['email'],
        'password':item['password']
    }

def users_entity (entity) -> list:
        return [
            user_entity(item) for item in entity
        ]
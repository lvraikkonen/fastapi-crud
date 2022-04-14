# def userEntity(item) -> dict:
#     return {
#         "id": str(item["_id"]),
#         "name": item["name"],
#         "email": item["email"],
#         "password": item["password"],
#         "role": item["role"]
#     }

# def usersEntity(entity) -> list:
#     return [userEntity(item) for item in entity]


def serializeDict(item) -> dict:
    new_dict = {**{i: str(item[i]) for i in item if i=="_id"}, **{i: item[i] for i in item if i!="_id"}}
    return new_dict

def serializeList(entity) -> list:
    return [serializeDict(item) for item in entity]
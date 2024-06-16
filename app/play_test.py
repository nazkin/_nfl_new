from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    id: int
    name: Union[str, None]
    isActive: bool


user_1 = User(id=1, name="Bob", isActive=True)
user_2 = User(id=2, name="Dylan", isActive=True)
user_3 = User(id=1, name=None, isActive=True)
user_4 = User(id=3, name="Tom", isActive=True)

users = [user_1, user_2, user_3, user_4]

duplicates = []
for (i, user) in enumerate(users):
    id_one = user.id
    for (i_2, user_2) in enumerate(users):
        id_two = user_2.id
        if id_one == id_two and i != i_2:
            print(user_2)
            duplicates.append(user_2)

print(duplicates)

for d in duplicates:
    d.dict(exclude_none=True)

print(duplicates)

x = User(**duplicates[0], **duplicates[1])
print(x)

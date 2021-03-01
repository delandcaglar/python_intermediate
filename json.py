import json

print(json.__file__)


person = {"name": "delo", "age": 38, "city": "Ney York", "hasChildren": False,
  "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4,sort_keys=True)
# separators=(';', '= ' seperator anlaminda guzel isine yarayabilir
# sort_keys= True alfabetik yapiyo bu da baya rahatlatabiliyor
# print(personJSON)

with open("person.json", "w") as file:
    json.dump(person,file,indent=4,sort_keys=True)

person = json.loads(personJSON)
print("bu python object hali #false buyuk harfle")
print(person)

# fi le ise load string ise loads
# person = json.loads()


with open ('person.json', "r") as file:
    person = json.load(file)
    print(person)


class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def encode_user(o):
    if isinstance(o,User):
        return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not Json serializable')

user = User("Max", 27)
userJSON = json.dumps(user, default=encode_user)
print("son")
print(userJSON)

from json import  JSONEncoder
# ovewrite yapiyorsun indirdigin librarye
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance ( o, User ):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self,o)

user = User("Max", 27)

userJSON = json.dumps(user, cls=UserEncoder)
print("son1")
print(userJSON)


userJSON = UserEncoder().encode(user)
print('yeni_yontem')
print(userJSON)


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user  = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)


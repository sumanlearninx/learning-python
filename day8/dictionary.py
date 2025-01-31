# dictionary - data structure to store and retrieve key-values
# note : the data type of keys in dictionary must be necessarily immutable - int, string, tuple

user = {
    "username" : "suman1",
    "age" : 25,
    "password" : "12345",
    "is_verified" : True,
    "age" : 50
}
print(user) # {'username': 'suman1', 'age': 25, 'password': '12345', 'is_verified': True}

print(user["username"]) # suman1
print(user["password"]) # 12345
print(user["age"])

print(user.get("age")) # 25

# difference in accessing values by keys VS using get method

# print(user["address"]) # Keys Error
print(user.get("address")) # None
print(user.get("address", "not found")) # giving default value if key not found

# changing values
user["username"] = "suman.123"
print(user) # {'username': 'suman.123', 'age': 50, 'password': '12345', 'is_verified': True}


# deleting particular key value

del user["is_verified"]
print(user) # {'username': 'suman.123', 'age': 50, 'password': '12345'}

# pop - deletes key as well as return value
is_deleted = user.pop("age")
print(is_deleted) # 50
print(user) # {'username': 'suman.123', 'password': '12345'}

# keys, values, items

print(user.keys()) # dict_keys(['username', 'password'])
print(user.values()) # dict_values(['suman.123', '12345'])
print(user.items()) # dict_items([('username', 'suman.123'), ('password', '12345')])

# loop in dictionary

for key, value in user.items(): # user.keys(), user.values()
    print(f"{key} - {value}") # username - suman.123
                              # password - 12345


# dictionary comprehension

words = ["apple", "ball", "cat"]
a = {key : len(key) for key in words}
print(a) # {'apple': 5, 'ball': 4, 'cat': 3}

# nested dictionary

user_details = {
    "name":{
        "f_name":"suman",
        "l_name":"bhandari"
    },
    "age" : 30,
    "address":{
        "province" : "bagmati",
        "district" : "bkt"
    }
}

print(user_details["address"]["province"]) # bagmati 

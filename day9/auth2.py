# second way of authentication logic
# using dictionary where username is the key
import getpass

users = {
    "suman1":{
        "username":"suman1",
        "password":"password"
    },
    "ram101":{
        "usernam":"ram101",
        "password":"rampass"
    }
}

def signup(username, password):
    user = users.get(username)
    if user:
        print("Username already exists")
        return
    
    users[username]= {
        "username":username,
        "password":password
    }

    print("User registered successfully...")

def login(username, password):
    user = users.get(username)
    if not user:
        print("User not registered yet .. regitser first")
        return
    
    if user["password"] == password:
        print("User Login Success ")
    else:
        print("Invalid password ")
    
if __name__ == "__main__":
    username = input("Enter username : ")
    password = getpass.getpass("Enter password : ")

    # signup(username,password)
    login(username,password)


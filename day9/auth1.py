users = [
    {
        'username':'suman1',
        'password':'password'
    },
    {
        'username':'suman2',
        'password':'password'
    }
]

def signup(username, password):
    for user in users:
        if user['username'] == username:
            print(f"User with username {username} already exists")
            return
        
    users.append(
        {
            'username': username,
            'password': password
        }
    )

    print("User registration success")

def login(username, password):
    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                print("Login success !!")
            else:
                print("Invalid password")
            return

    print("Invalid username")


username = input("Enter username : ")
password = input("Enter password : ")

# signup(username, password)
login(username, password)
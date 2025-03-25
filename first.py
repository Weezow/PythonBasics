def yourdad(val):
    print(__name__)
    a = val
    b = val
    if a == 1 :
        print(a)
    elif a == 2: 
        print("ya moms nicca")
    else: 
        print("error!!!")

def callyourdad(var = 2):
    yourdad(val = var)
    print(var)

callyourdad(1)

l = [1, 2, 3]

t = tuple(1,2,3)

users = []

def user(username, password, email):
    return {
        "username" : username,
        "password" : password,
        "email" : email
    }

users.append(user("Ricardo", "abcd", "yo@gmail.com"))
users.append(user("Leo", "Weezow", "leo@gmail.com"))
users.append(user("test", "test", "leo@gmail.com"))
users.append(user("bruh", "bruh", "leo@gmail.com"))
users.append(user("Sike", "sike", "leo@gmail.com"))

print(users)    

for usr in 10:
    print(usr)
    if usr["username"] == "Leo":
        print(usr["email"])
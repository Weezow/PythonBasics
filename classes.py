class DataBase:
    def __init__(self, user, password):
        self.master = user
        self.master_password = password
        self.auth = self.check_auth()
        self.users = []

    def check_auth(self):
        if self.master == "Leo" and self.master_password == "FuckNigga":
            return True
        else:
            return False
        
    def add_user(self, username, password):
        if self.auth == True:
            print("User succesfully added")
            self.users.append([username, password])
        else:
            print("Not authorised")

my_obj = DataBase("Leo", "FuckNigga")
my_obj2 = DataBase("Ricardo", "Mr.Nigga")

my_obj.add_user("Ortet", "MegaNigga")
print(my_obj.users)

my_obj2.add_user("Felicia", "BitchNigga")
print(my_obj2.users)
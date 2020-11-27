from Database.database_connection import *


# function to register the first time user/admin
def first_time_admin_registration(usrname, passwd):
    db[admin_collection].insert({"admin_name": usrname, "password": passwd})
    print("success")


# function which will verify if the user is already registered or not
def verify_admin(usrname, passwd):
    if_user_exists = db[admin_collection].find_one({"admin_name": usrname, "password": passwd})
    if if_user_exists is not None:
        print("Found And Matched")
        return True
    else:
        print("User Not Found")
        return False

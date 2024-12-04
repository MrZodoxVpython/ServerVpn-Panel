from adminLogin import loginAdmin
from userLogin import loginUser
from userMenu import menuUser
from adminMenu import menuAdmin
def userLoginVerification(): 
    if loginUser():
        menuUser()
    else:
        print("Verification Failed")

def adminLoginVerification():
    if loginAdmin():
        menuAdmin()
    else:
        print("Verification Failed")
 
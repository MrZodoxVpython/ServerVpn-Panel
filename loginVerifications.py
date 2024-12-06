def userLoginVerification(): 
    if loginUser():
       menu.menuUser() 
    else:
        print("Verification Failed")

def adminLoginVerification():
    if loginAdmin():
        menuAdmin()
    else:
        print("Verification Failed")
 
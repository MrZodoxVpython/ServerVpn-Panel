from loginVerifications import userLoginVerification, adminLoginVerification
from userSignUp import userSignUp

def loginMenu():
    print("Choose Login")
    logindashboard = input("1. User login\n2. Sign Up\nMasukkan pilihan: ")
    if logindashboard == "1":
        userLoginVerification()
    if logindashboard == "2":
        userSignUp()
loginMenu()
from loginVerifications import userLoginVerification
import UA
#MENU
def loginMenu():
    print("Choose Login")
    logindashboard = input("1. User login\n2. Sign Up\nMasukkan pilihan: ")
    if logindashboard == "1":
        userLoginVerification()
    if logindashboard == "2":
        UA.userSignUp()

#SERVER LIST
def menuUser():
    print(f"Welcome to VPN PANEL! Your balance now is")
    # print(f"Total SSH Account: {totalSsh}")
    # print(f"Total Trojan Account: {totalTrojan}")
    # print(f"Total Vmess Account: {totalVmess}")
    # print(f"Total Vless Account: {totalVless}")
    print(f"Total orders per month")

def listServer():
    print("List Server SG!")

loginMenu()
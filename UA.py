userCredential = {
    "user1": "password1"
}
adminCredential = {
    "admin1": "password1"
}
dataServer = {
    "Vmess": {
        "15000": "INDONESIA"
    },
    "Trojan": {
        "25000": "SINGAPURA"
    },
    "Vless": {
        "10000": "INDONESIA"
    }
}
balance = 1500000
#MENU
def loginMenu():
    print("Choose Login")
    logindashboard = input("1. User login\n2. Sign Up\nMasukkan pilihan: ")
    if logindashboard == "1":
        userLoginVerification()
    if logindashboard == "2":
        userSignUp()

# Menu User
def menuUser():
    print(f"\nWelcome to VPN PANEL {loginUser()}! Your balance now is {balance}\n")
    # print(f"Total SSH Account: {totalSsh}")
    # print(f"Total Trojan Account: {totalTrojan}")
    # print(f"Total Vmess Account: {totalVmess}")
    # print(f"Total Vless Account: {totalVless}")
    print(f"Total orders per month")

# SERVER
def listServer():
    print("List Server SG!")

# User login verification
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

# Login user 
def loginUser():
    while True:
        print("\nUser Login") 
        username = input("Masukkan Username: ")
        if username == "$admin":
            adminLoginVerification()
        if username in userCredential:
            password = input("Masukkan password: ")
            length = len(userCredential[username])
            if password in userCredential[username] and len(password) == length:
                print("Login berhasil")
                return username
            else:
                print("Password salah")
        else:
            print("Username tidak terdaftar")

# User daftar
def userSignUp():
    username = input("Masukkan Username: ")
    if username not in userCredential:
        password = input("Masukkan Password: ") 
        userCredential[username][password]
        print(userCredential)
    else:
        print("Username tidak tersedia")

# Login admin        
def loginAdmin():
    while True:
        print("\nLogin Admin")
        username = input("Masukkan username: ")
        if username in adminCredential:   
            password = input("Masukkan password: ")
            length = len(adminCredential[username])
            if password in adminCredential[username] and len(password) == length:
                print("Login berhasil")
                return True, username
            else:
                print("Password salah")
        else:
            print("Username tidak terdaftar")    

# Menu admin 
def menuAdmin(): 
    print("===ADMIN MENU===")
    print("1. Account Credential")
    print("2. Server Vpn")
    print("3. Server Account Manager")
    pilihan = input("Masukan pilihan: ")
    if pilihan == "1":
        print("Credential menu")
        print("1. Create account")
        print("2. Read account")
        print("3. Update account")
        print("4. Delete account") 
        if pilihan == "1":
            userCredential["user1"]
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            userCredential[username] = password
            menuAdmin()
            if pilihan == "2":
                readCredential()
                print(userCredential)
                print(adminCredential)
            if pilihan == "3":
                print(userCredential)
                usr = input("Masukkan oke")
                print(usr)
            if pilihan == "4":
                userCredential
        if pilihan == "2":
            print(adminCredential)
    if pilihan == "2":
        print("Server vpn")
    if pilihan == "3":
        print("Server acc")

def readCredential():
    print(f"User Credential\n Username: {userCredential}\n Password: {userCredential["user1"]}")

loginMenu()
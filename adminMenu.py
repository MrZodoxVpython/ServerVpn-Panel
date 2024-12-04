from userLogin import userCredential
from adminLogin import adminCredential
def menuAdmin(): 
    print("===ADMIN MENU===")
    print("1. Account Credential")
    print("2. Server Vpn")
    print("3. Server Account Manager")
    pilihan = input("Masukan pilihan: ")
    if pilihan == "1":
        print("1. User credential")
        print("2. Admin credential")
        if pilihan == "1":
            print("User Credential menu")
            print("1. Create account")
            print("2. Read account")
            print("3. Update account")
            print("4. Delete account")
            print(userCredential)
            if pilihan == "1":
                userCredential["user1"]
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                userCredential[username][password]
            if pilihan == "2":
                readCredential()
                print(userCredential)
                print(adminCredential)
            if pilihan == "3":
                print(userCredential)
                usr = input
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

menuAdmin()
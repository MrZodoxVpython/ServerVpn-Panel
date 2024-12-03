userCredential = {
    "user1": "password1"
}
def loginUser():
    while True:
        print("User Login") 
        username = input("Masukkan Username: ")
        if username in userCredential:
            password = input("Masukkan password: ")
            if password in userCredential["user1"]:
                print("Berhasil Login")
                break
            else:
                print("Akun salah")
        else:
            print("Akun salah")
def userDashboard():
    pass
from loginVerifications import userLoginVerification
userCredential = {
    "user1": "password1"
}
def loginUser():
    while True:
        print("\nUser Login") 
        username = input("Masukkan Username: ")
        if username in userCredential:
            password = input("Masukkan password: ")
            length = len(userCredential[username])
            if username and password == "$admin":
                userLoginVerification()
            elif password in userCredential[username] and len(password) == length:
                print("Login berhasil")
                return True
            else:
                print("Password salah")
        else:
            print("Username tidak terdaftar")
adminCredential = {
    "admin1": "password1"
}
def loginAdmin():
    while True:
        print("\nLogin Admin")
        username = input("Masukkan username: ")
        if username in adminCredential:   
            password = input("Masukkan password: ")
            length = len(adminCredential[username])
            if password in adminCredential[username] and len(password) == length:
                print("Login berhasil")
                return True
            else:
                print("Password salah")
        else:
            print("Username tidak terdaftar")    
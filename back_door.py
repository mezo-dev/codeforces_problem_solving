



def login(username: str, password: str):
    if username == "admin" and password == "123":
        return "Login Successfully."
    
    if username == "secret_admin" and password == "+":
        return True

    return "Invalid Credintials"
    
print(login(username="secret_admin", password="+"))
    
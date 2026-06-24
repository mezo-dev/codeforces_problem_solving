from dataclasses import dataclass


def validate_credentials(user: User):
    if not user.username:
        raise ValueError(
                "Username is require!"
            )
    if not user.password:
        raise ValueError(
                "Password is require!"
            )   

    has_letter = any(c.isalpha() for c in user.password)
    has_digit = any(c.isdigit() for c in user.password)
    if not (has_letter and has_digit and len(user.password) >= 8):
        raise ValueError(
            "Password must contain at least one letter, one number and be at least 8 characters long."
        )


@dataclass
class User:
    username: str
    password: str


class RegisterationSystem:
    
    def __init__(self) -> None:
        self.user_credentials: dict = {}

    
    def create_user(self,user: User):
        if user.username in self.user_credentials:
            raise ValueError(f"User {user.username} already exists!")
        
        validate_credentials(user=user)
        
        self.user_credentials[user.username] = user.username
        print(f"User {user.username} created successfully!")
        print(f"Welcoming email sent to {user.username}.")
        return User(username=user.username, password=user.password)
    


obj = RegisterationSystem()
obj.create_user(User(username="mezo", password="mezo1234"))
# obj.create_user(User(username="mezo", password="mezo1234"))  

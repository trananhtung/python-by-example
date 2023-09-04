from fastapi import FastAPI
from bcrypt import checkpw

app = FastAPI()


class User:
    """User class."""

    def __init__(self, username: str, password: str):
        self.username = username
        self.passphrase = checkpw(password.encode(), password.encode())

    def __str__(self):
        return f"User: {self.username}"

    def __repr__(self):
        return f"User: {self.username}"


valid_users = {
    "user1": User("user1", "password1"),
}


@app.get("/ch01/index")
def index():
    """Index."""
    return {"message": "Welcome FastAPI Nerds"}


@app.get("/ch01/login/")
def login(username: str, password: str):
    """Login."""
    if user := valid_users.get(username) is None:
        return {"message": "user does not exist"}

    if checkpw(password.encode(), user.passphrase.encode()):
        return user

    return {"message": "invalid user"}


@app.post("/ch01/login/signup")
def signup(username: str, password: str):
    """Signup."""
    if valid_users.get(username) is None:
        user = User(username, password)
        valid_users[username] = user
        return user

    return {"message": "user already exists"}

from sqlalchemy.orm import Session
import bcrypt
from .models import User
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def register(db: Session, username, password):
    if db.query(User).filter(User.username == username).first():
        raise Exception("Username already taken")
    hashed = hash_password(password)
    user = User(username=username, password=hashed)
    db.add(user)
    db.commit()
    print(f"User {username} registered.")

def login(db: Session, username, password):
    user = db.query(User).filter(User.username == username).first()
    if user and check_password(password, user.password):
        return user
    else:
        return None

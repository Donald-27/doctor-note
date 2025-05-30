from sqlalchemy.orm import Session
import bcrypt
from models import User

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def register(db: Session, username, password, full_name, email):
    if db.query(User).filter(User.username == username).first():
        raise Exception("Username already taken")
    if db.query(User).filter(User.email == email).first():
        raise Exception("Email already registered")
    hashed = hash_password(password)
    user = User(
        username=username,
        password=hashed,
        full_name=full_name,
        email=email
    )
    db.add(user)
    db.commit()
    print(f"User {username} registered.")
    
def login(db: Session, username, password):
    user = db.query(User).filter(User.username == username).first()
    if user and check_password(password, user.password):
        return user
    else:
        return None

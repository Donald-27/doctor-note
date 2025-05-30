from sqlalchemy.orm import Session
import bcrypt
from models import User

def hash_password(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')  # Store as string in DB

def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def register(db: Session, username: str, password: str, full_name: str, email: str):
    if db.query(User).filter(User.username == username).first():
        raise Exception("Username already taken.")
    if db.query(User).filter(User.email == email).first():
        raise Exception("Email already registered.")
    
    hashed = hash_password(password)
    user = User(
        username=username,
        password=hashed,
        full_name=full_name,
        email=email
    )
    db.add(user)
    db.commit()
    print(f"User '{username}' registered successfully.")

def login(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if user and check_password(password, user.password):
        return user
    return None

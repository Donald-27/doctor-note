
from sqlalchemy import create_engine
from .models import Base
DATABASE_URL = "sqlite:///doctor_notes.db"
engine = create_engine(DATABASE_URL)

def create_database():
    Base.metadata.create_all(engine)
    print(" doctor_notes.db created and tables initialized.")

if __name__ == "__main__":
    create_database()

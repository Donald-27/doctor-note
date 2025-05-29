# doctor_note_cli/init_db.py

from sqlalchemy import create_engine
from .models import Base

# SQLite database URL (local file)
DATABASE_URL = "sqlite:///doctor_notes.db"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create all tables defined in models.py
def create_database():
    Base.metadata.create_all(engine)
    print(" doctor_notes.db created and tables initialized.")

if __name__ == "__main__":
    create_database()

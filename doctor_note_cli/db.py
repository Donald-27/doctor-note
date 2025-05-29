from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

engine = create_engine("sqlite:///doctor_notes.db")  # local sqlite file
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

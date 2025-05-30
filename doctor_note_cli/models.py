from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    notes = relationship("DoctorNote", back_populates="user")

class DoctorNote(Base):
    __tablename__ = "doctor_notes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    patient_name = Column(String, nullable=False)
    diagnosis = Column(String, nullable=False)
    date = Column(Date, default=datetime.date.today)
    notes_text = Column(String, nullable=False)
    prescription = Column(String, nullable=False)
    next_appointment = Column(Date, nullable=True)

    user = relationship("User", back_populates="notes")

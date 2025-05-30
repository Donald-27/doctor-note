# doctor_note_cli/cli.py
import click
from sqlalchemy.orm import Session
from db import Session, init_db
from auth import register, login
from models import DoctorNote
from pdf_generator import generate_pdf
import getpass

import datetime

current_user = None

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@click.group()
def cli():
    """Doctor Note CLI Application"""
    pass

@cli.command()
@click.argument('username')
@click.option('--email', prompt='Email', required=False)
@click.option('--full_name', prompt='Full Name', required=False)
def register_user(username, email, full_name):
    password = getpass.getpass("Password: ")
    db = next(get_db())
    try:
        register(db, username, password, full_name, email)
    except Exception as e:
        print(e)

@cli.command()
@click.argument('username')
def login_user(username):
    global current_user
    password = getpass.getpass("Password: ")
    db = next(get_db())
    user = login(db, username, password)
    if user:
        current_user = user
        print(f"Logged in as {username}")
    else:
        print("Invalid username or password")


@cli.command()
@click.option('--patient', prompt='Patient name')
@click.option('--diagnosis', prompt='Diagnosis')
@click.option('--notes', prompt='Notes')
@click.option('--prescription', prompt='Prescription', default='')
@click.option('--appointment', prompt='Next appointment (YYYY-MM-DD)', default='')
def add_note(patient, diagnosis, notes, prescription, appointment):
    global current_user
    if not current_user:
        print("Please login first!")
        return
    db = next(get_db())
    note = DoctorNote(
        user_id=current_user.id,
        patient_name=patient,
        diagnosis=diagnosis,
        notes_text=notes,
        prescription=prescription,
        next_appointment=datetime.datetime.strptime(appointment, "%Y-%m-%d").date() if appointment else None )
    db.add(note)
    db.commit()
    print("Note added successfully.")
@cli.command()
def list_notes():
    global current_user
    if not current_user:
        print("Please login first!")
        return
    db = next(get_db())
    notes = db.query(DoctorNote).filter_by(user_id=current_user.id).all()
    for note in notes:
        print(f"ID: {note.id} | Patient: {note.patient_name} | Diagnosis: {note.diagnosis} | Date: {note.date}")

@cli.command()
@click.argument('note_id', type=int)
def view_note(note_id):
    global current_user
    if not current_user:
        print("Please login first!")
        return
    db = next(get_db())
    note = db.query(DoctorNote).filter_by(id=note_id, user_id=current_user.id).first()
    if not note:
        print("Note not found.")
        return
    print(f"Patient: {note.patient_name}")
    print(f"Diagnosis: {note.diagnosis}")
    print(f"Date: {note.date}")
    print(f"Prescription: {note.prescription}")
    print(f"Next Appointment: {note.next_appointment}")
    print(f"Notes:\n{note.notes_text}")
@cli.command()
@click.argument('note_id', type=int)
def delete_note(note_id):
    global current_user
    if not current_user:
        print("Please login first!")
        return
    db = next(get_db())
    note = db.query(DoctorNote).filter_by(id=note_id, user_id=current_user.id).first()
    if not note:
        print("Note not found.")
        return
    db.delete(note)
    db.commit()

    print("Note deleted successfully.")


@cli.command()
@click.argument('note_id', type=int)

def export_pdf(note_id):
    global current_user
    if not current_user:
        print("Please login first!")
        return
    db = next(get_db())
    note = db.query(DoctorNote).filter_by(id=note_id, user_id=current_user.id).first()
    if not note:
        print("Note not found.")
        return
    filename = f"doctor_note_{note_id}.pdf"
    generate_pdf(note, filename)
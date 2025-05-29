import click
from sqlalchemy.orm import Session
from .db import Session, init_db
from .auth import register, login
from .models import DoctorNote
from .pdf_generator import generate_pdf
import getpass

current_user = None

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('username')
def register_user(username):
    password = getpass.getpass("Password: ")
    db = next(get_db())
    try:
        register(db, username, password)
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
def add_note(patient, diagnosis, notes):
    global current_user
    if not current_user:
        print("Please login first!")
        return
    db = next(get_db())
    note = DoctorNote(user_id=current_user.id, patient_name=patient,
                      diagnosis=diagnosis, notes_text=notes)
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
    print(f"Notes:\n{note.notes_text}")

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

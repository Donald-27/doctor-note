# Doctor Notes CLI
A doctors note website that implements both CLI and ORM
This is a simple command-line program to help doctors or medical staff manage patient notes easily. You can add, view, and save patient records including diagnosis, prescriptions, and appointments. 
It also lets you export your notes as PDF files for printing or sharing.

This tool is made with Python and uses a local database to keep your notes safe and organized.

What This Project Does
User Registration and Login:
Securely create user accounts with unique usernames. Passwords are safely stored using hashing, so that your data stays protected.

Add Doctor Notes:
Save detailed notes about each patient. You can enter the patient’s name, diagnosis, prescription, notes, and the date for the next appointment.

View Notes:
List all the notes you have added or view a single note by its ID. This helps keep track of patient histories easily.

Export to PDF:
Export any note as a PDF file. This makes it easy to share notes with others or keep printed copies. The PDF includes patient details, diagnosis, date, and your notes.

Simple Command-Line Interface:
Use easy commands in the terminal to manage everything without needing a complicated graphical interface.

Why Use This Project?
Simple and easy to use:
Runs on your computer with no internet needed. Works well for small clinics or individual doctors.

Secure:
Passwords are hashed using bcrypt to keep user accounts safe.

Organized Notes:
Stores notes in a local SQLite database, so you can quickly search and access patient info.

Portable:
Export notes to PDF for sharing or printing anytime.

Easy to Use:
Friendly CLI commands with prompts make it beginner-friendly.

How It Works
User Account System:

Register a new user with a username and password.

Login with your username and password.

Only logged-in users can add or view notes.

Database:

Uses SQLite, a simple file-based database stored locally as doctor_notes.db.

The database contains two tables: users and doctor_notes.

Each note is linked to the user who created it.

Adding Notes:

You enter patient name, diagnosis, notes, prescription, and next appointment date.

Notes are saved with the current date by default.

Viewing and Listing Notes:

View summary list of all your notes with patient names and diagnosis.

View full details of a specific note by ID.

PDF Export:

Converts notes to PDF format using the fpdf Python library.

Saved as files named like doctor_note_1.pdf, where 1 is the note ID.

Installation and Setup
1. Clone the Project
2. 
git clone https://github.com/donald-22/doctor_notes_cli.git
cd doctor_notes_cli
3. Create a Python Virtual Environment and Activate It
bash

python3 -m venv venv
source venv/bin/activate  # Linux/macOS

3. Install Dependencies
pip install -r requirements.txt

5. Initialize the Database
Run this once to create the database and tables:


Project Structure Overview
cli.py – The main command-line interface where all commands live (register, login, add note, etc.)

models.py – Defines the database tables for users and notes using SQLAlchemy

auth.py – Handles user registration, login, and password security with bcrypt

db.py – Sets up the database connection and session handling

pdf_generator.py – Creates PDFs from notes using FPDF

init_db.py – Script to create the database and tables

requirements.txt – List of Python packages needed

Dependencies
This project uses the following Python packages:

SQLAlchemy: To handle database operations easily

bcrypt: For secure password hashing

click: For building the command-line interface

fpdf: To generate PDF files

Python 3.8 or higher

Install all at once with:

bash
Copy code
pip install -r requirements.txt
Contact Information
If you want to reach out for help, feedback, or to contribute:

Email: kipropdonald27@gmail.com

GitHub: donald-27

Phone: +254724779523

License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.

Thank you for checking out the Doctor Notes CLI!
If you want to suggest features or fix bugs, please feel free to contact me.



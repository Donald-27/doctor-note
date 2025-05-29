from doctor_note.cli import cli
from doctor_note.db import init_db

def main():
    init_db()
    cli()

if __name__ == '__main__':
    main()

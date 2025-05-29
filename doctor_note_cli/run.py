from doctor_note_cli.cli import cli
from doctor_note_cli.db import init_db

def main():
    init_db()
    cli()

if __name__ == '__main__':
    main()

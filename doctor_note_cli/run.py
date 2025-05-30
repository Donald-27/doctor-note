from cli import cli

from db import init_db


def main():
    init_db()
    cli()

if __name__ == '__main__':
    main()

# database_setup.py

from models import create_tables
from database import engine

if __name__ == "__main__":
    create_tables(engine)
    print("Таблицы созданы успешно.")

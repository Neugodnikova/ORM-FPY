import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Загрузка переменных из .env файла
load_dotenv()

# Получение строки подключения из переменной окружения
DATABASE_URI = os.getenv("DATABASE_URI")

# Создание движка подключения
engine = create_engine(DATABASE_URI)

# Создание фабрики сессий
Session = sessionmaker(bind=engine)

def get_session():
    """Создает и возвращает новую сессию."""
    return Session()


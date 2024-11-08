from sqlalchemy.orm import sessionmaker
from database import engine
from models import Publisher

Session = sessionmaker(bind=engine)
session = Session()

# Проверка данных издателей
publishers = session.query(Publisher).all()
if publishers:
    for publisher in publishers:
        print(f"ID: {publisher.id}, Name: {publisher.name}")
else:
    print("Таблица издателей пуста.")
    
session.close()

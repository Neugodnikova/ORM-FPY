# load_fixtures.py

import json
from sqlalchemy.orm import sessionmaker
from database import engine
from models import Publisher, Shop, Book, Stock, Sale

Session = sessionmaker(bind=engine)
session = Session()

session.query(Sale).delete()
session.query(Stock).delete()
session.query(Book).delete()
session.query(Publisher).delete()
session.query(Shop).delete()
session.commit()



with open('fixtures/tests_data.json', 'r', encoding='utf-8') as fd:
    data = json.load(fd)


for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))

session.commit()
session.close()
print("Данные загружены успешно.")

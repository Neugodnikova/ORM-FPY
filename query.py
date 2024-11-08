from sqlalchemy import select
from models import Publisher, Book, Shop, Stock, Sale
from database import get_session

def get_sales_by_publisher(publisher_input):
    """Возвращает информацию о продажах книг указанного издателя."""
    session = get_session()

    # Определяем, искать по ID или по имени
    try:
        publisher_id = int(publisher_input)
        publisher_filter = Publisher.id == publisher_id
    except ValueError:
        publisher_filter = Publisher.name == publisher_input

    # Запрос для выборки данных
    query = (
        select(Book.title, Shop.name, Sale.price, Sale.date_sale)
        .join(Publisher, Publisher.id == Book.id_publisher)
        .join(Stock, Stock.id_book == Book.id)
        .join(Shop, Shop.id == Stock.id_shop)
        .join(Sale, Sale.id_stock == Stock.id)
        .where(publisher_filter)
    )

    # Выполнение запроса
    results = session.execute(query).all()
    session.close()
    return results

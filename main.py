from query import get_sales_by_publisher

def main():
    # Ввод имени или идентификатора издателя
    publisher_input = input("Введите имя или ID издателя: ")

    # Получение данных о продажах книг издателя
    results = get_sales_by_publisher(publisher_input)

    # Вывод данных
    if results:
        for title, shop_name, price, date_sale in results:
            print(f"{title} | {shop_name} | {price} | {date_sale.strftime('%d-%m-%Y')}")
    else:
        print("Нет данных для указанного издателя.")

if __name__ == "__main__":
    main()

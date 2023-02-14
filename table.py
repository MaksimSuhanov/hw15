import sqlite3
def main():
    again = 'да'
    while again == 'да':
        item_id = int(input('ID товара:'))
        item_name = input('Название товара')
        price = float(input('Цена:'))
        add_item(item_id, item_name, price)
        again = input('Добавить ещё позицию?')

def add_item(item_id, item_name, price):
    conn = sqlite3.connect('inventory3.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO Inventory (item_id, item_name, price) VALUES(?,?,?)''',
                (item_id, item_name, price))
    conn.commit()
    conn.close()
if __name__ == '__main__':
    main()
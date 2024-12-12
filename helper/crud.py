import sqlite3

class CRUD:
    def __init__(self, db_name='genesys.db'):
        self.db_name = db_name

    def connect(self):
        try:
            connection = sqlite3.connect(self.db_name)
            print("Connected to the database!")
            return connection
        except sqlite3.Error as e:
            print("Connection failed:", e)
            return None

    def create_price_table(self):
        query = '''CREATE TABLE IF NOT EXISTS price (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    item TEXT NOT NULL, 
                    quantity INTEGER NOT NULL, 
                    price REAL NOT NULL);'''

        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            print("Price table created successfully!")
            connection.close()

    def create_price(self, item, quantity, price):
        query = '''INSERT INTO price (item, quantity, price) 
                   VALUES (?, ?, ?)'''

        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query, (item, quantity, price))
            connection.commit()
            print("A new price record was inserted successfully!")
            connection.close()

    def read_price(self):
        query = '''SELECT * FROM price'''
        items = []

        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                item = {'id': row[0], 'item': row[1], 'quantity': row[2], 'price': row[3]}
                items.append(item)
            connection.close()

        return items

    def update_price(self, price_id, item, quantity, price):
        query = '''UPDATE price SET item = ?, quantity = ?, price = ? WHERE id = ?'''
        
        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query, (item, quantity, price, price_id))
            connection.commit()
            print(f"Price record with ID {price_id} was updated successfully!")
            connection.close()

    def delete_price(self, price_id):
        query = '''DELETE FROM price WHERE id = ?'''

        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query, (price_id,))
            connection.commit()
            print(f"Price record with ID {price_id} was deleted successfully!")
            connection.close()

    def create_customer_table(self):
        query = '''CREATE TABLE IF NOT EXISTS customer (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name TEXT NOT NULL, 
                    number TEXT NOT NULL, 
                    address TEXT NOT NULL, 
                    item_name TEXT NOT NULL, 
                    item_price INTEGER NOT NULL, 
                    item_number INTEGER NOT NULL, 
                    confirmed BOOLEAN NOT NULL);'''

        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            print("Customer table created successfully!")
            connection.close()

    def create_customer(self, name, number, address, item_name, item_price, item_number, confirmed):
        query = '''INSERT INTO customer (name, number, address, item_name, item_price, item_number, confirmed) 
                   VALUES (?, ?, ?, ?, ?, ?, ?)'''

        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query, (name, number, address, item_name, item_price, item_number, confirmed))
            connection.commit()
            print("A new customer record was inserted successfully!")
            connection.close()

    def read_customers(self):
        query = '''SELECT * FROM customer'''
        customers = []

        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                customer = {'id': row[0], 'name': row[1], 'number': row[2], 'address': row[3], 
                            'item_name': row[4], 'item_price': row[5], 'item_number': row[6], 'confirmed': row[7]}
                customers.append(customer)
            connection.close()

        return customers

    def update_customer(self, customer_id, name, number, address, item_name, item_price, item_number, confirmed):
        query = '''UPDATE customer SET name = ?, number = ?, address = ?, item_name = ?, item_price = ?, 
                   item_number = ?, confirmed = ? WHERE id = ?'''

        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query, (name, number, address, item_name, item_price, item_number, confirmed, customer_id))
            connection.commit()
            print(f"Customer record with ID {customer_id} was updated successfully!")
            connection.close()

    def delete_customer(self, customer_id):
        query = '''DELETE FROM customer WHERE id = ?'''

        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query, (customer_id,))
            connection.commit()
            print(f"Customer record with ID {customer_id} was deleted successfully!")
            connection.close()

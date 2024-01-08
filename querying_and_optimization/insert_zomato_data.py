import os
import pandas as pd
import mysql.connector

# Get credentials from environment variables
user = os.environ.get('db_user')
password = os.environ.get('db_pwd')

# Database connection parameters
db_config = {
    'host': 'localhost',
    'user': user,
    'password': password,
    'database': 'coding_challenge_db'
}

# Create a connection to the database
db = mysql.connector.connect(**db_config)
cursor = db.cursor()

# Drop existing tables if they exist
cursor.execute("DROP TABLE IF EXISTS order_items;")
cursor.execute("DROP TABLE IF EXISTS orders;")
cursor.execute("DROP TABLE IF EXISTS products;")
cursor.execute("DROP TABLE IF EXISTS stores;")
cursor.execute("DROP TABLE IF EXISTS cities;")

# Create new tables without AUTO_INCREMENT for id
cursor.execute("""
CREATE TABLE cities (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    created_at DATETIME
);
""")

cursor.execute("""
CREATE TABLE stores (
    id INT PRIMARY KEY,
    slug VARCHAR(255),
    created_at DATETIME,
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES cities(id)
);
""")

cursor.execute("""
CREATE TABLE products (
    id INT PRIMARY KEY,
    slug VARCHAR(255),
    price DECIMAL(10, 2),
    store_id INT,
    FOREIGN KEY (store_id) REFERENCES stores(id)
);
""")

cursor.execute("""
CREATE TABLE orders (
    id INT PRIMARY KEY,
    type VARCHAR(255) NOT NULL,
    store_id INT,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (store_id) REFERENCES stores(id)
);
""")

cursor.execute("""
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    PRIMARY KEY (order_id, product_id)
);
""")

def insert_data_from_csv(table_name, csv_file_path, batch_size=802):
    df = pd.read_csv(csv_file_path)
    df = df.astype('object')
    placeholders = ', '.join(['%s'] * len(df.columns))
    columns = ', '.join(df.columns)
    sql = f"INSERT IGNORE INTO coding_challenge_db.{table_name} ({columns}) VALUES ({placeholders})"

    for i in range(0, len(df), batch_size):
        print(f"Inserting batch {i//batch_size + 1} of {len(df)//batch_size + 1} into {table_name}")
        batch = [tuple(x) for x in df.iloc[i:i+batch_size].to_numpy()]
        try:
            # print(sql, batch)
            cursor.executemany(sql, batch)
            db.commit()
        except mysql.connector.Error as err:
            print("Error occurred:", err)

# Insert data into each table
insert_data_from_csv('cities', './datasets/cities.csv')
print('Cities inserted')
insert_data_from_csv('stores', './datasets/stores.csv')
print('Stores inserted')
insert_data_from_csv('products', './datasets/products.csv')
print('Products inserted')
insert_data_from_csv('orders', './datasets/orders.csv')
print('Orders inserted')
insert_data_from_csv('order_items', './datasets/order_items.csv')
print('Order items inserted')

# Close connection
cursor.close()
db.close()

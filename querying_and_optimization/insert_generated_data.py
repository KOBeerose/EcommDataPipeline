import os
import pandas as pd
import mysql.connector

# Get credentials from environemnt variables
user = os.environ.get('db_user')
password = os.environ.get('db_pwd')

# Database connection parameters
db_config = {
    'host': 'localhost',
    'user': user,
    'password': password,
    'database': 'coding_challenge_data'
}

# Create a connection to the database
db = mysql.connector.connect(**db_config)
cursor = db.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS countries (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS stores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    slug VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL,
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES countries(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    slug VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    store_id INT,
    FOREIGN KEY (store_id) REFERENCES stores(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(255) NOT NULL,
    store_id INT,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (store_id) REFERENCES stores(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    PRIMARY KEY (order_id, product_id)
);
""")

def clean_csv_duplicates(csv_file_path, subset):
    df = pd.read_csv(csv_file_path)
    df.drop_duplicates(subset=subset, inplace=True)
    return df

# Cleaning order_items CSV
order_items_cleaned = clean_csv_duplicates('./datasets/generated/order_items.csv', subset=['order_id', 'product_id'])

# Function to insert data from a CSV file into a table
def insert_data_from_csv(table_name, csv_file_path, batch_size=1000):
    df = pd.read_csv(csv_file_path)
    df = df.astype('object')
    placeholders = ', '.join(['%s'] * len(df.columns))
    columns = ', '.join(df.columns)
    sql = f"INSERT IGNORE INTO coding_challenge_data.{table_name} ({columns}) VALUES ({placeholders})"

    for i in range(0, len(df), batch_size):
        print(f"Inserting batch {i//batch_size + 1} of {len(df)//batch_size + 1} into {table_name}")
        batch = [tuple(x) for x in df.iloc[i:i+batch_size].to_numpy()]
        try:
            cursor.executemany(sql, batch)
            db.commit()
        except mysql.connector.Error as err:
            print("Error occurred:", err)

# Insert data into each table
insert_data_from_csv('countries', './datasets/generated/countries.csv')
print('Countries inserted')
insert_data_from_csv('stores', './datasets/generated/stores.csv')
print('Stores inserted')
insert_data_from_csv('products', './datasets/generated/products.csv')
print('Products inserted')
insert_data_from_csv('orders', './datasets/generated/orders.csv')
print('Orders inserted')
insert_data_from_csv('order_items', './datasets/generated/order_items.csv')
print('Order items inserted')

# close connection
cursor.close()
db.close()

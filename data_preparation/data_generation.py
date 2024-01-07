from faker import Faker
from datetime import datetime, timedelta
import random
import pandas as pd

# Initialize Faker
fake = Faker()

# Generate a list of 20 unique countries
countries = [fake.country() for _ in range(20)]
countries_df = pd.DataFrame({'name': countries, 'created_at': [datetime.now() for _ in countries]})

# Generate stores (assuming 500 stores for more substantial data)
stores_data = []
for _ in range(500):
    stores_data.append({
        'slug': fake.slug(),
        'created_at': datetime.now(),
        'country_id': random.choice(countries_df.index) + 1
    })
stores_df = pd.DataFrame(stores_data)

# Generate products (assuming each store has 100 products)
products_data = []
for store_id in range(1, 501):
    for _ in range(100):
        price = random.uniform(10, 500)
        products_data.append({
            'slug': fake.slug(),
            'price': price,
            'store_id': store_id
        })
products_df = pd.DataFrame(products_data)

# Generate orders (assuming each store has 1000 orders over 12 months)
start_date = datetime.now() - timedelta(days=365)
orders_data = []
for store_id in range(1, 501):
    for _ in range(1000):
        order_date = fake.date_time_between(start_date=start_date, end_date='now')
        orders_data.append({
            'type': random.choice(['Type1', 'Type2']),
            'store_id': store_id,
            'created_at': order_date
        })
orders_df = pd.DataFrame(orders_data)

# Generate order items (assuming 5 items per order on average)
order_items_data = []
for order_id in range(1, 500001):  # 500 stores * 1000 orders
    for _ in range(random.randint(1, 5)):
        product_id = random.randint(1, 50000)  # 500 stores * 100 products
        quantity = random.randint(1, 10)
        order_items_data.append({
            'order_id': order_id,
            'product_id': product_id,
            'quantity': quantity
        })
order_items_df = pd.DataFrame(order_items_data)

# Save data to CSV files
countries_df.to_csv('./datasets/generated/countries.csv', index=False)
stores_df.to_csv('./datasets/generated/stores.csv', index=False)
products_df.to_csv('./datasets/generated/products.csv', index=False)
orders_df.to_csv('./datasets/generated/orders.csv', index=False)
order_items_df.to_csv('./datasets/generated/order_items.csv', index=False)

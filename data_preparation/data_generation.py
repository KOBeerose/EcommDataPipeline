from faker import Faker
from datetime import datetime, timedelta
import random
import pandas as pd

# Initialize Faker for data generation
fake = Faker()

# Generate 20 unique countries
countries = [fake.country() for _ in range(20)]
countries_df = pd.DataFrame({'name': countries, 'created_at': [datetime.now() for _ in countries]})

# Generate data for 500 stores spread over the last 7 years
stores_data = []
for _ in range(500):
    created_at = fake.date_time_between(start_date='-7y', end_date='-4y')
    stores_data.append({
        'slug': fake.company(),
        'created_at': created_at,
        'country_id': random.choice(countries_df.index) + 1
    })
stores_df = pd.DataFrame(stores_data)

# Generate product data for each store
products_data = []
for store_id, store in enumerate(stores_data, 1):
    for _ in range(100):
        products_data.append({
            'slug': fake.word(),
            'price': random.uniform(10, 500),
            'store_id': store_id
        })
products_df = pd.DataFrame(products_data)

# Generate order data starting from the store's creation date
orders_data = []
for store_id, store in enumerate(stores_data, 1):
    num_orders = random.randint(500, 1500)  # Random number of orders for each store
    store_creation_date = store['created_at']  # Fetch the store's creation date
    for _ in range(num_orders):
        # Ensure order date is after the store's creation date and before the current date
        order_date = fake.date_time_between(start_date=store_creation_date, end_date='-4y')
        orders_data.append({
            'type': random.choice(['Online', 'In-Store', 'Pickup']),
            'store_id': store_id,
            'created_at': order_date
        })
orders_df = pd.DataFrame(orders_data)

# Generate order items data
order_items_data = []
for order_id in range(1, len(orders_data) + 1):
    for _ in range(random.randint(1, 5)):
        order_items_data.append({
            'order_id': order_id,
            'product_id': random.randint(1, 50000),
            'quantity': random.randint(1, 10)
        })
order_items_df = pd.DataFrame(order_items_data)

# Save generated data to CSV files
countries_df.to_csv('./datasets/generated/countries.csv', index=False)
stores_df.to_csv('./datasets/generated/stores.csv', index=False)
products_df.to_csv('./datasets/generated/products.csv', index=False)
orders_df.to_csv('./datasets/generated/orders.csv', index=False)
order_items_df.to_csv('./datasets/generated/order_items.csv', index=False)

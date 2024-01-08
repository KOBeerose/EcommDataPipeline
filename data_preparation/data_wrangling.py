import re
import pandas as pd
from datetime import datetime

# Load data
users_df = pd.read_csv('./datasets/zomato/users.csv', index_col=[0])
restaurants_df = pd.read_csv('./datasets/zomato/restaurant.csv', index_col=[0])
orders_df = pd.read_csv('./datasets/zomato/orders.csv', index_col=[0])
menu_df = pd.read_csv('./datasets/zomato/menu.csv', index_col=[0])
food_df = pd.read_csv('./datasets/zomato/food.csv', index_col=[0])

# Adjust price based on description
def extract_price(value):
    if pd.isnull(value) or value == '':
        return None
    str_value = str(value)
    match = re.search(r'\d+', str_value)
    if match:
        price = float(match.group())
        if 'FOR TWO' in str_value.upper():
            price /= 2
        return price
    else:
        return None 

# apply the function to the price column
menu_df.iloc[:, 4] = menu_df.iloc[:, 4].astype(str)
menu_df['price'] = menu_df.iloc[:, 4].apply(extract_price)

# Extract numeric part of 'menu_id'
menu_df['menu_id'] = menu_df['menu_id'].str.extract('(\d+)').astype('Int64')

# Changing r_id columns to Int
menu_df['r_id'] = menu_df['r_id'].astype('Int64')
orders_df['r_id'] = orders_df['r_id'].astype('Int64')


# ---------- cities ----------

# Create and clean cities DataFrame
cities_df = pd.DataFrame(restaurants_df['city'].unique(), columns=['name'])
cities_df['created_at'] = datetime.now()
cities_new = cities_df.dropna().drop_duplicates().reset_index(drop=True)

# Rearrange cities columns
cities_new['id'] = range(1, len(cities_df) + 1)
cities_new = cities_new[['id', 'name', 'created_at']]


# ---------- stores ----------

# Map city names to IDs
city_to_city_id = dict(zip(cities_df['name'], cities_new['id']))
restaurants_df['city_id'] = restaurants_df['city'].map(city_to_city_id)

# Prepare stores DataFrame
stores_new = restaurants_df[['id', 'name', 'city_id']].copy()
stores_new.rename(columns={'name': 'slug'}, inplace=True)
stores_new['created_at'] = datetime.now()

# Create slugs
def create_unique_slug(text, _id=None):
    text = str(text).lower()
    text = re.sub(r'\W+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return f"{text}-{_id}" if _id is not None else text

stores_new['slug'] = stores_new['slug'].apply(create_unique_slug)


# ---------- products ----------

# Merge menu and food DataFrames
products_df = menu_df.merge(food_df, left_on='f_id', right_on='f_id')

# Map r_id to store_id
r_id_to_store_id = dict(zip(restaurants_df['id'], stores_new['id']))
products_df['store_id'] = products_df['r_id'].map(r_id_to_store_id).astype('Int64')

# Prepare products DataFrame
products_new = products_df[['menu_id', 'item', 'price', 'store_id']].copy()
products_new.rename(columns={'menu_id': 'id', 'item': 'slug'}, inplace=True)
products_new['slug'] = products_new.apply(lambda x: create_unique_slug(x['slug'], x['id']), axis=1)


# ---------- orders ----------

# Merge orders and restaurants DataFrames
orders_restaurant_df = orders_df.merge(restaurants_df, left_on='r_id', right_on='id')

# Prepare orders DataFrame
orders_new = orders_restaurant_df[['cuisine', 'r_id', 'order_date']].copy()
orders_new.rename(columns={'cuisine': 'type', 'r_id': 'store_id', 'order_date': 'created_at'}, inplace=True)

# rearrage orders columns
orders_new['id'] = range(1, len(orders_new) + 1)
orders_new = orders_new[['id', 'type', 'store_id', 'created_at']]


# ---------- order_items ----------

# Merge orders and menu DataFrames
order_menu_df = pd.merge(orders_df, menu_df, left_index=True, right_index=True)

# Prepare order_items DataFrame
order_items_new = order_menu_df[['r_id_x', 'sales_qty']].copy()
order_items_new.rename(columns={'r_id_x': 'product_id', 'sales_qty': 'quantity'}, inplace=True)
order_items_new = order_items_new.dropna().reset_index(drop=True)

# rearrage order_items columns
order_items_new['order_id'] = range(1, len(order_items_new) + 1)
order_items_new = order_items_new[['order_id', 'product_id', 'quantity']]

# Save data to CSV
cities_new.to_csv('./datasets/cities.csv', index=False)
stores_new.to_csv('./datasets/stores.csv', index=False)
products_new.to_csv('./datasets/products.csv', index=False)
orders_new.to_csv('./datasets/orders.csv', index=False)
order_items_new.to_csv('./datasets/order_items.csv', index=False)

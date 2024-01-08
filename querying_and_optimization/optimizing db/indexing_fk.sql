-- 3. Optimize the DB using 

-- Indexing foreign keys in 'stores'
ALTER TABLE coding_challenge_data.stores
ADD INDEX idx_country_id (country_id);

-- Indexing foreign keys in 'orders'
ALTER TABLE coding_challenge_data.orders
ADD INDEX idx_store_id (store_id);

-- Indexing foreign keys in 'order_items'
ALTER TABLE coding_challenge_data.order_items
ADD INDEX idx_order_id (order_id),
ADD INDEX idx_product_id (product_id);

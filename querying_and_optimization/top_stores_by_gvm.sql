-- 2. Retrieve top stores with their corresponding GMV

-- Retrieves the top 20 stores based on the GMV work for both generated and zomato data.
SELECT 
    stores.id AS StoreID, 
    stores.slug AS StoreName, 
    SUM(products.price * order_items.quantity) AS GrossMerchandiseVolume
FROM 
    coding_challenge_data.stores AS stores
INNER JOIN 
    coding_challenge_data.orders AS orders ON stores.id = orders.store_id
INNER JOIN 
    coding_challenge_data.order_items AS order_items ON orders.id = order_items.order_id
INNER JOIN 
    coding_challenge_data.products AS products ON order_items.product_id = products.id
GROUP BY 
    stores.id
ORDER BY 
    GrossMerchandiseVolume DESC
LIMIT 20;

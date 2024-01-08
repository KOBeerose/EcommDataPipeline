-- 1. Retrieving city-specific GMV* data instead since zomato data is city based.

-- Calculate Total GMV for all the cities
SELECT 
    SUM(products.price * order_items.quantity) INTO @TotalGMV
FROM
    coding_challenge_db.order_items AS order_items
INNER JOIN 
    coding_challenge_db.products AS products ON order_items.product_id = products.id;

-- Calculate Gross Merchandise Volume specific for each city
-- Making sure to utilise indexed foreign keys to join the tables
SELECT 
    cities.name AS CityName, 
    SUM(products.price * order_items.quantity) AS GrossMerchandiseVolume,
    SUM(products.price * order_items.quantity)*100 / @TotalGMV AS GrossMerchandisePercentage
FROM 
    coding_challenge_db.cities AS cities
INNER JOIN 
    coding_challenge_db.stores AS stores ON cities.id = stores.city_id
INNER JOIN 
    coding_challenge_db.orders AS orders ON stores.id = orders.store_id
INNER JOIN 
    coding_challenge_db.order_items AS order_items ON orders.id = order_items.order_id
INNER JOIN 
    coding_challenge_db.products AS products ON order_items.product_id = products.id
GROUP BY 
    cities.name
ORDER BY 
    GrossMerchandiseVolume DESC;

-- 1. Retrieve country-specific GMV* data, along with corresponding percentages.

-- Calculate Total GMV for all the countries
SELECT 
    SUM(products.price * order_items.quantity) INTO @TotalGMV
FROM
    coding_challenge_data.order_items AS order_items
INNER JOIN 
    coding_challenge_data.products AS products ON order_items.product_id = products.id;

-- Calculate Gross Merchandise Volume specific for each country
-- Making sure to utilise indexed foreign keys to join the tables
SELECT 
    countries.name AS CountryName, 
    SUM(products.price * order_items.quantity) AS GrossMerchandiseVolume,
    SUM(products.price * order_items.quantity)*100 / @TotalGMV AS GrossMerchandisePercentage
FROM 
    coding_challenge_data.countries AS countries
INNER JOIN 
    coding_challenge_data.stores AS stores ON countries.id = stores.country_id
INNER JOIN 
    coding_challenge_data.orders AS orders ON stores.id = orders.store_id
INNER JOIN 
    coding_challenge_data.order_items AS order_items ON orders.id = order_items.order_id
INNER JOIN 
    coding_challenge_data.products AS products ON order_items.product_id = products.id
GROUP BY 
    countries.name
ORDER BY 
    GrossMerchandiseVolume DESC;

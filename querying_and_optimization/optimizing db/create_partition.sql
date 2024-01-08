-- 3. Optimize the DB (indexes, denormalization)

-- We could also partition by the created_at column in the orders table 
-- BUT it's NOT supported with Foreign Keys in MySQL
ALTER TABLE coding_challenge_data.orders 
PARTITION BY RANGE (YEAR(created_at)) (
    PARTITION p2017 VALUES LESS THAN (2017),
    PARTITION p2018 VALUES LESS THAN (2018),
    PARTITION p2019 VALUES LESS THAN (2019),
    PARTITION pmax VALUES LESS THAN MAXVALUE
);

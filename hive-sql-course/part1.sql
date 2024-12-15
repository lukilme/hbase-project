CREATE DATABASE IF NOT EXISTS course;

USE course;

CREATE TABLE IF NOT EXISTS my_table (
    col1 STRING,
    col2 ARRAY<STRING>,
    col3 STRING,
    col4 INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '.'
COLLECTION ITEMS TERMINATED BY ':'
LINES TERMINATED BY '\\n'
STORED AS TEXTFILE;

CREATE TABLE IF NOT EXISTS orders (
    cust_id VARCHAR(20),
    cust_name VARCHAR(50),
    odr_date STRING,
    ship_date STRING,
    courier VARCHAR(20),
    recvd_date STRING,
    returned VARCHAR(5),
    returned_date STRING,
    return_reason VARCHAR(50)
) 
row format delimited fields terminated by ","
lines terminated by "\n" 
stored as textfile;

SELECT * FROM orders;

LOAD DATA LOCAL INPATH '/opt/hive/metastore_db/assignment_create_table_2018.txt' INTO TABLE orders;

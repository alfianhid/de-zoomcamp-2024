-- Question 1: What is count of records for the 2022 Green Taxi Data?
-- Answer: 840,402
SELECT count(1) FROM `alfianhid-projects.de_zoomcamp_alfianhid.green_tripdata_2022`;

-- Question 2: Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
-- What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?
-- Answer: 0 MB for the External Table and 6.41MB for the Materialized Table
SELECT COUNT(DISTINCT(PULocationID)) FROM `alfianhid-projects.de_zoomcamp_alfianhid.green_tripdata_2022`;
SELECT COUNT(DISTINCT(PULocationID)) FROM `alfianhid-projects.de_zoomcamp_alfianhid.green_tripdata_2022_materialized`;

-- Question 3: How many records have a fare_amount of 0?
-- Answer: 1622
SELECT SUM(IF(fare_amount=0, 1, 0)) FROM `alfianhid-projects.de_zoomcamp_alfianhid.green_tripdata_2022`;

-- Question 4: What is the best strategy to make an optimized table in Big Query if your query will always order the results 
-- by PUlocationID and filter based on lpep_pickup_datetime? (Create a new table with this strategy)
-- Answer: Partition by lpep_pickup_datetime and cluster by PUlocationID
CREATE OR REPLACE TABLE `alfianhid-projects.de_zoomcamp_alfianhid.green_tripdata_2022_partitioned`
PARTITION BY lpep_pickup_datetime
CLUSTER BY PUlocationID AS (
  SELECT * FROM `alfianhid-projects.de_zoomcamp_alfianhid.green_tripdata_2022`
);

-- Question 5: Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)
-- Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from 
-- clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values?
SELECT DISTINCT PULocationID FROM `alfianhid-projects.de_zoomcamp_alfianhid.green_tripdata_2022_materialized`
WHERE lpep_pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30'; -- Answer: This query will process 12.82 MB when run. 

SELECT DISTINCT PULocationID FROM `alfianhid-projects.de_zoomcamp_alfianhid.green_tripdata_2022_partitioned`
WHERE lpep_pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30'; -- Answer: This query will process 1.12 MB when run.

-- Question 6: Where is the data stored in the External Table you created?
-- Answer: GCS

-- Question 7: It is best practice in Big Query to always cluster your data?
-- Answer: True

-- Question 8: Write a SELECT count(*) query FROM the materialized table you created. How many bytes does it estimate will be read? Why?
-- Answer: 0 B. Because this particular query is getting answered from the metadata tables, hence no cost. 
-- If you use some filter condition or use some actual column in the group by, you will incur cost.
SELECT COUNT(*) FROM `alfianhid-projects.de_zoomcamp_alfianhid.green_tripdata_2022_materialized`;

-- Create a Materialized Table from an External Table
CREATE OR REPLACE TABLE `alfianhid-projects.de_zoomcamp_alfianhid.green_tripdata_2022_materialized`
AS 
SELECT * FROM `alfianhid-projects.de_zoomcamp_alfianhid.green_tripdata_2022`;
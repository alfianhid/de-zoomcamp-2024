-- Create an External Table from GCS URI
CREATE OR REPLACE EXTERNAL TABLE `alfianhid-projects.de_zoomcamp_alfianhid.green_tripdata_2022`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://de_zoomcamp_alfianhid/green_tripdata/2022-*.parquet']
);
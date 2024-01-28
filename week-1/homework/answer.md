## Question 1. Knowing docker tags
Which tag has the following text? - *Automatically remove the container when it exits* 
- `--delete`
- `--rc`
- `--rmc`
- `--rm`
### Answer: `--rm`
### Approach: 

Read from `docker run --help` or [docker run | Docker Docs](https://docs.docker.com/engine/reference/commandline/run/ "docker run | Docker Docs")

## Question 2. Understanding docker first run
What is version of the package *wheel* ?
- 0.42.0
- 1.0.0
- 23.0.1
- 58.1.0 
### Answer: `0.42.0`
### Approach: 
```
docker run -it --entrypoint=bash python:3.10-slim
```
```
pip list
```

## Question 3. Count records
How many taxi trips were totally made on September 18th 2019? Tip: started and finished on 2019-09-18.\
Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.
- 15767
- 15612
- 15859
- 89009

### Answer: `15612`
### Approach:
```
docker network create de-zoomcamp-network
```
```
docker run --rm \ 
    -e POSTGRES_USER="alfianhid" \
    -e POSTGRES_PASSWORD="postgres" \
    -e POSTGRES_DB="ny_taxi_data" \
    -v $(pwd)/postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=de-zoomcamp-network \
    --name postgres-container \
    -t postgres:13
```
```
docker run --rm -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="pgadmin" \
    -e PGADMIN_CONFIG_WTF_CSRF_ENABLED="False" \
    -e PGADMIN_LISTEN_ADDRESS=0.0.0.0 \
    -e PGADMIN_LISTEN_PORT=5050 \
    -p 5050:5050 \
    --network=de-zoomcamp-network \
    --name pgadmin-container \
    --link postgres-container \
    -t dpage/pgadmin4
```
or if you want to use the docker-compose.yml file, you can run the following command (choose one):
```
docker compose up -d
```
```
docker build --no-cache -f Dockerfile -t ingest_nyc_taxi_data:1.0 .
```
```
docker run \
    --network=de-zoomcamp-network \
    -t ingest_nyc_taxi_data:1.0 \
    --user=alfianhid \
    --password=postgres \
    --db=ny_taxi_data \
    --host=postgres-container \
    --filepath=green_tripdata_2019-09.csv.gz \
    --table=green_tripdata_2019_09 \
    --url=https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz
```
```
docker run \
    --network=de-zoomcamp-network \
    -t ingest_nyc_taxi_data:1.0 \
    --user=alfianhid \
    --password=postgres \
    --db=ny_taxi_data \
    --host=postgres-container \
    --filepath=taxi+_zone_lookup.csv \
    --table=taxi_zone_lookup \
    --url=https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv
```
```
SELECT
	COUNT(1) AS total_taxi_trips_on_sept_18
FROM
	public.green_tripdata_2019_09
WHERE
	DATE(lpep_pickup_datetime) = '2019-09-18'
	AND DATE(lpep_dropoff_datetime) = '2019-09-18';
```
## Question 4. Largest trip for each day
Which was the pick up day with the largest trip distance.\
Use the pick up time for your calculations.

- 2019-09-18
- 2019-09-16
- 2019-09-26
- 2019-09-21

### Answer: `2019-09-26`
### Approach:
```
SELECT
	DATE(lpep_pickup_datetime) AS pick_up_date_with_largest_trip_distance
FROM
	public.green_tripdata_2019_09
GROUP BY
	DATE(lpep_pickup_datetime)
ORDER BY
	MAX(trip_distance) DESC
LIMIT
	1;
```
## Question 5. Three biggest pick up Boroughs
Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown.\
Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?
- "Brooklyn", "Manhattan", "Queens"
- "Bronx", "Brooklyn", "Manhattan"
- "Bronx", "Manhattan", "Queens" 
- "Brooklyn", "Queens", "Staten Island"

### Answer: `"Brooklyn", "Manhattan", "Queens"`
### Approach:
```
SELECT
    tzl."Borough"
FROM 
    public.green_tripdata_2019_09 gtd
JOIN 
    public.taxi_zone_lookup tzl ON gtd."PULocationID" = tzl."LocationID"
WHERE 
    DATE(gtd.lpep_pickup_datetime) >= '2019-09-18'
    AND tzl."Borough" != 'Unknown'
GROUP BY tzl."Borough"
HAVING SUM(gtd.total_amount) > 50000
ORDER BY total_amount_sum DESC
LIMIT 3;
```
## Question 6. Largest tip
For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?\
We want the name of the zone, not the id. Note: it's not a typo, it's `tip` , not `trip`
- Central Park
- Jamaica
- JFK Airport
- Long Island City/Queens Plaza

### Answer: `JFK Airport`
### Approach:
```
SELECT 
    tzl_dropoff."Zone" AS dropoff_zone_name
FROM 
    public.green_tripdata_2019_09 gtd
JOIN 
    public.taxi_zone_lookup tzl_pickup ON gtd."PULocationID" = tzl_pickup."LocationID"
JOIN 
    public.taxi_zone_lookup tzl_dropoff ON gtd."DOLocationID" = tzl_dropoff."LocationID"
WHERE 
    DATE(gtd.lpep_pickup_datetime) >= '2019-09-01'
    AND DATE(gtd.lpep_pickup_datetime) < '2019-10-01'
    AND tzl_pickup."Zone" = 'Astoria'
GROUP BY dropoff_zone_name
ORDER BY max_tip_amount DESC
LIMIT 1;
```
## Question 7. Creating Resources
After updating the main.tf and variable.tf files run:
```
terraform apply
```
Paste the output of this command into the homework submission form.

### Answer:
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

   google_bigquery_dataset.de_zoomcamp_alfianhid will be created
  + resource "google_bigquery_dataset" "de_zoomcamp_alfianhid" {
      + creation_time              = (known after apply)
      + dataset_id                 = "de_zoomcamp_alfianhid"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + effective_labels           = (known after apply)
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "asia-southeast1"
      + max_time_travel_hours      = (known after apply)
      + project                    = "alfianhid-projects"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = (known after apply)
    }

   google_storage_bucket.de_zoomcamp_alfianhid will be created
  + resource "google_storage_bucket" "de_zoomcamp_alfianhid" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "ASIA-SOUTHEAST1"
      + name                        = "de_zoomcamp_alfianhid"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.de_zoomcamp_alfianhid: Creating...\
google_storage_bucket.de_zoomcamp_alfianhid: Creating...\
google_storage_bucket.de_zoomcamp_alfianhid: Creation complete after 2s [id=de_zoomcamp_alfianhid]\
google_bigquery_dataset.de_zoomcamp_alfianhid: Creation complete after 4s [id=projects/alfianhid-projects/datasets/de_zoomcamp_alfianhid]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

### Approach:
```
gcloud auth application-default login
```
```
terraform init
```
```
terraform plan
```
```
terraform apply
```
-- Docs: https://docs.mage.ai/guides/sql-blocks
SELECT vendor_id, COUNT(vendor_id) FROM ny_taxi_data.green_taxi GROUP BY vendor_id;
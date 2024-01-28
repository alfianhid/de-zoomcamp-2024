variable "credentials" {
  type = string
  description = "Update to your GCP service account JSON file location"
  default     = ".credentials/alfianhid-projects-service-account.json"
}

variable "project" {
  type = string
  description = "Update to your GCP Project ID"
  default     = "alfianhid-projects"
}

variable "region" {
  type = string
  description = "Update to your desired region" 
  default     = "asia-southeast1-a"
}

variable "location" {
  type = string
  description = "Update to your desired location"
  default     = "asia-southeast1"
}

variable "bq_dataset_name" {
  type = string
  description = "Update to a unique BigQuery dataset name"
  default     = "de_zoomcamp_alfianhid"
}

variable "gcs_bucket_name" {
  type = string
  description = "Update to a unique GCS bucket name"
  default     = "de_zoomcamp_alfianhid"
}

variable "gcs_storage_class" {
  type = string
  description = "Update to a GCS bucket storage class"
  default     = "STANDARD"
}
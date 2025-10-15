variable "aws_region" { default = "ap-south-1" }
variable "project_suffix" { default = "demo" }
variable "raw_bucket_name" { default = "event-pipeline-raw-demo-12345" }
variable "lambda_zip_path" { default = "../lambda/ingest/build/ingest.zip" }

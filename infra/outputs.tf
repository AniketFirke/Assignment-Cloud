output "raw_bucket" {
  value = aws_s3_bucket.raw.bucket
}
output "lambda_name" {
  value = aws_lambda_function.ingest.function_name
}

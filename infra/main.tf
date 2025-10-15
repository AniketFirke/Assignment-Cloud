provider "aws" {
  region = var.aws_region
}

data "aws_iam_policy_document" "lambda_assume" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

resource "aws_s3_bucket" "raw" {
  bucket = var.project-sever
  acl    = "private"
  force_destroy = true
}

resource "aws_iam_role" "lambda_exec" {
  name               = "lambda_exec_role_${var.project_suffix}"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume.json
}

resource "aws_iam_role_policy_attachment" "lambda_basic" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "ingest" {
  function_name = "ingest_handler_${var.project_suffix}"
  filename      = var.lambda_zip_path
  handler       = "handler.lambda_handler"
  runtime       = "python3.11"
  role          = aws_iam_role.lambda_exec.arn
  source_code_hash = filebase64sha256(var.lambda_zip_path)
  environment {
    variables = {
      BUCKET = aws_s3_bucket.raw.bucket
    }
  }
}

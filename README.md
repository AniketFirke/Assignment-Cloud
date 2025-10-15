infra/ — contains Terraform files that define our infrastructure: S3 buckets, Lambda functions, IAM roles, and triggers.

lambda/ — holds the Python code for the Lambda functions, including the event ingestion and aggregation logic.

glue/ — contains a PySpark ETL job for large-scale data aggregation using AWS Glue.

ci/ — includes a GitHub Actions YAML workflow for automated testing and deployment.

docs/ — stores the research report and architecture justification documents.

And the README.md, which explains how to deploy and test the pipeline.”

```''```

# package lambda
cd lambda/ingest
mkdir -p build
cp handler.py build/
cd build
zip -r ../../build/ingest.zip .
cd ../../..

# deploy infra
cd infra
terraform init
terraform apply -auto-approve

```
event-driven-pipeline/
├─ infra/
│  ├─ main.tf
│  ├─ variables.tf
│  └─ outputs.tf
├─ lambda/
│  ├─ ingest/
│  │  ├─ handler.py
│  │  ├─ requirements.txt
│  │  └─ build/ingest.zip
│  └─ aggregate/
│     └─ handler.py
├─ glue/
│  └─ daily_agg.py
├─ ci/
│  └─ ci-cd.yml
├─ docs/
│  ├─ 1-Research-Report.docx
│  └─ 2-Architecture-Justification.pdf
└─ README.md

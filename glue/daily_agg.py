from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import to_date

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

raw_df = spark.read.json("s3://event-pipeline-raw-demo-12345/raw/")
# Example: group by device and date
agg = raw_df.groupBy("device").count()
agg.write.mode("overwrite").csv("s3://event-pipeline-raw-demo-12345/reports/daily-agg/")

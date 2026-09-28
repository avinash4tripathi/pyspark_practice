from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Reading JSON").getOrCreate()

import json

with open("/Workspace/Users/avinash.t@diggibyte.com/pyspark_practice/src/Data/employees.json", "r") as f:
    data = json.load(f)

df = spark.createDataFrame(data)
display(df)
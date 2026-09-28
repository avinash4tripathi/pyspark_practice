from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Reading CSV").getOrCreate()

df = spark.read.csv("file:/Workspace/Users/avinash.t@diggibyte.com/pyspark_practice/src/Data/employee.csv",header=True,inferSchema=True)

display(df)
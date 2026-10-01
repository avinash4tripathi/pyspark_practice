# length_calulate_string
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.appName("UDFExample").getOrCreate()

# Sample DataFrame
data = [("Avinash",), ("Spark",), ("PySpark",)]
df = spark.createDataFrame(data, ["name"])

# Define Python function
def string_length(s):
    return len(s)

# Register as UDF
length_udf = udf(string_length, IntegerType())

# Apply UDF
df2 = df.withColumn("name_length", length_udf(df["name"]))
df2.show()

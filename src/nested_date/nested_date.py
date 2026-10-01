from pyspark.sql.functions import from_json, explode
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType

from pyspark.sql import SparkSession

# Start Spark session
spark = SparkSession.builder.appName("NestedDataExample").getOrCreate()

# Example: Creating a DataFrame from JSON strings
json_data = [
    '{"customer_id":101,"name":"Avinash","orders":[{"product":"Laptop","price":60000},{"product":"Mouse","price":1000}]}'
]

df = spark.createDataFrame(json_data, "string").toDF("json_column")

schema = StructType([
    StructField("customer_id", IntegerType()),
    StructField("name", StringType()),
    StructField("orders", ArrayType(
        StructType([
            StructField("product", StringType()),
            StructField("price", IntegerType())
        ])
    ))
])

df2 = df.withColumn("data", from_json("json_column", schema))
df3 = df2.select("data.customer_id", "data.name", explode("data.orders").alias("order"))
df4 = df3.select("customer_id", "name", "order.product", "order.price")

# Display the final result
display(df4)

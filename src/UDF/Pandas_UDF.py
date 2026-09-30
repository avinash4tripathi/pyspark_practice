from pyspark.sql import SparkSession
import pandas as pd
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.appName("UDFExample").getOrCreate()

data = [("Avinash",), ("Spark",), ("PySpark",)]
df = spark.createDataFrame(data, ["name"])

@pandas_udf(IntegerType())
def string_length_pandas(s: pd.Series) -> pd.Series:
    return s.str.len()

df2 = df.withColumn("name_length", string_length_pandas(df["name"]))
df2.show()

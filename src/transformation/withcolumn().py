from pyspark.sql import SparkSession

path = "file:/Workspace/Users/avinash.t@diggibyte.com/pyspark_practice/src/Data/amazon_fires (1).csv"
print(path)

df = spark.read.csv(path, header=True, inferSchema=True)
#display(df.limit(20))

# Rename columns using withColumnRenamed
df_renamed = (df
    .withColumnRenamed("ano", "year")
    .withColumnRenamed("mes", "month")
    .withColumnRenamed("estado", "state")
    .withColumnRenamed("numero", "fire_count")
    .withColumnRenamed("encontro", "date")
)

print("Renamed columns:", df_renamed.columns)
display(df_renamed.limit(20))
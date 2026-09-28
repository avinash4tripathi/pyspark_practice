import os
print(os.getcwd())

path = "/Workspace/Users/avinash.t@diggibyte.com/pyspark_practice/amazon_fires (1).csv"
print(path)

df = spark.read.csv(path, header=True, inferSchema=True)
display(df.limit(20))

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

# Transform data inside columns using withColumn
from pyspark.sql.functions import regexp_extract, col, when

# 1. Extract number from "10 Fires" -> 10, "0 Fires" -> 0
df_clean = df_renamed.withColumn(
    "fire_count",
    regexp_extract(col("fire_count"), r"([0-9]+)", 1).cast("int")
)

# 2. Translate Portuguese month names to English
df_clean = df_clean.withColumn(
    "month",
    when(col("month") == "Janeiro", "January")
    .when(col("month") == "Fevereiro", "February")
    .when(col("month") == "Maro", "March")
    .when(col("month") == "Abril", "April")
    .when(col("month") == "Maio", "May")
    .when(col("month") == "Junho", "June")
    .when(col("month") == "Julho", "July")
    .when(col("month") == "Agosto", "August")
    .when(col("month") == "Setembro", "September")
    .when(col("month") == "Outubro", "October")
    .when(col("month") == "Novembro", "November")
    .when(col("month") == "Dezembro", "December")
    .otherwise(col("month"))
)

print("After data transformation:")
display(df_clean.limit(20))

# Save the cleaned data to a permanent table
df_clean.write.mode("overwrite").saveAsTable("workspace.default.amazon_fires")
print("Saved to table: workspace.default.amazon_fires")


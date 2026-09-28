from pyspark.sql.functions import when, col

df = spark.table("demo")
display(df)


df.sal = df.withColumn(
    "salary",
    (when(col("salary")>=80000,"High")
     .when(col("salary")>=50000,"Medium")
     .otherwise("Low"))
)
display(df.sal)

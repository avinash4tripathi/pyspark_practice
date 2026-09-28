from pyspark.sql.functions import when, col

df = spark.table("demo")
display(df)


df_sal = df.withColumn(
    "Salary_category",
    (when(col("salary")>=80000,"High")
     .when(col("salary")>=50000,"Medium")
     .otherwise("Low"))
)
display(df_sal) 

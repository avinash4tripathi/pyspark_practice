from pyspark.sql.functions import *

df = spark.table("demo")
display(df)

df_groupby = df.groupBy("department").agg(
    count("salary").alias("employee_count"),
    sum("salary").alias("total_salary"),
    avg("salary").alias("avg_salary"),
    max("salary").alias("max_salary"),
    min("salary").alias("min_salary")
)

display(df_groupby) 


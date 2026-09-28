from pyspark.sql.functions import *

df = spark.table("demo")
display(df)

df_groupby = df.groupBy("department").agg(
    sum("salary").alias("total_salary")
    )
display(df_groupby)
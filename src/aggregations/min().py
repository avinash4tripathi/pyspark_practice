from pyspark.sql.functions import *

df = spark.table("demo")
display(df)

df_groupby = df.groupBy("department").agg(
    min("salary").alias("Minumun_salary")
)
display(df_groupby)
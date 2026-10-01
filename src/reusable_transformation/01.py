# reusable_transformation/01.py
# Demonstrates reusable transformation using applyInPandas() with groupby()
# to compute avg and max salary per person, saving results to a Delta managed table.
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
import pandas as pd
claen_customer=[
    (1,"Avinsh","America",25000),
    (2,"Bhavesh","Canada",45000),
    (3,"Chetan","India",30000),
    (4,"Dhruv","Australia",50000),
    (5,"Eshaan","China",45000),
]

column_schema = StructType([
    StructField("id", IntegerType()),
    StructField("name", StringType()),
    StructField("city", StringType()),
    StructField("salary", IntegerType())
])

df = spark.createDataFrame(claen_customer, column_schema)
#display(df)

def calc_stats(pdf):
    return pd.DataFrame({
        "avg_salary": [pdf["salary"].mean()],
        "max_salary": [pdf["salary"].max()]
    })

result = df.groupby("name").applyInPandas(
    calc_stats,
    schema="avg_salary double, max_salary double"
)

display(result)

# Save as managed table (no LOCATION needed)
df.write.format("delta").mode("overwrite").saveAsTable("workspace.default.my_custom_df")



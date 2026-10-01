#Old record ko close karo and new record insert karo.
#Type 2 allows us to know which version of the customer record was valid at that time.
from pyspark.sql import Row
from pyspark.sql.functions import current_date, lit
data = [
    (101, "Avinash", "Lucknow"),
    (102, "Amit", "Delhi"),
    (103, "Priya", "Kanpur")
]

df = spark.createDataFrame(
    data,
    ["customer_id", "customer_name", "city"]
)

df.show()


scd_df = (
    df
    .withColumn("effective_start_date", current_date())
    .withColumn("effective_end_date", lit(None).cast("date"))
    .withColumn("is_current", lit(True))
)

scd_df.show()
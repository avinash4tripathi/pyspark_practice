from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from delta.tables import DeltaTable

spark = SparkSession.builder.appName("SCD_Examples").getOrCreate()

# Sample data
data = [(1, "Avinash", "Dubai"),
        (2, "Ravi", "Delhi"),
        (3, "Rajesh", "Mumbai"),
        (4, "Rakesh", "Bangalore")]

schema = StructType([
    StructField("id", IntegerType()),
    StructField("name", StringType()),
    StructField("city", StringType())
])

initial_df = spark.createDataFrame(data, schema)
display(initial_df)


# SCD TYPE 1: Simple Overwrite (No History)

type1_path = "/Volumes/workspace/default/employee_data/Type1_SCD"

# Step 1: Initial load
initial_df.write.format("delta").mode("overwrite").save(type1_path)
display(spark.read.format("delta").load(type1_path))

# Step 2: Update - Avinash moves to Noida
update_data = [(1, "Avinash", "Noida")]
update_df = spark.createDataFrame(update_data, schema)

# Type 1 Logic: Union new data + drop duplicates (keeps last)
type1_current = spark.read.format("delta").load(type1_path)
type1_updated = type1_current.union(update_df).dropDuplicates(["id"])
type1_updated.write.format("delta").mode("overwrite").save(type1_path)

# After update Dubai → Noida
#Old value LOST - only 1 row exists"
display(spark.read.format("delta").load(type1_path))


# SCD TYPE 2: Track Full History

type2_path = "/Volumes/workspace/default/employee_data/Type2_SCD"

# Step 1: Initial load with SCD columns
type2_initial = (initial_df
    .withColumn("start_date", lit("2024-01-01"))
    .withColumn("end_date", lit(None).cast("string"))
    .withColumn("is_current", lit(True)))

type2_initial.write.format("delta").mode("overwrite").save(type2_path)
#Initial load with SCD columns
display(spark.read.format("delta").load(type2_path))

# Step 2: Update - Avinash moves to Noida
update_data = [(1, "Avinash", "Noida")]
update_df = spark.createDataFrame(update_data, schema)

# Type 2 Logic using Delta Table API
type2_table = DeltaTable.forPath(spark, type2_path)

# 2a. Close old record (mark as inactive)
type2_table.update(
    condition="id = 1 AND is_current = true",
    set={"is_current": "false", "end_date": "'2024-06-01'"}
)

# 2. Insert new record
new_record = (update_df
    .withColumn("start_date", lit("2024-06-01"))
    .withColumn("end_date", lit(None).cast("string"))
    .withColumn("is_current", lit(True)))

new_record.write.format("delta").mode("append").save(type2_path)

#After update Dubai → Noida
#History PRESERVED - 2 rows exist for Avinash
display(spark.read.format("delta").load(type2_path).orderBy("id", "start_date"))


# SCD TYPE 3: Track Previous Value Only (Limited History)

type3_path = "/Volumes/workspace/default/employee_data/Type3_SCD"

# Step 1: Initial load (no previous columns yet)
initial_df.write.format("delta").mode("overwrite").save(type3_path)
print("\n1. Initial load:")
display(spark.read.format("delta").load(type3_path))

# Step 2: First update - Avinash moves to Noida
update_data = [(1, "Avinash", "Noida")]
update_df = spark.createDataFrame(update_data, schema)

# Type 3 Logic: Add previous_city and city_change_date columns
type3_current = spark.read.format("delta").load(type3_path)
type3_table = DeltaTable.forPath(spark, type3_path)

# Check if previous columns exist, if not add them
if "previous_city" not in type3_current.columns:
    type3_current = type3_current.withColumn("previous_city", lit(None).cast("string")) \
                                 .withColumn("city_change_date", lit(None).cast("string"))
    type3_current.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(type3_path)
    type3_table = DeltaTable.forPath(spark, type3_path)

# Update: move current city to previous_city, then update city
type3_table.update(
    condition="id = 1",
    set={
        "previous_city": "city",
        "city": "'Noida'",
        "city_change_date": "'2024-06-01'"
    }
)

#After first update Dubai → Noida
#Previous value stored in previous_city column
display(spark.read.format("delta").load(type3_path))

# Step 3: Second update - Avinash moves to Hyderabad
# Type 3: Overwrites previous_city (Dubai lost, only Noida remembered)
type3_table.update(
    condition="id = 1",
    set={
        "previous_city": "city",
        "city": "'Hyderabad'",
        "city_change_date": "'2024-09-01'"
    }
)

#3. After second update Noida → Hyderabad
#Dubai is LOST - only last change Noida is remembered
display(spark.read.format("delta").load(type3_path))

# COMPARISON
#Type1
display(spark.read.format("delta").load(type1_path).filter("id = 1"))

#Type2
display(spark.read.format("delta").load(type2_path).filter("id = 1").orderBy("start_date"))

#Type3
display(spark.read.format("delta").load(type3_path).filter("id = 1"))

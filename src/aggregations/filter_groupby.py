from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    count,
    countDistinct,
    sum,
    avg,
    min,
    max,
)

spark = SparkSession.builder.appName("Aggregations").getOrCreate()


employees = spark.read.csv(
    "/Workspace/Users/avinash.t@diggibyte.com/pyspark_practice/src/Data/employee.csv",
    header=True,
    inferSchema=True
)
display(employees.limit(10))
# COUNT
print("COUNT:")
employees.count()

# COUNT DISTINCT
print("COUNT DISTINCT:")
employees.select(countDistinct("department")).show()

# SUM
print("SUM:")
employees.select(sum("salary")).show()

# AVG
print("AVG:")
employees.select(avg("salary")).show()

# MIN
print("MIN:")
employees.select(min("salary")).show()

# MAX
print("MAX:")
employees.select(max("salary")).show()

# GROUP BY
print("GROUP BY:")
employees.groupBy("department").count().show()

# GROUP BY WITH MULTIPLE COLUMNS
print("GROUP BY WITH MULTIPLE COLUMNS:")
employees.groupBy("department", "city").count().show()

# FILTER AFTER AGGREGATION
print("FILTER AFTER AGGREGATION:")

result = (
    employees
    .groupBy("department")
    .agg(
        sum("salary").alias("total_salary")
    )
    .filter("total_salary > 100000")
    )

result.show()
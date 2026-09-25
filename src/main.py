import os
import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Force PySpark to use the installed Python interpreter on Windows.
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

# Start Spark
spark = SparkSession.builder.appName("SQL_pySpark").getOrCreate()

# Sample data
data = [(1, "Amit", "IT", 50000),
        (2, "Rahul", "HR", 40000),
        (3, "Advik", "IT", 70000),
        (4, "Priya", "Finance", 60000),
        (5, "Raj", "IT", 55000)]

columns = ["id", "name", "department", "salary"]

df = spark.createDataFrame(data, columns)

df.show()
df.createOrReplaceTempView("employees")

# Run first SQL Query
sql_result = spark.sql("""
    SELECT *
    FROM employees
    WHERE name = 'Amit'
""")
sql_result.show()

# SQL Where
sql_result = spark.sql("""
    SELECT *
    FROM employees
    WHERE salary > 50000
""")
sql_result.show()

# SQL Group by
sql_result = spark.sql("""
    SELECT
        department,
        AVG(salary) AS average_salary
    FROM employees
    WHERE salary > 50000
    GROUP BY department
""")
sql_result.show()

# Now writing the query in PySpark
from pyspark.sql.functions import avg
pyspark_result = (
    df
    .filter(df["salary"] > 50000)
    .groupBy("department")
    .agg(avg("salary").alias("average_salary"))
)

pyspark_result.show()

# Explain plan
sql_plan = spark.sql("""
    EXPLAIN
    SELECT
        department,
        AVG(salary) AS average_salary
    FROM employees
    WHERE salary > 50000
    GROUP BY department
""")

sql_plan.show(truncate=False)

# Lazy evaluation
filtered_df = df.filter(df["salary"] > 50000)  # transformation
filtered_df.explain()  # inspect the plan

# Action
filtered_df.show()
count = filtered_df.count()
print("Number of employees:", count)

spark.stop()
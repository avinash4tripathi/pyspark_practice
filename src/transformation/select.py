from pyspark.sql import SparkSession

#Start Spark Session
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

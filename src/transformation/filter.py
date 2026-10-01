from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Filter_SQL").getOrCreate()

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

filtered_df = df.filter(df["salary"] > 50000)
display(filtered_df)


from pyspark.sql import Row
#Old value overwrite karta hai.
customers = [
    (101, "Avinash", "Dubai"),
    (102, "Amit", "Delhi"),
    (103, "Priya", "Mumbai"),
    (104, "Rajesh", "Bangalore"),
    (105, "Priyanka", "Mumbai"),
    (106, "Ravi", "Delhi")
]

columns = ["customer_id", "customer_name", "city"]

df = spark.createDataFrame(customers, columns)
display(df)
updates = [
    (101, "Avinash","LA")
]

update_df = spark.createDataFrame(updates, columns)

display(update_df) 



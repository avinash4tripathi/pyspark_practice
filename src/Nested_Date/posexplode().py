from pyspark.sql.functions import posexplode

array = ["Avinash","Sql","Pandas"]

df = spark.createDataFrame([(array,)],["Data"])

df.select(posexplode('Data')).show()
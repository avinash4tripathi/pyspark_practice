from pyspark.sql.functions import explode

array = ["Avinash","Pysaprk","SQL"]
# Explode () "It converts the array into a row"
df = spark.createDataFrame([(array,)], ["data"])
df.select(explode(df.data)).show()
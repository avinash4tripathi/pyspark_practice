from pyspark.sql.window import Window
from pyspark.sql.functions import *

#Create a window
window = Window.partitionBy("department").orderBy(col("salary").desc())
from pyspark.sql.window import Window
from pyspark.sql.functions import *

emp_data = [(1,'manish',50000,'IT','m'),
(2,'vikash',60000,'sales','m'),
(3,'raushan',70000,'marketing','m'),
(4,'mukesh',80000,'IT','m'),
(5,'priti',90000,'sales','f'),
(6,'nikita',45000,'marketing','f'),
(7,'ragini',55000,'marketing','f'),
(8,'rashi',100000,'IT','f'),
(9,'aditya',65000,'IT','m'),
(10,'rahul',50000,'marketing','m'),
(11,'rakhi',50000,'IT','f'),
(12,'akhilesh',90000,'sales','m')]

emp_schema = ['id','name','salary','dept','gender']

emp_df = spark.createDataFrame(data=emp_data,schema=emp_schema)
emp_df = emp_df.select("id","name","salary","gender","dept")

#Window function - rank
window_df = Window.partitionBy("dept").orderBy("salary")
emp_df = emp_df.withColumn("rank",rank().over(window_df))
display(emp_df)

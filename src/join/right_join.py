from pyspark.sql import SparkSession

product_data = [(1, 'fanta',20),
(2, 'dew',22),
(5, 'sprite',40),
(7, 'redbull',100),
(12,'mazza',45),
(22,'coke',27),
(25,'limca',21),
(27,'pepsi',14),
(56,'sting',10)]

product_schema=['id','name','price']

product_df = spark.createDataFrame(product_data, product_schema)


sales_data = [(1,22,10,"01-06-2022"),
(1,27,5,"03-02-2023"),
(2,5,3,"01-06-2023"),
(5,22,1,"22-03-2023"),
(7,22,4,"03-02-2023"),
(9,5,6,"03-03-2023"),
(2,1,12,"15-06-2023"),
(1,56,2,"25-06-2023"),
(5,12,5,"15-04-2023"),
(11,12,76,"12-03-2023")]

sales_schema = ['customer_id','product_id','quantity','date_of_purchase']

sales_df = spark.createDataFrame(sales_data, sales_schema)

sales_df = sales_df.join(product_df, sales_df["product_id"] == product_df["id"], "right")

display(sales_df)
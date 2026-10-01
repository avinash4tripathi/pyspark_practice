# PySpark Practice 

This created to learn and practice Apache Spark with Python using PySpark. The work focused on setting up the local environment on Windows, creating Spark sessions, loading sample employee data, and running SQL and DataFrame queries to explore data analysis patterns.

##  Overview

The project demonstrates the following PySpark concepts:

- Creating a SparkSession and DataFrames from Python tuples
- Registering a DataFrame as a temporary SQL table
- Running SQL queries using Spark SQL
- Filtering rows with WHERE conditions
- Grouping by Department and calculating average salary
- Using DataFrame API operations instead of SQL
- Inspecting Spark execution plans with EXPLAIN
- Understanding lazy evaluation in Spark
- Reading CSV and JSON files with PySpark
- DataFrame transformations: `select()`, `filter()`, `drop()`, `withColumn()`, `withColumnRenamed()`, `when()`
- Aggregations: `count()`, `countDistinct()`, `sum()`, `avg()`, `min()`, `max()`, `groupBy()` with multiple columns
- All join types: inner, left, right, outer, full outer, cross, left semi, left anti
- Window functions: `row_number()`, `rank()`, `dense_rank()`, `lag()`, `lead()`, running totals with `rowsBetween()`
- Nested data: `explode()`, `posexplode()`, parsing JSON with `from_json()` and flattening struct/array fields
- UDFs: regular Python UDFs with `udf()` and vectorized Pandas UDFs with `@pandas_udf`
- Slowly Changing Dimensions (SCD): Type 1 (overwrite), Type 2 (full history), Type 3 (limited history) using Delta Table API
- Reusable transformations with `applyInPandas()` and saving to Delta tables


```

## Folders in this project

| Folder | Description |
| --- | --- |
| `data/` | Sample datasets in CSV and JSON format — Amazon fire data, employee data, and orders — used as input by reading, transformation, and aggregation scripts |
| `reading_practice/` | Reading data into Spark DataFrames from CSV files (`spark.read.csv()`), JSON files (`json.load()`), and existing Spark tables (`spark.table()`); also includes a `when()` salary categorization example |
| `transformation/` | Core DataFrame transformations — `select()`, `filter()`, `drop()`, `withColumn()`, `withColumnRenamed()`, `when()`, and `regexp_extract()` on employee and Amazon fires datasets; also includes the main `pyspark_practice.py` script with SQL queries, `EXPLAIN` plan, and lazy evaluation demo |
| `aggregations/` | Aggregation operations — `count()`, `countDistinct()`, `sum()`, `avg()`, `min()`, `max()`, `groupBy()` with single and multiple columns, and filtering after aggregation on employee and `demo` table data |
| `join/` | All PySpark join types demonstrated on customer and sales/product DataFrames — inner, left, right, outer, full outer, cross, left semi, and left anti joins |
| `window_function/` | Window functions on employee data — `row_number()`, `rank()`, `dense_rank()`, `lag()`, `lead()`, running totals with `rowsBetween()`, and demonstrations of `partitionBy()` vs `orderBy()` |
| `nested_date/` | Handling nested and array data — `explode()` to flatten arrays into rows, `posexplode()` for position-aware exploding, and `from_json()` to parse JSON strings with `explode()` to flatten nested struct/array fields |
| `udf/` | User Defined Functions — regular Python UDF with `udf()` and vectorized Pandas UDF with `@pandas_udf` decorator, both computing string length on a name column |
| `scd/` | Slowly Changing Dimensions — Type 1 (overwrite, no history), Type 2 (full history with `start_date`/`end_date`/`is_current` via Delta Table API), Type 3 (limited history with `previous_city` column), and a complete combined demo using Delta tables |
| `reusable_transformation/` | Reusable transformation using `applyInPandas()` with `groupby()` to compute avg and max salary per person, saving results to a Delta managed table |

## What was fixed today

While running the project, there were several environment and code issues that were debugged and resolved:

1. `python` command was not recognized in the Windows terminal.
2. PySpark was not installed in the environment.
3. PySpark needed an explicit Python executable on Windows using:
   - `PYSPARK_PYTHON`
   - `PYSPARK_DRIVER_PYTHON`
4. A DataFrame column access issue happened because the column names were inconsistent in case (`Salary` vs `salary`).
5. The final script was updated to use consistent lowercase column names so DataFrame and SQL operations work correctly.

## Setup instructions

From the project folder, run:

```bash
cd C:\Users\tripa\Desktop\pyspark
py -m pip install pyspark
py src/main.py
```

## Why `py` is used on Windows

On Windows, `py` is the standard Python launcher. It reliably finds the installed Python interpreter. This is why earlier commands like `python src/main.py` failed while `py src/main.py` worked.

## Main script behavior

The script does the following:

1. Creates a Spark session named `SQL_pySpark`
2. Creates a DataFrame with employee data
3. Displays all rows
4. Runs a SQL query for a specific employee name
5. Runs a WHERE query for salaries greater than 50000
6. Runs a grouped aggregation query for average salary by department
7. Repeats the same logic using the PySpark DataFrame API
8. Uses `EXPLAIN` to display the Spark logical plan
9. Demonstrates lazy evaluation and the count action

## Example data used

```python
[(1, "Amit", "IT", 50000),
 (2, "Rahul", "HR", 40000),
 (3, "Advik", "IT", 70000),
 (4, "Priya", "Finance", 60000),
 (5, "Raj", "IT", 55000)]
```

## Example SQL query used

```sql
SELECT department, AVG(salary) AS average_salary
FROM employees
WHERE salary > 50000
GROUP BY department
```

## Result summary

The final output confirms the project is working successfully and the average salary by department is correctly calculated.

## Notes

- Spark was successfully initialized on the local machine.
- The project is a learning setup for SQL + DataFrame operations in PySpark.
- The warnings about Hadoop and `winutils.exe` are common on Windows local setups and do not block basic execution for practice work.

## Current status

The project is working successfully in the terminal with the command:

```bash
py src/main.py
```

This confirms the PySpark demo, SQL queries, and DataFrame transformations are running correctly.

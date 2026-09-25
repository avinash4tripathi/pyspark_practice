# PySpark Practice Project

This created to learn and practice Apache Spark with Python using PySpark. The work focused on setting up the local environment on Windows, creating Spark sessions, loading sample employee data, and running SQL and DataFrame queries to explore data analysis patterns.

##  Overview

The project demonstrates the following concepts:

- Creating a SparkSession
- Creating a DataFrame from Python tuples
- Registering a DataFrame as a temporary SQL table
- Running SQL queries using Spark SQL
- Filtering rows with WHERE conditions
- Grouping by Department and calculating average salary
- Using DataFrame API operations instead of SQL
- Inspecting Spark execution plans with EXPLAIN
- Understanding lazy evaluation in Spark

## Files in this project

- `src/main.py` - Main PySpark script containing all examples and tests
- `src/avg.sql` - SQL file with a simple SELECT query example

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

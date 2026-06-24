from pyspark.sql import SparkSession
import os

# Fix Windows hostname issue
os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"
os.environ["SPARK_LOCAL_HOSTNAME"] = "localhost"

# Create Spark Session
spark = SparkSession.builder \
    .appName("EmployeeRDDAnalysis") \
    .master("local[*]") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .getOrCreate()

sc = spark.sparkContext

# Read CSV as RDD
rdd = sc.textFile("employee_data.csv")

# Remove header
header = rdd.first()
data = rdd.filter(lambda row: row != header)

# Split CSV rows
employees = data.map(lambda row: row.split(","))

# -------------------------------
# 1. Sort by salary descending
# -------------------------------
sorted_employees = employees.sortBy(
    lambda row: int(row[3]),
    ascending=False
)

print("\n===== Employees Sorted By Salary =====")
for emp in sorted_employees.collect():
    print(emp)

# -------------------------------
# 2. Department-wise total salary
# -------------------------------
dept_salary = employees.map(
    lambda row: (row[2], int(row[3]))
)

dept_totals = dept_salary.reduceByKey(
    lambda a, b: a + b
)

print("\n===== Department Salary Totals =====")
for dept in dept_totals.collect():
    print(dept)

# -------------------------------
# 3. Top 3 highest paid employees
# -------------------------------
top3 = sorted_employees.take(3)

print("\n===== Top 3 Highest Paid Employees =====")
for emp in top3:
    print(emp)

# Save top 3 to file
with open("top_3_employees.txt", "w") as f:
    for emp in top3:
        f.write(",".join(emp) + "\n")

print("\nTop 3 employees saved to file.")

spark.stop()
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("SalesDataFrameAnalysis") \
    .getOrCreate()

# Read CSV into DataFrame
df = spark.read.csv(
    "sales_data.csv",
    header=True,
    inferSchema=True
)

print("\n===== All Products Sorted By Sales =====")
sorted_df = df.orderBy(col("sales").desc())
sorted_df.show()

print("\n===== Top 3 Highest Selling Products =====")
top3 = sorted_df.limit(3)
top3.show()

print("\n===== Products With Sales > 80000 =====")
filtered_df = df.filter(col("sales") > 80000)
filtered_df.show()

# Save output as CSV
filtered_df.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("filtered_sales_output")

print("Filtered data saved successfully.")

spark.stop()
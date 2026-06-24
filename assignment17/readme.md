# PySpark DataFrame Sales Analysis

## Features

- Read CSV into DataFrame
- Sort products by sales descending
- Display top 3 products
- Filter products with sales > 80000
- Save filtered data as CSV

## Build

```bash
docker build -t sales-analysis .
```

## Run

```bash
docker run sales-analysis
```

## Output

Filtered CSV stored in:

filtered_sales_output/
FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    default-jdk \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pyspark

WORKDIR /app

COPY . .

CMD ["python", "sales_analysis.py"]
FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    wget \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

RUN pip install pyspark

WORKDIR /app

COPY . .

CMD ["python", "employee_analysis.py"]
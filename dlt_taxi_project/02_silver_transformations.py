# Databricks notebook source
import dlt
from pyspark.sql.functions import col, when, weekofyear, year, expr

# 1. Clean Silver Table
@dlt.table(
    name="silver_taxi_clean",
    comment="Silver: cleaned taxi data with suspicious ride flag"
)
def silver_taxi_clean():
    df = dlt.read("bronze_taxi")

    # Add suspicious flag: Example rule -> fare per km > 10 is suspicious
    df = df.withColumn(
        "suspicious_flag",
        when((col("trip_distance") > 0) & (col("fare_amount")/col("trip_distance") > 10), True).otherwise(False)
    )

    return df


# 2. Weekly Aggregates
@dlt.table(
    name="silver_weekly_agg",
    comment="Silver weekly aggregates: total trips, avg fare, suspicious count"
)
def silver_weekly_agg():
    df = dlt.read("silver_taxi_clean")

    agg = (
        df
        .withColumn("week", weekofyear(col("pickup_datetime")))
        .withColumn("year", year(col("pickup_datetime")))
        .groupBy("year", "week")
        .agg(
            expr("count(*) AS total_trips"),
            expr("avg(fare_amount) AS avg_fare"),
            expr("sum(CASE WHEN suspicious_flag THEN 1 ELSE 0 END) AS suspicious_rides")
        )
    )

    return agg

# Databricks notebook source
import dlt
from pyspark.sql.functions import col

@dlt.table(
    name="gold_top3_fares",
    comment="Gold: Top 3 highest fare rides with passenger & trip details"
)
def gold_top3_fares():
    df = dlt.read("silver_taxi_clean")
    return df.orderBy(col("fare_amount").desc()).limit(3)

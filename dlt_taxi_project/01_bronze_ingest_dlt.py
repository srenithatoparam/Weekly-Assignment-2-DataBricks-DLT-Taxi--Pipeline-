# Databricks notebook source
import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="bronze_taxi",
    comment="Bronze: raw taxi data imported from managed table"
)
@dlt.expect_or_drop("positive_distance", "trip_distance > 0")
def bronze_table():
    return spark.read.table("workspace.default.taxi_sample")

from pyspark import pipelines as dp

@dp.table(
    name="sales_bronze",
    comment="Raw sales data"
)
def sales_bronze():

    return (
        spark.read.format("jdbc")
        .option(
            "url",
            "jdbc:postgresql://46.250.172.124:5432/postgres"
        )
        .option("dbtable", "test_data_01")
        .option("user", "root")
        .option("password", "ki")
        .option("driver", "org.postgresql.Driver")
        .load()
    )
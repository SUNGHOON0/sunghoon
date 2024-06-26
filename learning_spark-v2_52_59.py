import findspark 
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import concat, expr, col


schema = "id INT, First STRING, Last STRING, Hits INT"

data = [
    [1, "Jules", "Damji", 4535],
    [2, "Brooke", "Wenig", 8908],
    [3, "Hanse", "Kim", 7659],
    [4, "Sunghoon", "Oh", 10568]
]

if __name__ == "__main__":
    spark = (SparkSession
             .builder
             .appName("hi")
             .getOrCreate())

    blogs_df = spark.createDataFrame(data, schema)
    blogs_df.show()

    blogs_df.select(expr("Hits*2")).show(2)
    #or
    blogs_df.select(col("Hits")*2).show(2)
    blogs_df.withColumn("Big Hitters", (expr("Hits > 10000"))).show()
    blogs_df.withColumn("AuthorsID", concat(col("First"), col("Last"), col("Id"))) \
            .select("AuthorsID") \
            .show(4)
    
    blogs_df.select(expr("Hits")).show(2)

    blogs_df.sort(col("Id").desc()).show()

    from pyspark.sql import Row 
    blog_row = Row(4, "Sunghoon", "Oh", 10568)
    print(blog_row[1])

    rows = [Row("Sunghoon Oh", "Seoul"), Row("Hanse Kim", "Ulsan")]
    authors_df = spark.createDataFrame(rows, ["Authors", "State"])
    authors_df.show()
    
    
           
            
    

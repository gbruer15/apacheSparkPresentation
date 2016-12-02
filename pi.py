from __future__ import print_function
import sys
from random import random
from operator import add


from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("PythonPi").getOrCreate()

    # Use two partitions (threads) by default
    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2

    # Each partition will perform approximately f about 100000 times
    n = 100000 * partitions

    # This function throws a dart within the unit square and returns 1 if it lands 
    # in the unit circle
    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 < 1 else 0

    # Have the specified number of partitions perform the map operation on n 
    # values, using the function f(), and then add those values up.
    count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)

    # count is the number of darts that landed in the unit circle. Using area 
    # ratios, approximately count = (pi/4) * n darts should land in the unit circle.
    # That gives pi = 4*count/n
    print("Pi is roughly %f" % (4.0 * count / n))

    spark.stop()
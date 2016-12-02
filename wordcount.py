from __future__ import print_function

import sys
from operator import add


from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()


    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    # lines = sc.textFile(sys.argv[1])

    # map each line to a list of words that make up the line
    # map each word to a tuple of that word and the number 1
    # reduce each tuple using addition, grouping by the word
    counts = lines.flatMap(lambda line: line.split(' ')) \
                  .map(lambda word: (word, 1)) \
                  .reduceByKey(add)

    # Now actually do it?
    output = counts.collect()

    # Print out the results
    for (word, count) in output:
        print("%s: %i" % (word, count))

    spark.stop()


# text_file = sc.textFile("hdfs://...")
# counts = text_file.flatMap(lambda line: line.split(" ")) \
#              .map(lambda word: (word, 1)) \
#              .reduceByKey(lambda a, b: a + b)
# counts.saveAsTextFile("hdfs://...")
from __future__ import print_function
import sys
from operator import add
from pyspark.sql import SparkSession

def line_tokenize(line):
    s = re.sub(r'[^\w\s]','',s)
    return re.split(r'\s*', s)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    

    # spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()
    #
    #
    #
    #
    # lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    # # lines = sc.textFile(sys.argv[1])
    #
    # # map each line to a list of words that make up the line
    # # map each word to a tuple of that word and the number 1
    # # reduce each tuple using addition, grouping by the word
    # counts = lines.flatMap(lambda line: line.split(' '))
    # print(counts)
    #
    #             #   .map(lambda word: (word, 1)) \
    #             #   .reduceByKey(add)
    #
    # # # Now bring those results all back to the master process
    # # output = counts.collect()
    # #
    # # # Print out the results
    # # for (word, count) in output:
    # #     print("%s: %i" % (word, count))
    #
    # spark.stop()

from __future__ import print_function
import sys
import random
from pyspark import SparkConf, SparkContext
import collections

def create_file(n=10000,minval=0,maxval=10):
    f = open('nums.txt', 'w')
    for i in xrange(n): f.write('%d\n' % random.randint(minval,maxval))    
    f.close()

def main():

    # Create the file
    create_file(n=10000,minval=0,maxval=10)

    # Setup the "app".
    conf = SparkConf().setMaster("local").setAppName("counter")
    sc = SparkContext(conf = conf)

    # Define the RDD
    lines = sc.textFile('nums.txt')
    
    # Define the transormation - convert each line to an int.
    vals = lines.map(lambda x: int(x))

    # Apply an action to be executed in parallel.
    result = vals.countByValue()

    print(result.items()) # Prints [(0,#), (1,#), ...]

if __name__ == "__main__": main()
    

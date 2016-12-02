---
title: "COSC462 Final Project: Apache Spark"
author: Alex Klibisz, Grant Bruer
date: 12/2/16
geometry: margin=0.6in
header-includes:
  - \hypersetup{colorlinks=false,
            urlcolor=blue,
            allbordercolors={0 0 0},
            pdfborderstyle={/S/U/W 0.5}}
---

## Disclaimer

This information is basically a summary from the two references given at the bottom. 

## What is Apache Spark?

- Framework for parallel processing of data
- Supported in Java, Python, Scala, and R
- A great use for it is MapReduce operations

## What does it mean to MapReduce?

- Map: For a list of things, map each thing to a value.
- Reduce: Combine those values into a single value

The mapping part is trivially parallelizable by sharing the mapping work among different nodes. 

The reduce part requires coordination between nodes, but it is farily easily solved.

Thus MapReduce is easily scalable.


## But I thought MapReduce from Hadoop already does that?

Yes, MapReduce does that, but Spark does it a little different

- Spark keeps things in memory, while MapReduce keeps things on disk
- Spark is made to be easier to develop on
- Has machine learning algorithms built in
- Lazy evaluation means Spark can optimize operations automatically

## Running Spark

- Interactive python interpreter: `./bin/pyspark --master local[2]`
- Any spark program : `./bin/spark-submit <program> <program args>`

## Hello, World!!


```
spark = SparkSession.builder.appName("HelloWorld").getOrCreate()
nums = spark.sparkContext.parallelize(range(1, 10))
helloList = nums.map(lambda n: "Hello, World %d!\n" % n)
combinedHello = helloList.reduce(lambda s1, s2: s1 + s2)
print(combinedHello)
```


## Real Stuff

A Spark application has a master/driver program that runs parallel operations on a cluster.

Spark is built to manage resilient distributed dataset (RDD), which is "a collection of elements partitioned across the nodes of the cluster that can be operated on in parallel." (From Spark programming guide)

The general strategy goes like this: The master program partitions a dataset across a cluster by creating an RDD. Then, each node in the cluster performs some operation on its data, and the results from all the nodes are combined.


### Resilient Distributed Dataset (RDD)
- Created from interpreting a file or in-memory dataset
- Automatically recovers from node failures
- Programs perform transformations and actions on RDDs

Creating from file: `distributedFile = sc.textFile("data.txt")`

- RDD is an array of lines partitioned across multiple nodes

Creating from in-memory dataset: `distributedDataset = sc.parallelize([1, 2, 3, 4])`

Both of these have an optional second argument that says how many partitions to cut the data into. If not specified, the number of partitions is automatically guessed.


### Example MapReduce Operation Step By Step

```
# Create RDD of lines in file
lines = sc.textFile("data.txt")

# Map the data from a line to the length of a line
lineLengths = lines.map(lambda line: len(line))

# Add up all the line lengths
totalLength = lineLengths.reduce(lambda length1, length2: length1 + length2)

# Get length of longest line
maxLength = lineLengths.reduce(lambda a, b: a if a > b else b)

print ("Total line lengths: " + totalLengths)
print ("Max line length: " + maxLength)
```

#### Notes on Example
- Lazy: the first two commands don't do any actual computation; they just tell Spark what you want to do. Spark waits until you ask for a result before doing any computation, so nothing is done until the reduce actions.

- Caching: since we use lineLengths twice, it would be good if Spark cached those values after the first run. We should add `lineLengths.cache()` to let Spark know we'll reuse that transformation.


### RDD Operations

#### Transformations

Transforms one distributed dataset to another distributed dataset. These can be done in parallel easily after partitioning the initial dataset. 

Examples: map, filter, union, reduceByKey.

#### Actions

Gets a result from a distributed dataset. This returns some value to the master process. 

Examples: count, reduce, collect, saveAsTextFile.


Lazy evaluation means that nothing is distributed or computed until an Action is performed, at which point Spark can make some optimizations for that specific Action.



### Caching RDD
- Speeds up future operations on it




## Shared Variables

### Broadcast Variable

- Read-only
- Used automatically for each stage
- Should be used explicitly if needed across multiple stages

### Accumulator

- Can only be added to
- Only the master process can read the value



## Shuffles? May be too much information. We'll think about it.
- Some operations cause a distributed dataset to be moved around. For instance, `reduceByKey` combines values for a single key into a single key-value pair. One node might not have all the values for a given key, so it needs to communicate with other nodes to get the values it needs. Thus, the data needs to be shuffled around in order for all the reduced key-value pairs to be calculated.
- Expensive
- May spill to disk
- Intermediate files saved to disk until RDD is garbage-collected (when all references to it are gone)




## Reference Links

- http://spark.apache.org/docs/latest/quick-start.html
- http://spark.apache.org/docs/latest/programming-guide.html
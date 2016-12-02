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

## What is Apache Spark?

- Framework for parallel processing of data
- Supported in Java, Python, Scala, and R
- A great use for it is MapReduce operations

## What does it mean to MapReduce?

- Map: For a list of things, map each thing to a value.
- Reduce: Combine those values into a single value

The mapping part is trivially parallelizable by sharing the mapping work among different nodes. 

The reduce part requires coordination between nodes, but it is farily easily solved.


## But I thought MapReduce from Hadoop already does that?

## Yes, MapReduce does that, but Spark does it a little different

- Spark keeps things in memory, while MapReduce keeps things on disk
- Spark is made to be easier to develop on
- Has machine learning algorithms built in
- Some fourth thing

## Running Spark

- Interactive python interpreter: `./bin/pyspark --master local[2]`
- Any spark program : `./bin/spark-submit <program> <program args>`

## Hello, World!!

```
TBD
```


## Reference Links

- http://spark.apache.org/docs/latest/quick-start.html


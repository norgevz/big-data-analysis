import os
import sys
os.environ["PYSPARK_SUBMIT_ARGS"]='pyspark-shell'
os.environ["PYSPARK_PYTHON"]='python3'
os.environ["PYSPARK_DRIVER_PYTHON"]='python3'
os.environ["SPARK_HOME"]='/opt/cloudera/parcels/SPARK2/lib/spark2/'

spark_home = os.environ.get('SPARK_HOME', None)
if not spark_home:
    raise ValueError('SPARK_HOME environment variable is not set')
sys.path.insert(0, os.path.join(spark_home, 'python'))
sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.10.6-src.zip'))
os.environ["PYSPARK_PYTHON"] = 'python3'
exec(open(os.path.join(spark_home, 'python/pyspark/shell.py')).read())

import re
from pyspark.sql.functions import udf
from pyspark.sql.types import *
import pyspark.sql.functions as f

@f.udf(ArrayType(StringType()))
def parse_article(text):
    try:
#        article_id, text = line.rstrip().split('\t', 1)
#        text = re.sub("^\W+|\W+$", "", text, flags=re.UNICODE)
        words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
        words = [x.lower() for x in words]
        ids = [i for i in range(1, len(words)) if words[i-1] == "narodnaya"]
        return ["narodnaya_" + words[i] for i in ids]
    except ValueError as e:
        return []

log_schema = StructType(fields=[
    StructField("id", StringType()),
    StructField("text", StringType())
])
wiki = spark.read.csv("hdfs:///data/wiki/en_articles_part", schema=log_schema, sep="\t").cache()

wiki = wiki.withColumn("words_list", parse_article("text"))
ans = wiki.select(f.explode("words_list").alias("word")).groupBy("word").count().orderBy("word").collect()


for (word, c) in ans:
    print(word + "\t" + str(c))


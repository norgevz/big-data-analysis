
OUT_DIR="task1_"$(date +"%s%6N")
FINAL_OUT_DIR="final_task1_"$(date +"%s%6N")
NUM_REDUCERS=8

hdfs dfs -rm -r -skipTrash ${OUT_DIR} > /dev/null
hdfs dfs -rm -r -skipTrash ${FINAL_OUT_DIR} > /dev/null

yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapred.jab.name="Streaming permCount" \
    -D mapreduce.job.reduces=${NUM_REDUCERS} \
    -files mapper.py,reducer.py \
    -mapper "python mapper.py" \
    -reducer "python reducer.py" \
    -input /data/wiki/en_articles \
    -output ${OUT_DIR} > /dev/null \



yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	-D mapreduce.partition.keycomparator.options="-k2,2nr" \
	-D mapreduce.partition.keypartitioner.options="-k1,1" \
	-D stream.num.map.output.key.fields=2 \
    -D mapred.jab.name="Final stage" \
    -D mapreduce.job.reduces=${NUM_REDUCERS} \
    -files head_reducer.py \
    -mapper "cat" \
    -reducer "python head_reducer.py" \
    -input ${OUT_DIR} \
    -output ${FINAL_OUT_DIR} > /dev/null \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat ${FINAL_OUT_DIR}/* | sort -rnk2,2 | head -n 10




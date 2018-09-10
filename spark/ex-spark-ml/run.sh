#! /usr/bin/env bash

OUT_DIR="task1_"$(date +"%s%6N")
NUM_REDUCERS=8

hdfs dfs -rm -r -skipTrash ${OUT_DIR} > /dev/null

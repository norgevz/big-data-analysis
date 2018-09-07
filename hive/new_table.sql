add jar /opt/cloudera/parcels/CDH/jars/hive-contrib-1.1.0-cdh5.12.1.jar;
add jar /opt/cloudera/parcels/CDH/jars/hive-serde-1.1.0-cdh5.12.1.jar;

USE ad_hsp201807;

DROP TABLE IF EXISTS SerDeExample;

CREATE EXTERNAL TABLE SerDeExample (
	ip STRING,
	date STRING,
	request STRING,
	responseCode STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.contrib.serde2.RegexSerDe'
WITH SERDEPROPERTIES (
"input.regex" = '^(\\S*)\\t\\t\\t(\\d{8})\\S*\\t(\\S*)\\t.*$'
)
STORED AS TEXTFILE
LOCATION '/data/user_logs/user_logs_S';

select * from SerDeExample limit 10;

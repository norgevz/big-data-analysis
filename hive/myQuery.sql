ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-contrib.jar;

USE ad_hsp201807;

DROP TABLE IF EXISTS Subnets;

CREATE EXTERNAL TABLE Subnets (
    ip STRING,
    mask STRING
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY  '\t'
STORED AS TEXTFILE
LOCATION '/data/subnets/variant1';

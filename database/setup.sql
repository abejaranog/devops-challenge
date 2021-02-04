 CREATE USER devops WITH SUPERUSER PASSWORD 'psql';

 CREATE DATABASE devops;
 \c devops

 CREATE TABLE air_quality(
    TIMEINSTANT TIMESTAMP,
    ID_ENTITY TEXT,
    SO2      FLOAT(48),
    NO2       FLOAT(48),
    CO         FLOAT(48),
    O3 FLOAT(48),
    PM10 FLOAT(48),
    PM2_5 FLOAT(48)
);

COPY air_quality
FROM '/tmp/airq.csv' DELIMITER ',' CSV HEADER;
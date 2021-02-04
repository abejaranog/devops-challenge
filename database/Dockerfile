FROM postgres:alpine
COPY environment_airq_measurand.csv /tmp/airq.csv
COPY *.sql /docker-entrypoint-initdb.d/
ADD setup.sql /docker-entrypoint-initdb.d
RUN chmod a+r /docker-entrypoint-initdb.d/*
EXPOSE 5432
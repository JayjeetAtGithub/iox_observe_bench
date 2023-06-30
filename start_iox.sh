#!/bin/bash
set -e

echo "Starting IOx"
../influxdb_iox/target/release/influxdb_iox run all-in-one -vv --catalog-dsn=sqlite:///tmp/iox_catalog.sqlite --router-http-bind=0.0.0.0:8080 --querier-grpc-bind=0.0.0.0:8082
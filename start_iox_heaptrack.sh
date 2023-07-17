#!/bin/bash
set -e

echo "Starting IOx with Heaptrack"
export INFLUXDB_IOX_ROUTER_HTTP_BIND_ADDR=0.0.0.0:8080
export INFLUXDB_IOX_QUERIER_GRPC_BIND_ADDR=0.0.0.0:8082

cd iox/
cargo with 'heaptrack' -- run --profile=release --no-default-features -- run all-in-one --exec-mem-pool-bytes 10737418240 -vv

#!/bin/bash
set -e

echo "Starting IOx"
export INFLUXDB_IOX_ROUTER_HTTP_BIND_ADDR=0.0.0.0:8080
export INFLUXDB_IOX_QUERIER_GRPC_BIND_ADDR=0.0.0.0:8082

cd iox/
cargo run --no-default-features --features=heappy --profile=release run all-in-one -vv

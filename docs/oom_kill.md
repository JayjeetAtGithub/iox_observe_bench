# Reproducing the Issue

1. Run IOx (release) with heaptrack enabled in a terminal using `cargo-with`.
```bash
export INFLUXDB_IOX_ROUTER_HTTP_BIND_ADDR=0.0.0.0:8080
export INFLUXDB_IOX_QUERIER_GRPC_BIND_ADDR=0.0.0.0:8082

cargo with 'heaptrack' -- run --profile=release --no-default-features -- run all-in-one --exec-mem-pool-bytes 10737418240 -vv
```

2. Run IOx sql in a second terminal.
```bash
./target/release/influxdb_iox sql
```

Then execute the following SQL query,

```bash
> use otel_otel;
> SELECT "trace_id", MAX("time") AS t FROM 'spans' WHERE "service.name" = 'frontend' AND "time" >= to_timestamp(1688713200000000000) AND "time" <= to_timestamp(1689537120000000000) GROUP BY "trace_id" ORDER BY t DESC LIMIT 20;
```

3. Wait for IOx to get killed by the OOM killer and a heaptrack `.gz` file to be generated.

4. Open the `.gz` files with the `heaptrack_gui` to generate the flamegraph. Some already generated profiles and flamegraphs can be found in the `heaptrack_profiles` directory.
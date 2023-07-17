## Issue Description

On making a `Find Traces` query from Jaegar UI, which makes a query like this (), IOx ends up using all of the available DRAM and eventually gets killed the OOM killer in Linux. 

## System Specifications

* OS: Debian 11 Bullseye
* DRAM: 32GB
* IOx version: 33e41fc5cbca33dbd6021c0556b281488883b547
* Rust version: 1.70.0 (90c541806 2023-05-31)
* Cargo version: 1.70.0 (ec8a8a0ca 2023-04-25)

## Reproducing the Issue

1. Install dependencies.
```bash
cargo install cargo-with
sudo apt-get install heaptrack heaptrack-gui
```

2. Download the dataset from [here](https://drive.google.com/drive/folders/1nd3FaZXlsvM8JelXHJjHZONDzvB9UeVs?usp=sharing) into your `/path/to/home/.influxdb_iox` directory.

3. Run IOx (release) with heaptrack enabled in a terminal using `cargo-with`.
```bash
export INFLUXDB_IOX_ROUTER_HTTP_BIND_ADDR=0.0.0.0:8080
export INFLUXDB_IOX_QUERIER_GRPC_BIND_ADDR=0.0.0.0:8082

cargo with 'heaptrack' -- run --profile=release --no-default-features -- run all-in-one --exec-mem-pool-bytes 10737418240 -vv
```

4. Run IOx sql in a second terminal.
```bash
./target/release/influxdb_iox sql
```

Then execute the following SQL query,

```bash
> use otel_otel;
> SELECT "trace_id", MAX("time") AS t FROM 'spans' WHERE "service.name" = 'frontend' AND "time" >= to_timestamp(1688713200000000000) AND "time" <= to_timestamp(1689537120000000000) GROUP BY "trace_id" ORDER BY t DESC LIMIT 20;
```

5. Wait for IOx to get killed by the OOM killer and a heaptrack `.gz` file to be generated.

6. Open the `.gz` files with the `heaptrack_gui` to generate the flamegraph. Some already generated profiles and flamegraphs can be found in the `heaptrack_profiles` directory. Alternatively, you can also generate the flamegraph in `.svg` file using `heaptrack_print`,

```bash
heaptrack_print -f heaptrack.app.pid.gz -a -F stacks.txt
git clone https://github.com/brendangregg/FlameGraph
cd FlameGraph/
./flamegraph.pl --title "heaptrack" --colors mem --countname allocations < stacks.txt > heaptrack.app.pid.svg
```

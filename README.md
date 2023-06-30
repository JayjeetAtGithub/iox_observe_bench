## IOx Observability Benchmark

### Running Instructions

1. Start IOx
```bash
./start_iox.sh
```

2. Start Jaegar, HotRODs, and Jaegar InfluxDB
```bash
./start_jaegar.sh
```

3. Generate traces using HotRODs
```bash
python3 gen_trace.py [seed]
watch ./watch_spans.sh
```

4. Execute queries
```bash
python3 query.py
```


### Benchmarks

1. Num traces: 1, 10, 100, 1000, 10000, 100000, 1000000
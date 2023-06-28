## IOx Observability Benchmark

### Running Instructions


1. Start IOx
```bash
cargo run -- run all-in-one -vv --catalog-dsn=memory --router-http-bind=0.0.0.0:8080 --querier-grpc-bind=0.0.0.0:8082
```

2. Start Jaegar, HotRODs, and Jaegar InfluxDB
```bash
docker compose --file demo/docker-compose.yml --project-directory . up --abort-on-container-exit --remove-orphans
```

3. Generate traces using HotRODs
```bash
python3 gen_trace.py
```


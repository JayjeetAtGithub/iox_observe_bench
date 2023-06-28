from flightsql import FlightSQLClient

import pandas
import time

if __name__ == "__main__":
    client = FlightSQLClient(
        host="localhost",
        port="8082",
        insecure="true",
        token="xxx",
        metadata={"bucket-name": "otel_otel"},
    )

    s = time.time()
    info = client.execute('SELECT "trace_id", MAX("time") AS t FROM "spans" WHERE spans."service.name" = \'frontend\' AND "time" >= to_timestamp(1687960353941000000) AND "time" <= to_timestamp(1687963953941000000) GROUP BY "trace_id" ORDER BY t DESC LIMIT 1000')
    reader = client.do_get(info.endpoints[0].ticket)
    table = reader.read_all()
    e = time.time()
    print(table)
    print("\n\n")
    print("Read ", table.num_rows, " rows in ", e - s, " secs")

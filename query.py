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

    for i in range(10):
        s = time.time()
        query = 'SELECT "trace_id", MAX("time") AS t FROM \'spans\' WHERE "service.name" = \'frontend\' AND "time" >= to_timestamp(1688713200000000000) AND "time" <= to_timestamp(1689537120000000000) GROUP BY "trace_id" ORDER BY t DESC LIMIT 20;'
        info = client.execute(query)

        reader = client.do_get(info.endpoints[0].ticket)
        table = reader.read_all()
        e = time.time()
        print(e - s)

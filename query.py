from flightsql import FlightSQLClient
import pandas

if __name__ == "__main__":
    client = FlightSQLClient(
        host="localhost",
        port="8082",
        insecure="true",
        token="xxx",
        metadata={"bucket-name": "otel_otel"},
    )

    info = client.execute("select trace_id from spans limit 5;")
    reader = client.do_get(info.endpoints[0].ticket)

    print(reader.read_all().to_pandas())

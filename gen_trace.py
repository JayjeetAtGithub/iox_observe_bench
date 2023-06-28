import requests
import random


def GET_req(url, params):
    print(url)
    resp = requests.get(url = url, params = params)
    print(resp)


if __name__ == "__main__":
    config_url = "http://localhost:8090/config"
    dispatch_url = "http://localhost:8090/dispatch"

    for i in range(1, 500):
        config_params = {"nonse": random.uniform(1.1, 1.9)}
        GET_req(config_url, config_params)

        dispatch_params = {"customer": random.randint(100, 999), "nonse": random.uniform(1.1, 1.9)}
        GET_req(dispatch_url, dispatch_params)

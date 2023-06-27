import requests
import random


def GET_req(url, params):
    resp = requests.get(url = config_url, params = config_params)
    print(resp)


if __name__ == "__main__":
    config_url = "http://localhost:8090/config"
    dispatch_url = "http://localhost:8090/dispatch?customer=392&nonse=0.5107292739627883"

    for i in range(1, 50000):
        config_params = {"nonse": random.uniform(1.1, 1.9)}
        GET_req(config_url, config_params)

        dispatch_params = {"customer": random.randint(100, 999), "nonse": random.uniform(1.1, 1.9)}
        GET_req(dispatch_url, dispatch_params)

import requests
import random
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor

def GET_req(url, params):
    print(url)
    resp = requests.get(url = url, params = params)
    print(resp)


if __name__ == "__main__":
    config_url = "http://localhost:8090/config"
    dispatch_url = "http://localhost:8090/dispatch"

    with ThreadPoolExecutor(max_workers=mp.cpu_count()) as executor:
        for i in range(100000):
            config_params = {"nonse": random.uniform(1.1, 1.9)}
            executor.submit(GET_req, config_url, config_params)

            dispatch_params = {"customer": 123, "nonse": random.uniform(1.1, 1.9)}
            executor.submit(GET_req, dispatch_url, dispatch_params)

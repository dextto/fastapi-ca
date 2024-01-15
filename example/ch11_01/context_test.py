from concurrent.futures import ThreadPoolExecutor, as_completed
import requests


def send_request(var: str):
    response = requests.get(f"http://localhost:8000/context?var={var}")
    return response.json()


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(send_request, str(i)) for i in range(10)]

    for future in as_completed(futures):
        print(future.result())

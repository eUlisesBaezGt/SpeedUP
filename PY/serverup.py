import requests
import time

def check_server_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Server is up and running!")
        else:
            print(f"Server is not accessible. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Server is not accessible. Error:", e)

def monitor_server(url, interval):
    while True:
        check_server_status(url)
        time.sleep(interval)

if __name__ == "__main__":
    server_url = "https://github.com/"  # Replace with your server URL
    check_interval = 60  # Check interval in seconds (e.g., every 60 seconds)

    monitor_server(server_url, check_interval)

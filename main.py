
import requests
import concurrent.futures

def check_proxy(proxy):
    try:
        response = requests.get("https://google.com", proxies={"https": proxy}, timeout=5)
        if response.status_code == 200:
            return proxy
        else:
            return None
    except Exception:
        return None

def main():
    proxy_file_path = ""  # Path to the .txt file containing proxies
    working_proxy_file_path = ""  # Path to the file to store working proxies

    with open(proxy_file_path, "r") as file:
        proxies = file.readlines()

    proxies = [proxy.strip() for proxy in proxies]

    working_proxies = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(check_proxy, proxies)

    for result in results:
        if result is not None:
            working_proxies.append(result)

    print(f"{len(working_proxies)} proxies are working out of {len(proxies)}")
    print("Working proxies:")
    for proxy in working_proxies:
        print(proxy)

    with open(working_proxy_file_path, "a") as file:  # Open file in append mode
        for proxy in working_proxies:
            file.write(proxy + "\n")

if __name__ == "__main__":
    main()

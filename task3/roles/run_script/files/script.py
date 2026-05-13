import requests

url = "https://tools-httpstatus.pickup-services.com/"

status_paths = ["200", "201", "301", "400", "500"]

for path in status_paths:
    final_url = url + path
    print("Request:", final_url)

    try:
        response = requests.get(final_url, timeout=5)

        code = response.status_code
        body = response.text

        if 100 <= code < 400:
            print("[OK]", code, body)
        else:
            raise Exception(f"[ERROR] {code} {body}")

    except Exception as e:
        print("Caught exception:", e)
        continue 
    